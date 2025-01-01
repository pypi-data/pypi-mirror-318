import os
import json
import click
from kuzco.core.case_manager import CaseManager

# # Validator for the app name (avoid app names who dont have docker image name pattern)
def validate_app_name(ctx, param, value):
    if not value.islower() or not all(c.isalnum() or c in {'-'} for c in value):
        raise click.BadParameter("App name must be lowercase and can only contain letters, numbers, and '-'.")
    return value

@click.command(context_settings={"ignore_unknown_options": True, "allow_extra_args": True})
@click.argument('command', type=click.Choice(['run', 'install', 'ci', 'restart'], case_sensitive=False))
@click.argument('type', type=click.Choice(['service', 'utils'], case_sensitive=False))
@click.argument('app_name', callback=validate_app_name)
@click.argument('config_path', type=click.Path(exists=True, dir_okay=True, file_okay=False), default='.')
@click.option('--docker', is_flag=True, help="Enable Docker support.")
@click.option('--uvicorn', is_flag=True, help="Enable Uvicorn with additional arguments.")
@click.pass_context
def cli(ctx, command, type, app_name, config_path, docker, uvicorn):
    """
    CLI tool for managing Python monorepos.

    COMMAND: run/install/ci/restart
    TYPE: service/utils
    APP_NAME: Name of the application (lowercase, numbers, and '-' only).
    CONFIG_PATH: Path to the base directory containing the config.json file.
    """
    # Resolve absolute path to config.json
    config_path = os.path.abspath(config_path)
    config_file = os.path.join(config_path, 'config.json')

    # Check if config.json exists
    if not os.path.isfile(config_file):
        click.echo(f"Error: config.json not found in {config_path}")
        return

    # Load config.json
    try:
        with open(config_file, 'r') as f:
            config_data = json.load(f)
    except json.JSONDecodeError:
        click.echo("Error: config.json is not a valid JSON file.")
        return

    # Capture extra arguments if uvicorn is enabled
    extra_args_dict = {}
    if uvicorn:
        for arg in ctx.args:
            if arg.startswith("--"):
                if "=" not in arg:
                    click.echo(f"Error: Invalid argument format: {arg}. Must be in the form --key=value.")
                    return
                key, value = arg[2:].split('=', 1)
                extra_args_dict[key] = value

    # Derive paths based on config and inputs
    project_base_dir = config_path
    mono_repo_base_dir = os.path.join(config_path, config_data.get("repo_name", "demo-repo"))
    services_dir = os.path.join(mono_repo_base_dir, config_data.get("services_dir", "services"))
    utils_dir = os.path.join(mono_repo_base_dir, config_data.get("utils_dir", "utils"))
    target_service_location = os.path.join(services_dir, app_name)
    target_service_venv_dir = os.path.join(target_service_location, config_data.get("venv_dir_name", ".venv"))
    target_service_main_file = os.path.join(target_service_location, "app", config_data.get("service_main_file", "main.py"))
    app_json_file = os.path.join(target_service_location, config_data.get("local_utils_file", "local-utils.json"))
    docker_ignore_file = os.path.join(mono_repo_base_dir, ".dockerignore")
    version_lock_file = os.path.join(mono_repo_base_dir, config_data.get("version_lock_file", "versions-lock.json"))

    # Check if any derived paths are missing
    required_paths = {
        "mono_repo_base_dir": mono_repo_base_dir,
        "services_dir": services_dir,
        "utils_dir": utils_dir,
        "target_service_location": target_service_location,
        "target_service_main_file": target_service_main_file,
        "app_json_file": app_json_file,
        "version_lock_file": version_lock_file,
    }

    for name, path in required_paths.items():
        if not os.path.exists(path):
            click.echo(f"Error: Required path '{name}' does not exist: {path}")
            return

    # Construct the final dictionary
    monopylib_args = {
        'cli_current_command': command,
        'project_base_dir': project_base_dir,
        'mono_repo_base_dir': mono_repo_base_dir,
        'target_service_location': target_service_location,
        'utils_dir': utils_dir,
        'target_service_venv_dir': target_service_venv_dir,
        'target_service_main_file': target_service_main_file,
        'app_json_file': app_json_file,
        'docker_ignore_file': docker_ignore_file,
        'version_lock_file': version_lock_file,
        'docker': str(docker).lower(),  # Add docker flag
        'uvicorn': str(uvicorn).lower(),
        'uvicorn_args': extra_args_dict,
    }

    # Print the resulting dictionary
    # click.echo(json.dumps(monopylib_args, indent=4))

    case_manager = CaseManager(monopylib_args)
    case_manager.execute()

if __name__ == '__main__':
    cli()
