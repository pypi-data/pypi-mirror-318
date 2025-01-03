import os
import json
import click
from kuzco.core.case_manager import CaseManager
from kuzco.core.creator_manager import CreatorManager
from kuzco.scripts.tree import ProjectTreeBuilder

# Validator for app name
def validate_app_name(ctx, param, value):
    if not value.islower() or not all(c.isalnum() or c in {'-'} for c in value):
        raise click.BadParameter("App name must be lowercase and can only contain letters, numbers, and '-'.")
    return value

@click.group()
def cli():
    """
    CLI tool for managing Python monorepos.
    """
    pass

@cli.command(context_settings={"ignore_unknown_options": True, "allow_extra_args": True})
@click.argument('command', type=click.Choice(['run', 'install', 'ci', 'restart'], case_sensitive=False))
@click.argument('type', type=click.Choice(['service', 'utils'], case_sensitive=False))
@click.argument('app_name', callback=validate_app_name)
@click.option('--docker', is_flag=True, help="Enable Docker support.")
@click.option('--uvicorn', is_flag=True, help="Enable Uvicorn with additional arguments.")
@click.pass_context
def manage(ctx, command, type, app_name, docker, uvicorn):
    """
    Manage monorepo services or utils.

    COMMAND: run/install/ci/restart
    TYPE: service/utils
    APP_NAME: Name of the application (lowercase, numbers, and '-' only).
    """
    # Hardcoded configuration
    config_data = {
        "repo_name": "src",
        "services_dir": "services",
        "utils_dir": "utils",
        "venv_dir_name": ".venv",
        "version_lock_file": "versions-lock.json",
        "service_main_file": "main.py",
        "local_utils_file": "local-utils.json"
    }

    config_path = os.getcwd()  # Use current working directory as the base
    mono_repo_base_dir = os.path.join(config_path, config_data["repo_name"])
    services_dir = os.path.join(mono_repo_base_dir, config_data["services_dir"])

    # Construct paths
    paths = {
        "project_base_dir": config_path,
        "mono_repo_base_dir": mono_repo_base_dir,
        "services_dir": services_dir,
        "utils_dir": os.path.join(mono_repo_base_dir, config_data["utils_dir"]),
        "target_service_location": os.path.join(services_dir, app_name),
        "target_service_venv_dir": os.path.join(services_dir, app_name, config_data["venv_dir_name"]),
        "target_service_main_file": os.path.join(services_dir, app_name, "app", config_data["service_main_file"]),
        "app_json_file": os.path.join(services_dir, app_name, config_data["local_utils_file"]),
        "docker_ignore_file": os.path.join(config_path, ".dockerignore"),
        "version_lock_file": os.path.join(mono_repo_base_dir, config_data["version_lock_file"])
    }
    required_paths = {
        "project_base_dir": config_path,
        "mono_repo_base_dir": mono_repo_base_dir,
        "services_dir": services_dir,
        "utils_dir": os.path.join(mono_repo_base_dir, config_data["utils_dir"]),
        "target_service_location": os.path.join(services_dir, app_name),
        "target_service_main_file": os.path.join(services_dir, app_name, "app", config_data["service_main_file"]),
        "app_json_file": os.path.join(services_dir, app_name, config_data["local_utils_file"]),
        "version_lock_file": os.path.join(mono_repo_base_dir, config_data["version_lock_file"])
    }

    for name, path in required_paths.items():
        if not os.path.exists(path):
            click.echo(f"Error: Required path '{name}' does not exist: {path}")
            return   

    extra_args_dict = {}
    if uvicorn:
        for arg in ctx.args:
            if arg.startswith("--"):
                if "=" not in arg:
                    click.echo(f"Error: Invalid argument format: {arg}. Must be in the form --key=value.")
                    return
                key, value = arg[2:].split('=', 1)
                extra_args_dict[key] = value

    monopylib_args = {
        'cli_current_command': command,
        'docker': str(docker).lower(),
        'uvicorn': str(uvicorn).lower(),
        'uvicorn_args': extra_args_dict,
        **paths
    }

    case_manager = CaseManager(monopylib_args)
    case_manager.execute()

@cli.group()
def create():
    """
    Create monorepo structures and files.
    """
    pass


import click

@create.command()
@click.option('--base-path', default=".", show_default=True, type=click.Path(exists=True, file_okay=False), help="Base path for creating the monorepo.")
def monorepo(base_path):
    """
    Create a new monorepo structure.
    """
    creator = CreatorManager(base_path)
    creator.create_monorepo()


@create.command()
@click.argument('service_name')
@click.argument('base_path', type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.option('--uvicorn', is_flag=True, default=False, help="Include uvicorn setup.")
def service(service_name, base_path, uvicorn):
    """
    Create a new service inside the monorepo.
    """
    creator = CreatorManager(os.path.dirname(base_path))
    creator.create_service(service_name,  uvicorn)


@create.command()
@click.argument('util_name')
@click.argument('base_path', type=click.Path(exists=True, dir_okay=True, file_okay=False))
def util(util_name, base_path):
    """
    Create a new utility inside the monorepo.
    """
    creator = CreatorManager(os.path.dirname(base_path))
    creator.create_util(util_name)

@cli.group()
def tree():
    """
    Generate and display the project tree structure.
    """
    pass

@tree.command()
@click.argument('base_dir', type=click.Path(exists=True), default='.')
def show(base_dir):
    """
    Show the project tree structure based on the provided base directory.
    BASE_DIR: Path to the base directory of the project.
    """
    try:
        builder = ProjectTreeBuilder(base_dir)
        tree = builder.build_tree()
        click.echo(json.dumps(tree, indent=2))
    except Exception as e:
        click.echo(f"Error: {e}")


if __name__ == '_main_':
    cli()