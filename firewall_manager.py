import platform
import subprocess

def firewall_management_linux():
    subprocess.run(["./firewall_manager.sh"])

def firewall_management_windows():
    subprocess.run(["powershell.exe", "-File", "firewall_manager.ps1"])

def firewall_manager():
    os_type = platform.system()
    if os_type == "Linux":
        try:
            print("The operating system is Linux.")
            firewall_management_linux()
        except Exception as e:
            print(f"Error occurred while managing firewall on Linux: {e}")
    elif os_type == "Windows":
        try:
            print("The operating system is Windows.")
            firewall_management_windows()
        except Exception as e:
            print(f"Error occurred while managing firewall on Windows: {e}")
    else:
        raise NotImplementedError(f"Firewall management not implemented for OS: {os_type}")
    
if __name__ == "__main__":
    firewall_manager()