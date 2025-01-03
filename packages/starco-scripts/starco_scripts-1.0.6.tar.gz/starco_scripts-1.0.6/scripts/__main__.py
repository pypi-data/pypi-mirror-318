#!/usr/bin/env python3
from . import linux_service
from . import nginx_config
from . import docker
from . import ssl_manager
import os,sys,subprocess

def run_astro_script():
    cmd = ["bash", "-c", "curl -Ls https://raw.githubusercontent.com/Soroushnk/Astro/main/Astro.sh | bash"]
    subprocess.run(cmd)

def main():
    if os.geteuid() != 0:
        print("This script must be run as root!")
        sys.exit(1)

    while True:
        print("\nUtility Scripts Menu")
        print("1. Linux Service Manager")
        print("2. Nginx Configuration Manager")
        print("3. Docker Manager")
        print("4. Run Astro Script")
        print("5. SSL Certificate Manager")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            linux_service.main()
        elif choice == "2":
            nginx_config.main()
        elif choice == "3":
            docker.main()
        elif choice == "4":
            run_astro_script()
        elif choice == "5":
            ssl_manager.main()
        elif choice == "6":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
