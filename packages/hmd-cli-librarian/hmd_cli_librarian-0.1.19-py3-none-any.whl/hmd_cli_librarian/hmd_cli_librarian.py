# Implement the lifecycle commands here
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from tempfile import gettempdir
import requests
import boto3
from cement import minimal_logger

from hmd_cli_tools import cd
from hmd_cli_tools.hmd_cli_tools import read_manifest, load_hmd_env
from hmd_cli_neuronsphere.hmd_cli_neuronsphere import (
    start_neuronsphere,
    stop_neuronsphere,
    run_local_service,
)
from hmd_lib_librarian_client.artifact_tools import (
    content_item_path_from_spec,
)
from hmd_cli_tools.prompt_tools import prompt_for_values
from typing import Dict

import yaml

logger = minimal_logger(__name__)


minio_script = """
curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc
export PATH=$PATH:$HOME/minio-binaries/

mc alias set localminio http://minio:9000 {access_key} {secret_key}
mc admin config set localminio/ notify_webhook:{repo_name} \
    endpoint="http://proxy/{instance_name}/apiop/handle_events"
mc admin service restart localminio
mc event add localminio/{bucket_name} arn:minio:sqs::{repo_name}:webhook \
  --event put,delete
"""


def validate_config(config: Dict) -> bool:
    valid = True
    logger.info(config)
    if "content_path_configs" not in config:
        logger.error("Invalid Config: missing 'content_path_configs' property")
        valid = False

    if "content_items_paths" in config and not isinstance(
        config["content_path_configs"], dict
    ):
        logger.error("Invalid Config: 'content_path_configs' must be a dictionary")
        valid = False

    return valid


def merge_config(orig: dict, override: dict) -> dict:
    ret = {**orig}
    logger.info(f"orig: {orig}")
    for k, v in override.items():
        orig_val = orig.get(k)

        if orig_val is None:
            ret[k] = v
            continue

        if isinstance(v, dict) and isinstance(orig_val, dict):
            ret[k] = v
            continue

        # if isinstance(v, list) and isinstance(orig_val, list):
        #     ret[k] = [
        #         *orig_val,
        #         *v,
        #     ]
        #     continue

        ret[k] = orig_val

    logger.info(f"merge: {ret}")
    return ret


def get_config(config_file: str = "./src/configs/default.librarian.json"):
    manifest = read_manifest()

    manifest_cfg = manifest.get("deploy", {}).get("default_configuration", None)

    if config_file is None:
        config_file = "./src/configs/default.librarian.json"

    librarian_cfg_path = Path(config_file)

    if not os.path.exists(librarian_cfg_path) and manifest_cfg is None:
        raise Exception(
            f"Cannot find Librarian configuration file at {config_file} or in manifest.json"
        )
    if manifest_cfg is None:
        manifest_cfg = {}
    local_override_path = "./meta-data/config_local.json"
    if manifest_cfg is not None and os.path.exists(local_override_path):
        with open(local_override_path, "r") as lo:
            local_override = json.load(lo)
            manifest_cfg = merge_config(manifest_cfg, local_override)

    if os.path.exists(librarian_cfg_path):
        with open(librarian_cfg_path, "r") as cfg:
            librarian_cfg = json.load(cfg)
            if "instance_configuration" in librarian_cfg:
                librarian_cfg = librarian_cfg["instance_configuration"]
            manifest_cfg = merge_config(manifest_cfg, librarian_cfg)

    return manifest_cfg


def update_setup_py(setup_path: Path, repo_name: str):
    with open(setup_path, "r") as setup:
        setup_data = setup.read().splitlines()

    output = []
    found = False
    for line in setup_data:
        if line.strip().startswith('name="hmd-lang-local-librarian",'):
            found = True
            indent = line.index("name")
            output.append((" " * indent) + f'name="{repo_name}",')
        else:
            output.append(line)
    if not found:
        raise Exception("setup.py doesn't contain an empty 'name' line.")
    with open(setup_path, "w") as setup:
        setup.writelines(f"{line}\n" for line in output)


