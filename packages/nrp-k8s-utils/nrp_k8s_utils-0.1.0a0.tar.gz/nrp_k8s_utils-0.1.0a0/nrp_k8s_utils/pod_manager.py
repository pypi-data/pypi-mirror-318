import shutil
import yaml
import logging
import time
import subprocess
import json
import tempfile
import os
from typing import Dict, List, Any, Union, Optional

class PodManager:

    def __init__(self, manifest: Union[str, Dict], context:Optional[str] = None, debug_mode: bool = False): 
        """
        Initialize the PodManager with the path to the Kubernetes manifest file and optional kubeconfig file.

        :param manifest_path: Path to the Kubernetes manifest YAML file.
        :param self.logger_level: self.logger level for the PodManager instance. Default is INFO.
        """    

        self.debug_mode = debug_mode
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)

        self._parse_manifest(manifest)

        self.name = self._manifest.get("metadata", {}).get("name", "Unknown")
        self.containers = self._manifest.get("spec", {}).get("containers", [])
        self.volumes = self._manifest.get("spec", {}).get("volumes", [])

        self._get_kubectl_path()

        if context and not isinstance(context, str):
            raise ValueError("Context must be a string")
        
        if context and isinstance(context, str):
            self.context = context
            self.logger.debug(f"Using provided context: {context}")
        else:
            self.context = self.get_current_context(verbose=False)
            self.logger.debug(f"Using current context: {self.context}")

        self.namespace = self.get_current_namespace(verbose=False)

    def _parse_manifest(self, manifest: Union[str, Dict]):
        if isinstance(manifest, str):
            self._manifest_path = manifest
            try:
                with open(self._manifest_path, 'r') as file:
                    self._manifest: Dict[str, Any] = yaml.safe_load(file)
            except FileNotFoundError:
                raise ValueError(f"Manifest file not found: {manifest}")
            except yaml.YAMLError as e:
                raise ValueError(f"Error parsing manifest file: {e}")
            try:
                with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yml") as temp_file:
                    yaml.dump(self._manifest, temp_file)
                    self._manifest_path = temp_file.name
            except yaml.YAMLError as e:
                raise ValueError(f"Error serializing the manifest to YAML: {e}")
        elif isinstance(manifest, Dict):
            self._manifest = manifest
            try:
                with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yml") as temp_file:
                    yaml.dump(self._manifest, temp_file)
                    self._manifest_path = temp_file.name
            except yaml.YAMLError as e:
                raise ValueError(f"Error serializing the manifest to YAML: {e}")
        else:
            raise ValueError("Manifest must be a file path or a dictionary")
        
    def _get_kubectl_path(self):
        """Get the path to the kubectl binary."""
        kubectl_path = os.getenv("KUBECTL_PATH", shutil.which("kubectl"))
        if not kubectl_path:
            raise FileNotFoundError(
                "The `kubectl` command is not found. Install it or set the KUBECTL_PATH environment variable."
            )
        self.kubectl_path = kubectl_path
        
# --------------------------------------------------------------------------------
# Pod Lifecycle Methods
# --------------------------------------------------------------------------------

    def _start_pod(self):
        """
        Start a pod using the provided Kubernetes manifest and wait until it is running.
        """
        self.logger.info("Starting pod")
        # Apply or create the manifest
        cmd = ["apply", "-f", self._manifest_path]
        self.run_kubectl_cmd(cmd, check=True, verbose=False)

    def start_pod(self) -> bool:
        """
        Start a pod using the provided Kubernetes manifest and wait until it is running.
        """
        self.logger.info("Starting pod")
        # Apply or create the manifest
        cmd = ["apply", "-f", self._manifest_path]
        self.run_kubectl_cmd(cmd, check=True, verbose=True)

        # Wait until the pod is in Running state
        start_time = time.time()
        timeout = 300
        while time.time() - start_time < timeout:
            status = self.get_pod_status(verbose=False)
            if status == "Running":
                self.logger.info(f"Pod {self.name} is running")
                return True
            self.logger.debug(f"Waiting for pod {self.name}, current status: {status}")
            time.sleep(1)
        raise TimeoutError(f"Timed out waiting for pod {self.name} to be running.")

    def stop_pod(self):
        """
        Stop a pod defined in the Kubernetes manifest.
        """
        self.logger.info("Stopping pod")
        cmd = ["delete", "pod", self.name, "-n", self.namespace]
        self.run_kubectl_cmd(cmd, check=False) 


