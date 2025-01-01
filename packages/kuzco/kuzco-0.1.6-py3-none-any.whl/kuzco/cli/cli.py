import os
import json
import click
from kuzco.core.case_manager import CaseManager
from kuzco.core.creator_manager import CreatorManager

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
@click.argument('config_path', type=click.Path(exists=True, dir_okay=True, file_okay=False), default='.')
@click.option('--docker', is_flag=True, help="Enable Docker support.")
@click.option('--uvicorn', is_flag=True, help="Enable Uvicorn with additional arguments.")
@click.pass_context
def manage(ctx, command, type, app_name, config_path, docker, uvicorn):
    """
    Manage monorepo services or utils.

    COMMAND: run/install/ci/restart
    TYPE: service/utils
    APP_NAME: Name of the application (lowercase, numbers, and '-' only).
    CONFIG_PATH: Path to the base directory containing the config.json file.
    """
    config_path = os.path.abspath(config_path)
    config_file = os.path.join(config_path, 'config.json')

    if not os.path.isfile(config_file):
        click.echo(f"Error: config.json not found in {config_path}")
        return

    try:
        with open(config_file, 'r') as f:
            config_data = json.load(f)
    except json.JSONDecodeError:
        click.echo("Error: config.json is not a valid JSON file.")
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

    mono_repo_base_dir = os.path.join(config_path, config_data.get("repo_name", "demo-repo"))
    services_dir = os.path.join(mono_repo_base_dir, config_data.get("services_dir", "services"))
    target_service_location = os.path.join(services_dir, app_name)

    paths = {
        "project_base_dir" :config_path,
        "mono_repo_base_dir" : os.path.join(config_path, config_data.get("repo_name", "demo-repo")),
        "services_dir" : os.path.join(mono_repo_base_dir, config_data.get("services_dir", "services")),
        "utils_dir" :os.path.join(mono_repo_base_dir, config_data.get("utils_dir", "utils")),
        "target_service_location" : os.path.join(services_dir, app_name),
        "target_service_venv_dir" : os.path.join(target_service_location, config_data.get("venv_dir_name", ".venv")),
        "target_service_main_file" : os.path.join(target_service_location, "app", config_data.get("service_main_file", "main.py")),
        "app_json_file" : os.path.join(target_service_location, config_data.get("local_utils_file", "local-utils.json")),
        "docker_ignore_file" : os.path.join(mono_repo_base_dir, ".dockerignore"),
        "version_lock_file" : os.path.join(mono_repo_base_dir, config_data.get("version_lock_file", "versions-lock.json"))

    }

    for name, path in paths.items():
        if not os.path.exists(path):
            click.echo(f"Error: Required path '{name}' does not exist: {path}")
            return

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


@create.command()
@click.option('--repo-name', default="demo-repo", help="Name of the repository.")
@click.argument('base_path', type=click.Path(exists=True, file_okay=False))
def monorepo(repo_name, base_path):
    """
    Create a new monorepo structure.
    """
    creator = CreatorManager(base_path)
    creator.create_monorepo(repo_name)


@create.command()
@click.argument('service_name')
@click.argument('config_path', type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.option('--uvicorn', is_flag=True, default=False, help="Include uvicorn setup.")
def service(service_name, config_path, uvicorn):
    """
    Create a new service inside the monorepo.
    """
    creator = CreatorManager(os.path.dirname(config_path))
    creator.create_service(service_name, config_path, uvicorn)


@create.command()
@click.argument('util_name')
@click.argument('config_path', type=click.Path(exists=True, dir_okay=True, file_okay=False))
def util(util_name, config_path):
    """
    Create a new utility inside the monorepo.
    """
    creator = CreatorManager(os.path.dirname(config_path))
    creator.create_util(util_name, config_path)


if __name__ == '_main_':
    cli()