def create_local_bucket(bucket_name: str):
    session = boto3.Session(
        aws_access_key_id="minioadmin", aws_secret_access_key="minioadmin"
    )

    s3_client = session.client("s3", endpoint_url="http://localhost:9000")
    try:
        s3_client.create_bucket(Bucket=bucket_name)
    except:
        pass


def start_dependencies(dependencies: dict):
    service_override = {}
    repo_home = Path(os.environ.get("HMD_REPO_HOME"))
    for k, v in dependencies.items():
        repo_class_name = v.get("repo_class_name")
        dep_repo = repo_home / repo_class_name

        if os.path.exists(dep_repo):
            with open(dep_repo / "meta-data" / "VERSION", "r") as version:
                repo_version = version.read().strip()
            run_local_service(repo_class_name, repo_version)
            service_override[k] = repo_class_name
        else:
            service_override[k] = "local"

    return service_override


def start(
    instance_name: str,
    config_file: str = "./src/configs/default.librarian.json",
    image: str = None,
):
    load_hmd_env()
    _hmd_home = os.environ.get("HMD_HOME")

    librarian_cfg = get_config(config_file=config_file)

    if not validate_config(librarian_cfg):
        return

    root_path = Path("./").absolute()

    schemas_path = root_path / Path(librarian_cfg.get("schemas", "./src/schemas"))

    if not os.path.exists(schemas_path):
        logger.info(
            "Cannot find schemas in project. Must be installed in Docker image."
        )

    if librarian_cfg.get("content_item_types") is None:
        cit_path = librarian_cfg.get(
            "content_item_type_config",
            "./src/entities/hmd_lang_librarian.content_item_type",
        )
    else:
        cit_path = librarian_cfg.get(
            "content_item_types",
            "./src/entities/hmd_lang_librarian.content_item_type",
        )

    try:
        if "@" in cit_path:
            cit_repo = cit_path.split("@")[0]
            cit_path = (
                Path("..")
                / cit_repo
                / "src"
                / "entities"
                / "hmd_lang_librarian.content_item_type"
            )
    except:
        pass

    cit_path = root_path / Path(cit_path)

    logger.info(f"Content Item Type Path: {cit_path}")
    if not os.path.exists(cit_path):
        raise Exception("Cannot find ContentItemTypes")

    repo_name = os.path.basename(os.getcwd())
    _dirname = Path(os.path.dirname(__file__))
    _librarian_dir = _dirname / "local_librarian_prj"

    tmpdir = gettempdir()
    tmp_path = Path(tmpdir)
    cache_path = Path(_hmd_home) / ".cache" / "local_services"

    if not (cache_path / repo_name).exists():
        os.makedirs(cache_path / repo_name, exist_ok=True)

    prj_dir = Path(os.getcwd())
    if not os.path.exists(tmp_path / repo_name):
        os.mkdir(tmp_path / repo_name)

    build_lib = False
    local_dc = {}

    if os.path.exists(prj_dir / "src" / "docker" / "docker-compose.local.yaml"):
        with open(
            prj_dir / "src" / "docker" / "docker-compose.local.yaml", "r"
        ) as dc_local:
            local_dc = yaml.safe_load(dc_local)

    if not os.path.exists("./src/docker"):
        build_lib = True
        shutil.copytree(_librarian_dir, tmp_path / repo_name, dirs_exist_ok=True)

        with open(tmp_path / repo_name / "meta-data" / "manifest.json", "r") as mf:
            manifest = json.load(mf)

        manifest["global_variables"] = {
            "base_package": repo_name.replace("-", "_"),
            "package_name": repo_name.replace("-", "_"),
        }

        with open(tmp_path / repo_name / "meta-data" / "manifest.json", "w") as mf:
            json.dump(manifest, mf)

        with open(tmp_path / repo_name / "meta-data" / "config_local.json", "r") as cfg:
            config_local = json.load(cfg)

        config_local["loader_config"] = {"local": ["hmd-lang-librarian", repo_name]}

        config_local["hmd_db_engines"]["dynamo"]["engine_config"][
            "dynamo_table"
        ] = f"{repo_name}-librarian"

        with open(tmp_path / repo_name / "meta-data" / "config_local.json", "w") as cfg:
            json.dump(config_local, cfg)

        with open(Path(os.getcwd()) / "meta-data" / "config_local.json", "w") as cfg:
            json.dump({"service_config": config_local}, cfg)

        update_setup_py(tmp_path / repo_name / "src" / "python" / "setup.py", repo_name)

        if os.path.exists(schemas_path):
            shutil.copytree(
                schemas_path,
                tmp_path / repo_name / "src" / "schemas",
                dirs_exist_ok=True,
            )
        if os.path.exists(cit_path):
            shutil.copytree(
                cit_path, tmp_path / repo_name / "src" / "cit", dirs_exist_ok=True
            )

        if not os.path.exists(tmp_path / repo_name / "src" / "docker"):
            os.mkdir(tmp_path / repo_name / "src" / "docker")

        if os.path.exists(schemas_path):
            with cd(tmp_path / repo_name):
                mickey = subprocess.run(["hmd", "mickey", "build"])

                if mickey.returncode > 0:
                    logger.error(mickey.stderr)
                    raise Exception("Error compiling schemas")

                pip_install = subprocess.run(
                    [
                        "pip",
                        "install",
                        "-e",
                        str(tmp_path / repo_name / "src" / "python"),
                    ]
                )

                if pip_install.returncode > 0:
                    logger.error(pip_install.stderr)
                    raise Exception("Error installing schemas")

        prj_dir = tmp_path / repo_name

    with cd(prj_dir):
        manifest = read_manifest()

        dependencies = manifest.get("deploy", {}).get("dependencies", {})

        session = boto3.Session()

        credentials = {
            "access_key": "dummykey",
            "secret_key": "dummykey",
            "token": None,
        }
        if "bucket_name" in librarian_cfg:
            creds = session.get_credentials()
            credentials = {
                "access_key": creds.access_key,
                "secret_key": creds.secret_key,
                "token": creds.token,
            }

        s3_endpoint = None
        bucket_name = f"{repo_name}-default-bucket"
        if "bucket_name" not in librarian_cfg:
            logger.info(f"Creating local bucket {bucket_name}")
            create_local_bucket(bucket_name)
            credentials["access_key"] = "minioadmin"
            credentials["secret_key"] = "minioadmin"
            credentials["token"] = None
            s3_endpoint = "http://minio:9000/"

            with open(
                cache_path / repo_name / f"{instance_name}_minio_config.sh", "w"
            ) as mc:
                mc.write(
                    minio_script.format(
                        bucket_name=bucket_name,
                        repo_name=repo_name,
                        instance_name=repo_name.replace("-", "_"),
                        access_key=credentials["access_key"],
                        secret_key=credentials["secret_key"],
                    )
                )

        if image is None:
            image_tag = (
                f"{os.environ.get('HMD_CONTAINER_REGISTRY', 'ghcr.io/neuronsphere')}/hmd-ms-librarian:{os.environ.get('HMD_MS_LIBRARIAN_VERSION', 'stable')}"
                if build_lib
                else f"{os.environ.get('HMD_CONTAINER_REGISTRY', 'ghcr.io/neuronsphere')}/{repo_name}:0.1"
            )
        else:
            image_tag = image
        logger.debug(f"Image Name: {image_tag}")
        default_docker_compose = {
            "services": {
                repo_name.replace("-", "_"): {
                    "image": image_tag,
                    "container_name": instance_name,
                    "environment": {
                        "AWS_ACCESS_KEY_ID": credentials["access_key"],
                        "AWS_SECRET_ACCESS_KEY": credentials["secret_key"],
                        "AWS_SESSION_TOKEN": credentials["token"],
                        "HMD_CUSTOMER_CODE": "hmd",
                        "HMD_DID": "aaa",
                        "HMD_ENVIRONMENT": "local",
                        "HMD_REGION": "reg1",
                        "HMD_INSTANCE_NAME": repo_name,
                        "BUCKET_NAME": librarian_cfg.get("bucket_name", bucket_name),
                        "S3_ENDPOINT": s3_endpoint,
                        "CONTENT_PATH_CONFIGS": json.dumps(
                            librarian_cfg["content_path_configs"]
                        ),
                        "GRAPH_QUERY_CONFIG": json.dumps(
                            librarian_cfg.get("graph_queries", {})
                        ),
                        # "HMD_SERVICE_NAME_OVERRIDES": json.dumps(service_override),
                        "SERVICE_CONFIG": json.dumps(
                            librarian_cfg.get("service_config", {})
                        ),
                    },
                    "depends_on": ["dynamodb", "graph-db"],
                    "volumes": [
                        f"{str(cit_path)}:/content_item_types",
                    ],
                },
            }
        }

        if os.path.exists(cache_path / repo_name / f"{instance_name}_minio_config.sh"):
            default_docker_compose["services"]["minio_config"] = {
                "image": "quay.io/minio/minio:RELEASE.2023-04-28T18-11-17Z",
                "entrypoint": "/bin/bash",
                "command": "/root/minio_config.sh",
                "volumes": [
                    f"{str(cache_path / repo_name / f'{instance_name}_minio_config.sh')}:/root/minio_config.sh"
                ],
            }

        default_docker_compose = merge_config(default_docker_compose, local_dc)

        local_mnts = []

        if os.path.exists(prj_dir / "src" / "python") and os.path.exists(schemas_path):
            local_mnts.append(repo_name)
        run_local_service(
            repo_name,
            "0.0.1",
            instance_name,
            local_mnts,
            db_init=False,
            docker_compose=default_docker_compose,
        )