# --------------------------------------------------------------------------------
# Public Methods
# --------------------------------------------------------------------------------


    def get_current_namespace(self, verbose:bool=True) -> str:
        """
        Retrieve the namespace defined in the current kubectl context.
        If no namespace is defined, return 'default'.

        :return: The namespace defined in the current context or 'default'.
        """
        try:
            cmd = ["config", "view", "--minify", "--output", "jsonpath={..namespace}"]
            result = self.run_kubectl_cmd(cmd, check=True, verbose=verbose)
            namespace = result.stdout.strip()
            if namespace:
                self.logger.debug(f"Current namespace: {namespace}")
                return namespace
            else:
                self.logger.debug("No namespace defined in the current context. Using 'default'.")
                self.logger.info(f"Current namespace: default")
                return "default"
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error retrieving current namespace: {e.stderr.strip()}")
            raise RuntimeError(f"Failed to retrieve current namespace: {e.stderr.strip()}")

    def get_current_context(self, verbose:bool=True) -> str:
        """
        Retrieve the current kubectl context as selected in the terminal.

        :return: The name of the currently active kubectl context.
        """
        try:
            cmd = ["kubectl", "config", "current-context"]
            result = self.run_subprocess_cmd(cmd, check=True, verbose=verbose)
            context = result.stdout.strip()
            self.logger.debug(f"Current context: {context}")
            return context
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error retrieving current kubectl context: {e.stderr.strip()}")
            raise RuntimeError(f"Failed to retrieve current kubectl context: {e.stderr.strip()}")
    
    def print_logs(self, container_name: str = None):
        """
        Print logs from a specified pod (and optionally container).
        """
        cmd = ["logs", self.name, "-n", self.namespace]
        if container_name:
            cmd.extend(["-c", container_name])

        result = self.run_kubectl_cmd(cmd, check=False)
        if result.returncode != 0:
            self.logger.error(f"Failed to get logs: {result.stderr}")
            raise RuntimeError(result.stderr)

        self.logger.info(result.stdout)
        return result.stdout

    def describe_pod(self):
        """
        Describe the pod defined in the Kubernetes manifest.
        """
        cmd = ["describe", "pod", self.name, "-n", self.namespace]
        result = self.run_kubectl_cmd(cmd, check=False)

        self.logger.info(result.stdout)
        return result.stdout

    def get_pod_status(self, verbose:bool = True) -> str:
        """
        Get the status of the pod defined in the Kubernetes manifest.
        """
        cmd = [
            "get", "pod", self.name, "-n", self.namespace, "-o", "json"
        ]
        result = self.run_kubectl_cmd(cmd, check=False, verbose=verbose)
        if result.returncode != 0:
            self.logger.error(f"Failed to get pod status: {result.stderr}")
            raise RuntimeError(result.stderr)
        try:
            pod_info = json.loads(result.stdout)
            status = pod_info.get("status", {}).get("phase", "Unknown")
            self.logger.debug(f"Pod status: {status}")
            return status
        except json.JSONDecodeError as e:
            self.logger.error(f"Error parsing JSON output: {e}")
            raise RuntimeError("Failed to parse pod status JSON")
    
    def run_container_cmd(self, command: Union[str, List], container_name: str = None, verbose: bool = True) -> str:
        """
        Run a command inside a pod using kubectl exec.
        :param command: Command to run as a list of arguments.
        :param container_name: (Optional) Name of the container in which to run the command.
        :return: Output of the command.
        """

        if isinstance(command, str):
            command = command.split

        cmd = [
            "exec", self.name, "--"
        ]
        if container_name:
            cmd.insert(cmd.index("exec") + 1, f"-c={container_name}")
        cmd.extend(command)

        if verbose:
            self.logger.info(f"Running command: {' '.join(cmd)}")

        result = self.run_kubectl_cmd(cmd, check=True, verbose=verbose)

        return result.stdout
    
    def run_kubectl_cmd(self, command: Union[str, List], check: bool = True, verbose: bool = True) -> subprocess.CompletedProcess:
        """
        Run a kubectl command using subprocess.run.

        :param command: Command to run as a list of arguments.
        :param check: If True, raise an exception if the command fails.
        :param verbose: If True, print the output of the command.
        :return: CompletedProcess object containing the result of the command.
        """
        if isinstance(command, str):
            command = command.split()
        cmd = ["kubectl", "--context", self.context]
        cmd.extend(command)

        result = self.run_subprocess_cmd(cmd, check=check, verbose=verbose)

        return result
    
    def run_subprocess_cmd(self, cmd: Union[str, List], check: bool = True, verbose: bool = True) -> subprocess.CompletedProcess:
        """
        Run a subprocess command using subprocess.run.
        :param cmd: Command to run as a list of arguments.
        :param check: If True, raise an exception if the command fails.
        :param verbose: If True, print the output of the command.
        """
        if not isinstance(cmd, list) or not all(isinstance(arg, str) for arg in cmd):
            raise ValueError(f"Invalid command: {cmd}. It must be a list of strings.")

        self.logger.debug(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if check and result.returncode != 0:
            self.logger.error(f"Command failed: {result.stderr}")
            raise RuntimeError(f"Command failed: {result.stderr}")
        if verbose:
            self.logger.info(result.stdout)
        return result
        
    def kubectl_copy(self, container_name: str, src_path: str, dest_path: str, verbose:bool = True) -> bool:
        """
        Kubectl CP a file from the local filesystem to a directory in a container.

        :param container_name: Name of the container.
        :param src_path: Path to the source file on the local filesystem.
        :param dest_path: Path to the destination directory in the container.
        :return: True if the file was copied successfully, False otherwise.
        """
        cmd = [
            "cp", src_path, f"{self.namespace}/{self.name}:{dest_path}", "-c", container_name
        ]

        if verbose:
            self.logger.info(f"Copying file {src_path} to {self.name}:{dest_path} in {container_name}")

        result = self.run_kubectl_cmd(cmd, check=True, verbose=verbose)
        if result.returncode == 0:
            self.logger.debug(f"File {src_path} copied to {self.name}:{dest_path} in container {container_name}")
            return True
        else:
            self.logger.error(f"Error copying file to container: {result.stderr}")
            return False


# --------------------------------------------------------------------------------
# Manifest Methods
# --------------------------------------------------------------------------------


    def add_container(self, container: Dict):
        """
        Add a container to the pod manifest.

        :param container: Dictionary containing the container definition.
        """
        # Check if container is valid
        if not container.get("name"):
            raise ValueError("Container must have a name")
        if not container.get("image"):
            raise ValueError("Container must have an image")
        
        for c in self.containers:
            if c["name"] == container["name"]:
                raise ValueError(f"Container with name {container['name']} already exists")

        self.containers.append(container)
        self._manifest["spec"]["containers"] = self.containers
        try:
            with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yml") as temp_file:
                yaml.dump(self._manifest, temp_file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error serializing the manifest to YAML: {e}")
        os.remove(self._manifest_path)
        self._manifest_path = temp_file.name

    def add_volume(self, volume: Dict):
        """
        Add a volume to the pod manifest.

        :param volume: Dictionary containing the volume definition.
        """

        # Check if volume is valid
        if not volume.get("name"):
            raise ValueError("Volume must have a name")

        for v in self.volumes:
            if v["name"] == volume["name"]:
                raise ValueError(f"Volume with name {volume['name']} already exists")

        self.volumes.append(volume)
        self._manifest["spec"]["volumes"] = self.volumes
        try:
            with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yml") as temp_file:
                yaml.dump(self._manifest, temp_file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error serializing the manifest to YAML: {e}")
        os.remove(self._manifest_path)
        self._manifest_path = temp_file.name

    def remove_container(self, container_name: str):
        """
        Remove a container from the pod manifest.

        :param container_name: Name of the container to remove.
        """
        for c in self.containers:
            if c["name"] == container_name:
                self.containers.remove(c)
                break
        else:
            raise ValueError(f"Container with name {container_name} not found")
        
        self._manifest["spec"]["containers"] = self.containers
        try:
            with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yml") as temp_file:
                yaml.dump(self._manifest, temp_file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error serializing the manifest to YAML: {e}")
        os.remove(self._manifest_path)
        self._manifest_path = temp_file.name
    
    def remove_volume(self, volume_name: str):
        """
        Remove a volume from the pod manifest.

        :param volume_name: Name of the volume to remove.
        """
        for v in self.volumes:
            if v["name"] == volume_name:
                self.volumes.remove(v)
                break
        else:
            raise ValueError(f"Volume with name {volume_name} not found")
        
        self._manifest["spec"]["volumes"] = self.volumes
        try:
            with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yml") as temp_file:
                yaml.dump(self._manifest, temp_file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error serializing the manifest to YAML: {e}")
        os.remove(self._manifest_path)
        self._manifest_path = temp_file.name

    def overwrite_manifest (self, manifest: Dict):
        """
        Replace the current manifest with a new one.

        :param manifest: Dictionary containing the new manifest.
        """
        self._manifest = manifest
        try:
            with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yml") as temp_file:
                yaml.dump(self._manifest, temp_file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error serializing the manifest to YAML: {e}")
        os.remove(self._manifest_path)
        self._manifest_path = temp_file.name
