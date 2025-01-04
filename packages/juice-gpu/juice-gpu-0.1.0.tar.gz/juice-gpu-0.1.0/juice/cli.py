import json
import os
import sys
import subprocess
from shutil import which

ext = '.exe' if os.name == 'nt' else ''

def verify_juice_executable():
    """Check if juice.exe is available on the system PATH"""
    juice_path = which(f'juice{ext}')
    if not juice_path:
        print(f"Error: juice{ext} not found on PATH")
        print(f"Please ensure juice{ext} is installed and available in your system PATH")
        sys.exit(1)
    return juice_path

def start_session(pid):
    juice_path = verify_juice_executable()

    process = subprocess.run(f"{juice_path} session request --quiet --dump-config --watch-pid {pid}", shell=True, capture_output=True, text=True)
    if process.returncode == 0:
        os.environ['JUICE_CONFIGURATION'] = process.stdout.strip()
        verify_juda_library(juice_path)
    else:
        print("Failed to start session")
        sys.exit(1)

def verify_juda_library(juice_path):
    """Check if the Juda library exists alongside the juice executable and load it"""
    juice_dir = os.path.dirname(juice_path)
    
    if os.name == 'nt':
        lib_name = 'RemoteGPUShim64.dll'
    else:
        lib_name = 'libRemoteGPUCuda.so'
    
    lib_path = os.path.join(juice_dir, lib_name)
    if os.path.exists(lib_path):
        try:
            from ctypes import cdll
            dll = cdll.LoadLibrary(lib_path)
            if dll:
                result = dll.JuiceInitialize()
                if result == 0:
                    print("Juice library loaded successfully")
                    return
                else:
                    print(f"Error initializing Juice library: {result}")
                    sys.exit(1)
        except Exception as e:
            print(f"Error loading {lib_name}: {str(e)}")
            sys.exit(1)
    
    print(f"Error: {lib_name} not found at {lib_path}")
    print("Please ensure the Juice library is properly installed alongside the juice executable")
    sys.exit(1)
