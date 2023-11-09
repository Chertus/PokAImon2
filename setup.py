# setup.py
import subprocess
import os
import sys

from data_manager import save_log

def check_prerequisites():
    with open('requirements.txt') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

    for req in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", req])
            save_log(f"Installed {req}")
        except subprocess.CalledProcessError:
            save_log(f"Failed to install {req}")

# Example usage
check_prerequisites()
