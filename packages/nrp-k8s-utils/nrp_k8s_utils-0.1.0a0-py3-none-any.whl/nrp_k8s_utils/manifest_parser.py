import yaml
import os
from typing import Tuple, List, Dict


class K8SManifestParser:
    def __init__(self, manifest_file):
        with open(manifest_file, 'r') as file:
            self.manifest = yaml.safe_load(file)
        self.manifest_file = manifest_file

    def get_pod_details(self) -> Tuple[str, str]:
        """Returns details about the pod such as name and namespace."""
        metadata = self.manifest.get('metadata', {})
        return metadata.get('name'), metadata.get('namespace', 'default')
        
    def get_containers(self):
        """Returns a list of containers in the pod."""
        spec = self.manifest.get('spec', {})
        return spec.get('containers', [])

    def get_resources(self):
        """Returns the resource requests and limits for each container."""
        containers = self.get_containers()
        resources = {}
        for container in containers:
            resources[container['name']] = container.get('resources', {})
        return resources
    
    def get_volumes(self) -> List[Dict]:
        """Returns a list of volumes in the pod."""
        spec = self.manifest.get('spec', {})
        return spec.get('volumes', [])  

    def add_container(self, container_spec: Dict):
        """Adds a new container to the pod."""
        if 'spec' not in self.manifest:
            self.manifest['spec'] = {}
        if 'containers' not in self.manifest['spec']:
            self.manifest['spec']['containers'] = []
        self.manifest['spec']['containers'].append(container_spec)

    def remove_container(self, container_name):
        """Removes a container by name."""
        containers = self.get_containers()
        updated_containers = [c for c in containers if c['name'] != container_name]
        if 'spec' in self.manifest:
            self.manifest['spec']['containers'] = updated_containers

    def modify_container(self, container_name, updates):
        """Modifies an existing container."""
        containers = self.get_containers()
        for container in containers:
            if container['name'] == container_name:
                container.update(updates)
                break

    def save_manifest(self, output_file=None) -> str:
            """
            Saves the updated manifest to a file. By default, the file will be saved in the same
            directory as the original manifest with a "_updated" suffix.
            """
            if output_file is None:
                base, ext = os.path.splitext(self.manifest_file)
                output_file = f"{base}_rsync{ext}"

            with open(output_file, 'w') as file:
                yaml.safe_dump(self.manifest, file)

            return output_file

    def clone_manifest(self, output_file=None):
        """
        Creates a copy of the manifest file. By default, the copy will be saved in the same
        directory as the original manifest with a "_copy" suffix.
        """
        if output_file is None:
            base, ext = os.path.splitext(self.manifest_file)
            output_file = f"{base}_copy{ext}"

        with open(output_file, 'w') as file:
            yaml.safe_dump(self.manifest, file)
