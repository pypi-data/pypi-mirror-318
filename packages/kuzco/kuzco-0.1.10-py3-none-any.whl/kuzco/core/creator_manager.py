import os
import json


class CreatorManager:
    def __init__(self, base_path):
        self.base_path = os.path.abspath(base_path)
        self.config = {
            "repo_name": "src",
            "services_dir": "services",
            "utils_dir": "utils",
            "venv_dir_name": ".venv",
            "version_lock_file": "versions-lock.json",
            "service_main_file": "main.py",
            "local_utils_file": "local-utils.json",
        }
    def create_monorepo(self):
        repo_name="src"
        repo_path = os.path.join(self.base_path, repo_name)

        # Create main repo folder and subfolders
        os.makedirs(os.path.join(repo_path, "services"), exist_ok=True)
        os.makedirs(os.path.join(repo_path, "utils"), exist_ok=True)

        # Create README.md in the base path
        readme_path = os.path.join(self.base_path, "README.md")
        with open(readme_path, "w") as readme_file:
            readme_file.write(f"# {repo_name}\n\nWelcome to the {repo_name} monorepo!")

        # Create versions-lock.json inside the repo_name folder
        version_lock_path = os.path.join(repo_path, "versions-lock.json")
        version_lock_data = {"common_requirements": ["some-pip-package==x.y.z"]}
        self._write_json(version_lock_path, version_lock_data)

        print(f"Monorepo '{repo_name}' created at {repo_path}")

    def create_service(self, service_name, uvicorn=False):
        # Use constraints from the config dictionary
        repo_path = os.path.join(self.base_path, self.config["repo_name"])
        service_path = os.path.join(repo_path, self.config["services_dir"], service_name)
        os.makedirs(service_path, exist_ok=True)
        os.makedirs(os.path.join(service_path, "app"), exist_ok=True)

        self._write_file(os.path.join(service_path, "app", "__init__.py"), "")
        self._write_file(
            os.path.join(service_path, "app", "main.py"), self._generate_main_py(uvicorn)
        )
        self._write_json(
            os.path.join(service_path, self.config["local_utils_file"]),
            {"local_dependencies": []},
        )
        self._write_file(os.path.join(service_path, "requirements.txt"), "")

        print(f"Service '{service_name}' created at {service_path}")

    def create_util(self, util_name):
        # Use constraints from the config dictionary
        repo_path = os.path.join(self.base_path, self.config["repo_name"])
        util_path = os.path.join(repo_path, self.config["utils_dir"], util_name)
        os.makedirs(util_path, exist_ok=True)
        os.makedirs(os.path.join(util_path, "app"), exist_ok=True)

        self._write_file(os.path.join(util_path, "app", "__init__.py"), "")
        self._write_file(
            os.path.join(util_path, "app", f"{util_name}.py"), f"# {util_name} utility"
        )
        self._write_json(
            os.path.join(util_path, self.config["local_utils_file"]),
            {"local_dependencies": []},
        )
        self._write_file(os.path.join(util_path, "requirements.txt"), "")

        print(f"Utility '{util_name}' created at {util_path}")
    def _write_json(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def _write_file(self, path, content):
        with open(path, "w") as f:
            f.write(content)

    def _load_json(self, path: str) -> dict:
        """
        Load a JSON file from the specified path.
        Ensure the path points to a file, not a directory.
        """
        if os.path.isdir(path):  # Check if the path is a directory
            path = os.path.join(path, "config.json")  # Append the config.json file name

        if not os.path.exists(path):  # Ensure the file exists
            raise FileNotFoundError(f"JSON file not found at {path}")

        with open(path, "r") as f:
            return json.load(f)

    def _generate_main_py(self, uvicorn):
        if uvicorn:
            return (
                "import uvicorn\n"
                "if __name__ == '__main__':\n"
                "    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)"
            )
        return "# Main application entry point"
