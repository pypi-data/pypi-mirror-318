import os
import json
from collections import defaultdict

class ProjectTreeBuilder:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.services = []
        self.service_dependencies = {}
        self.utils = []
        self.util_dependencies = {}
        self.util_to_services = defaultdict(set)

    def load_config(self, config_path):
        """Load the configuration from the specified config.json."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in config file: {config_path}")

    def load_local_utils(self, file_path):
        """Load the local-utils.json file and return its dependencies."""
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    return data.get('local_dependencies', [])
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON format in local-utils file: {file_path}")
        return []

    def process_services(self):
        """Process services and their dependencies."""
        services_dir = self.config['services_dir']
        local_utils_file = self.config['local_utils_file']

        services_path = os.path.join(os.getcwd(), self.config['repo_name'], services_dir)
        for service in os.listdir(services_path):
            service_path = os.path.join(services_path, service)
            if os.path.isdir(service_path):
                self.services.append(service)
                utils_path = os.path.join(service_path, local_utils_file)
                dependencies = self.load_local_utils(utils_path)
                self.service_dependencies[service] = dependencies

    def process_utils(self):
        """Process utils and their dependencies."""
        utils_dir = self.config['utils_dir']
        local_utils_file = self.config['local_utils_file']

        utils_path = os.path.join(os.getcwd(), self.config['repo_name'], utils_dir)
        for util in os.listdir(utils_path):
            util_path = os.path.join(utils_path, util)
            if os.path.isdir(util_path):
                self.utils.append(util)
                utils_file_path = os.path.join(util_path, local_utils_file)
                dependencies = self.load_local_utils(utils_file_path)
                self.util_dependencies[util] = dependencies

    def map_utils_to_services(self):
        """Map utils to services that depend on them directly or indirectly."""
        def resolve_dependencies(service, dependencies):
            for dependency in dependencies:
                self.util_to_services[dependency].add(service)
                resolve_dependencies(service, self.util_dependencies.get(dependency, []))

        for service, dependencies in self.service_dependencies.items():
            resolve_dependencies(service, dependencies)

    def build_tree(self):
        """Build the project tree by processing services, utils, and their dependencies."""
        self.process_services()
        self.process_utils()
        self.map_utils_to_services()

        tree = {
            "services": self.services,
            "utils": {util: list(self.util_to_services.get(util, [])) for util in self.utils}
        }

        return tree

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Build and display the project dependency tree.")
    parser.add_argument("config_path", type=str, help="Path to the config.json file.")

    args = parser.parse_args()
    builder = ProjectTreeBuilder(args.config_path)

    try:
        tree = builder.build_tree()
        print(json.dumps(tree, indent=2))
    except Exception as e:
        print(f"Error: {e}")
