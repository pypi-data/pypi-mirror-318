import logging
import sys

import click

from .loader_local_file import Local_file_loader
from .Permission_state import Permission_state
from .Spesification import Spesification


@click.group()
@click.version_option(version="0.1.0")
@click.option("--log-level", default="info", help="set logglevel for run")
def cli(log_level):
    """Tundra: A CLI tool for managing permissions and roles."""
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)

    if log_level == "info":
        handler.setLevel(logging.INFO)
    elif log_level == "error":
        handler.setLevel(logging.ERROR)
    elif log_level == "debug":
        handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)
    pass


@cli.command()
@click.option("--verification", is_flag=True, help="Run permission file verification")
@click.option(
    "--generate-roles",
    is_flag=True,
    help="Generate AR roles that are not in permissions file",
)
@click.option(
    "--permission-path",
    default=".",
    help="Path to permissions file or directory containing permissions file",
)
@click.option("--state-path", default="", help="Path to the current state file")
@click.option("--change-path", default="", help="Path for printing change output file")
def plan(verification, generate_roles, permission_path, state_path, change_path):
    """Plan changes to permissions and roles."""
    permissions = process_permissions(verification, generate_roles, permission_path)
    previous_state = Permission_state().load(Local_file_loader("yaml"), state_path)
    planned_state = Permission_state(permissions).generate()
    planned_state.compare(previous_state)
    planned_state.plan(change_path)
    click.echo("Plan completed.")


@cli.command()
@click.option("--verification", is_flag=True, help="Run permission file verification")
@click.option(
    "--generate-roles",
    is_flag=True,
    help="Generate AR roles that are not in permissions file",
)
@click.option(
    "--permission-path",
    default=".",
    help="Path to permissions file or directory containing permissions file",
)
@click.option(
    "--export-path",
    default="./permifrost_permissions.yml",
    help="Location for the processed permifrost file",
)
def apply(verification, generate_roles, permission_path, export_path):
    """Apply changes to permissions and roles."""
    permissions = process_permissions(verification, generate_roles, permission_path)
    permissions.export(export_path)
    click.echo(f"Changes applied and exported to {export_path}")


@cli.command()
@click.option("--verification", is_flag=True, help="Run permission file verification")
@click.option(
    "--generate-roles",
    is_flag=True,
    help="Generate AR roles that are not in permissions file",
)
@click.option(
    "--permission-path",
    default=".",
    help="Path to permissions file or directory containing permissions file",
)
def verify(verification, generate_roles, permission_path):
    """Verify permissions and roles."""
    process_permissions(verification, generate_roles, permission_path)
    click.echo("Verification completed.")


def process_permissions(verification, generate_roles, permission_path):
    permissions = Spesification(verification, generate_roles)
    permissions.load(permission_path)
    permissions.identify_modules()
    permissions.identify_entities()
    permissions.generate()
    return permissions


if __name__ == "__main__":
    cli()
