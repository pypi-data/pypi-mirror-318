import sys

from pygeai.cli.commands import ArgumentsEnum, Command, Option
from pygeai.cli.commands.admin import admin_commands
from pygeai.cli.commands.assistant import assistant_commands
from pygeai.cli.commands.builders import build_help_text
from pygeai.cli.commands.chat import chat_commands
from pygeai.cli.commands.configuration import configure, configuration_options
from pygeai.cli.commands.organization import organization_commands
from pygeai.cli.texts.help import HELP_TEXT
from pygeai.cli import __version__ as cli_version


def show_help():
    """
    Displays help text in stdout
    """
    help_text = build_help_text(base_commands, HELP_TEXT)
    sys.stdout.write(help_text)


def show_version():
    """
    Displays version in stdout
    """
    sys.stdout.write(
        f" - Globant Enterprise AI: GEAI cli utility. Version: {cli_version}\n"
    )


"""
Commands that have available subcommands should have action None, so the parser knows that it shouldn't
run any action but instead send it to process again to identify subcommand.
"""

base_commands = [
    Command(
        "help",
        ["help", "h"],
        "Display help text",
        show_help,
        ArgumentsEnum.NOT_AVAILABLE,
        [],
        []
    ),
    Command(
        "version",
        ["version", "v"],
        "Display version text",
        show_version,
        ArgumentsEnum.NOT_AVAILABLE,
        [],
        []
    ),
    Command(
        "configure",
        ["configure", "config", "c"],
        "Setup the environment variables required to interact with GEAI",
        configure,
        ArgumentsEnum.OPTIONAL,
        [],
        configuration_options
    ),
    Command(
        "organization",
        ["organization", "org"],
        "Invoke organization endpoints to handle project parameters",
        None,
        ArgumentsEnum.REQUIRED,
        organization_commands,
        [],
    ),
    Command(
        "assistant",
        ["assistant", "ast"],
        "Invoke assistant endpoints to handle assistant parameters",
        None,
        ArgumentsEnum.REQUIRED,
        assistant_commands,
        [],
    ),
    Command(
        "chat",
        ["chat"],
        "Invoke chat endpoints to handle chat with assistants parameters",
        None,
        ArgumentsEnum.REQUIRED,
        chat_commands,
        [],
    ),
    Command(
        "admin",
        ["admin", "adm"],
        "Invoke admin endpoints designed for internal use",
        None,
        ArgumentsEnum.REQUIRED,
        admin_commands,
        []
    )

]


base_options = (
    Option(
        "output",
        ["--output", "-o"],
        "Set output file to save the command result",
        True
    ),
)
