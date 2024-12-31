from setuptools import setup, find_packages
from setuptools.command.install import install
import platform
import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req_file:
    requirements = [r.strip() for r in req_file if r.strip()]

platform_system = platform.system().lower()
platform_machine = platform.machine().lower()

# Normalize 'arm64' to 'aarch64'
if platform_machine == "arm64":
    platform_machine = "aarch64"

wheel_dir = "wheels"
wheels = {
    ("windows", "amd64"): "fers_calculations-0.1.0-cp312-cp312-win_amd64.whl",
    ("linux", "x86_64"): "fers_calculations-0.1.0-cp312-cp312-manylinux_2_34_x86_64.whl",
    ("darwin", "x86_64"): "fers_calculations-0.1.0-cp312-cp312-macosx_10_12_x86_64.whl",
}

wheel_file = wheels.get((platform_system, platform_machine), "")

data_files = []
if wheel_file:
    # Build absolute path to the wheel, then convert to relative for data_files
    wheel_path_abs = os.path.join(script_dir, wheel_dir, wheel_file)
    if os.path.exists(wheel_path_abs):
        wheel_path_rel = os.path.relpath(wheel_path_abs, start=script_dir).replace("\\", "/")
        data_files.append((wheel_dir, [wheel_path_rel]))


def install_wheel():
    """
    Installs the prebuilt .whl for the detected platform.
    """
    if wheel_file:
        wheel_path_abs = os.path.join(script_dir, wheel_dir, wheel_file)
        print(f"DEBUG: Attempting to install wheel from {wheel_path_abs}")
        if os.path.exists(wheel_path_abs):
            try:
                print(f"DEBUG: Found wheel file: {wheel_path_abs}")
                result = subprocess.run(
                    ["pip", "install", wheel_path_abs], check=True, capture_output=True, text=True
                )
                print("DEBUG: Wheel installation output:")
                print(result.stdout)
                print(result.stderr)
            except subprocess.CalledProcessError as e:
                print("ERROR: Wheel installation failed.")
                print(f"STDOUT:\n{e.stdout}")
                print(f"STDERR:\n{e.stderr}")
                raise RuntimeError("Wheel installation failed.") from e
        else:
            print(f"ERROR: Wheel file does not exist: {wheel_path_abs}")
            raise RuntimeError(
                f"No compatible wheel found for platform {platform_system} on {platform_machine}. "
                "Ensure the correct wheel is included in the package."
            )


class CustomInstallCommand(install):
    """
    A subclass of setuptools 'install' that calls our install_wheel()
    after the normal install steps are done.
    """

    def run(self):
        print("DEBUG: Running custom install command...")
        super().run()
        print("DEBUG: Running wheel installation...")
        install_wheel()
        print("DEBUG: Wheel installation completed.")


setup(
    name="FERS",
    version="0.1.33",
    author="Jeroen Hermsen",
    author_email="j.hermsen@serrac.com",
    description="Finite Element Method library written in Rust with Python interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeroen124/FERS_core",
    packages=find_packages(include=["FERS_core", "FERS_core.*"]),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Rust",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    data_files=data_files,
    cmdclass={
        "install": CustomInstallCommand,
    },
)
