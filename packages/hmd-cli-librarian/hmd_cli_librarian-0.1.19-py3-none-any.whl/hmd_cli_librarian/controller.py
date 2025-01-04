import os

from cement import Controller, ex
from importlib.metadata import version
from hmd_cli_tools import load_hmd_env

VERSION_BANNER = """
hmd librarian version: {}
"""

VERSION = version("hmd_cli_librarian")


class LocalController(Controller):
    class Meta:
        label = "librarian"

        stacked_type = "nested"
        stacked_on = "base"

        # text displayed at the top of --help output
        description = "CLI tool for developing Librarians locally"

        arguments = (
            (
                ["-v", "--version"],
                {
                    "help": "Display the version of the librarian command.",
                    "action": "version",
                    "version": VERSION_BANNER.format(VERSION),
                },
            ),
        )

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help="start a local Librarian",
        arguments=[
            (
                ["instance_name"],
                {
                    "help": "name to assign service",
                    "action": "store",
                },
            ),
            (
                ["-cf", "--config-file"],
                {
                    "action": "store",
                    "dest": "config_file",
                },
            ),
            (
                ["-img", "--image"],
                {"action": "store", "dest": "image", "help": "Docker image to start"},
            ),
        ],
    )
    def start(self):
        args = {
            "instance_name": self.app.pargs.instance_name,
            "config_file": self.app.pargs.config_file,
            "image": self.app.pargs.image,
        }
        load_hmd_env(override=False)
        from .hmd_cli_librarian import start as do_start

        do_start(**args)

    @ex(
        help="reload a local Librarian",
        arguments=[
            (
                ["instance_name"],
                {
                    "help": "name to assign service",
                    "action": "store",
                },
            ),
        ],
    )
    def reload(self):
        load_hmd_env(override=False)
        from .hmd_cli_librarian import reload as do_reload

        do_reload(self.app.pargs.instance_name)

    @ex(
        help="stop a local Librarian",
        arguments=[
            (
                ["instance_name"],
                {
                    "help": "name to assign service",
                    "action": "store",
                },
            ),
        ],
    )
    def stop(self):
        load_hmd_env(override=False)
        from .hmd_cli_librarian import stop as do_stop

        do_stop(self.app.pargs.instance_name)

    @ex(
        help="adds a new ContentItemType",
        arguments=[
            (
                ["entity_type"],
                {
                    "action": "store",
                    "choices": ["cit", "noun", "relationship"],
                },
            )
        ],
    )
    def add(self):
        if self.app.pargs.entity_type == "cit":
            from .hmd_cli_librarian import add_content_item_type as do_add

            do_add()
            return
        if self.app.pargs.entity_type == "noun":
            from .hmd_cli_librarian import add_noun as do_add

            do_add()
            return
        if self.app.pargs.entity_type == "relationship":
            from .hmd_cli_librarian import add_relationship as do_add

            do_add()
            return
