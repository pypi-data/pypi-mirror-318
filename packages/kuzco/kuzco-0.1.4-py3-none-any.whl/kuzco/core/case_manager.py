from kuzco.core.venv_manager import VenvManager
from kuzco.core.run_manager import RunManager
from kuzco.core.pip_manager import PipManager
from kuzco.core.ci_manager import CIManager
from kuzco.helpers.logger import get_logger


logger = get_logger(__name__)

class CaseManager:
    def __init__(self, args):
        self.args = args

    def execute(self):
        command = self.args.get("cli_current_command")
        if command == "run":
            self.run_service()
        elif command == "ci":
            self.run_ci()
        elif command == "install":
            self.install_dependencies()
        elif command == "restart":
            self.restart_service()
        else:
            print(f"Unknown command: {command}")

    def run_service(self):
        print("Executing 'run' command.")
        run_manager = RunManager(self.args)
        try:
            run_manager.run_main()
        except Exception as e:
            print(f"Error running the service: {e}")


    def run_ci(self):
        print("Executing 'ci' command.")
        ci_manager = CIManager(self.args)
        ci_manager.generate_dockerignore()


    def install_dependencies(self):

        print("Executing 'install' command.")
        # venv_manager = VenvManager(self.args)
        # venv_manager.create_venv()
        # venv_manager.activate_venv()

        # Use PipManager for dependency management
        pip_manager = PipManager(self.args)
        pip_manager.install_dependencies()

    def restart_service(self):
        print("Executing 'restart' command.")
