import subprocess
import sys
import pkg_resources
import os

__all__ = [
    'execute_python_script',
    'get_package_version',
    'install_package',
    'list_packages',
    'run_python_code',
    'uninstall_package'
]

def execute_python_script(script_path):
    """
    Executes a Python script in a separate process.

    Args:
        script_path (str): The path to the Python script to execute.

    Returns:
        str: The output of the script execution.
    """
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"

def get_package_version(package_name):
    """
    Gets the version of an installed Python package.

    Args:
        package_name (str): The name of the package.

    Returns:
        str: The version of the package, or None if the package is not found.
    """
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return None

def install_package(package_name):
    """
    Installs a Python package using pip.

    Args:
        package_name (str): The name of the package to install.
    """
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package_name]
        )
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}: {e}")

def list_packages():
    """
    Lists all installed Python packages.

    Returns:
        list: A list of installed packages.
    """
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(
        [f"{i.key}=={i.version}" for i in installed_packages]
    )
    return installed_packages_list

def run_python_code(code):
    """
    Runs Python code in the current interpreter.

    Args:
        code (str): The Python code to execute.

    Returns:
        str: The output of the code execution.
    """
    try:
        # Redirect stdout and stderr to capture output
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = captured_output = open("temp_output.txt", "w+")
        sys.stderr = captured_error = open("temp_error.txt", "w+")

        # Execute the code
        exec(code)

        # Restore stdout and stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        # Read and return captured output
        captured_output.seek(0)
        output = captured_output.read()
        captured_error.seek(0)
        error = captured_error.read()

        # Clean up temporary files
        captured_output.close()
        captured_error.close()
        os.remove("temp_output.txt")
        os.remove("temp_error.txt")

        if error:
            return f"Error: {error}\nOutput: {output}"
        else:
            return output
    except Exception as e:
        return f"An error occurred: {e}"

def uninstall_package(package_name):
    """
    Uninstalls a Python package using pip.

    Args:
        package_name (str): The name of the package to uninstall.
    """
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "uninstall", "-y", package_name]
        )
        print(f"Successfully uninstalled {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to uninstall {package_name}: {e}")