def stop():
    stop_neuronsphere()


def reload():
    start()


# TODO: Make the following method prompts more interactive to create attributes, etc.


def add_content_item_type():
    questions = {
        "short_name": {"type": "input", "required": True},
        "description": {},
        "match_regex": {},
        "mime_type": {},
    }

    data = prompt_for_values(questions, False)

    data["match_regex"] = re.compile(data["match_regex"]).pattern

    filepath = f'./src/entities/hmd_lang_librarian.content_item_type/{data["short_name"]}.cit.hmdentity'

    if os.path.exists(filepath):
        raise Exception(f"ContentItemType already exists: {filepath}")

    with open(
        filepath,
        "w",
    ) as cit:
        json.dump(data, cit, indent=2)


def add_noun():
    questions = {"name": {"required": True}}

    data = prompt_for_values(questions, False)
    namespace = os.path.basename(os.getcwd()).replace("-", "_")

    filepath = f'./src/schemas/{namespace}/{data["name"]}.hms'

    if os.path.exists(filepath):
        raise Exception(f"Noun already exists: {filepath}")

    with open(filepath, "w") as n:
        json.dump(
            {
                "namespace": namespace,
                "name": data["name"],
                "metatype": "noun",
                "attributes": {},
            },
            n,
            indent=2,
        )


def add_relationship():
    questions = {
        "name": {"required": True},
        "ref_from": {"required": True},
        "ref_to": {"required": True},
    }

    data = prompt_for_values(questions, False)
    namespace = os.path.basename(os.getcwd()).replace("-", "_")

    filepath = f'./src/schemas/{namespace}/{data["name"]}.hms'

    if os.path.exists(filepath):
        raise Exception(f"Relationship already exists: {filepath}")

    with open(filepath, "w") as n:
        json.dump(
            {
                "namespace": namespace,
                "name": data["name"],
                "ref_from": data["ref_from"],
                "ref_to": data["ref_to"],
                "metatype": "relationship",
                "attributes": {},
            },
            n,
            indent=2,
        )
