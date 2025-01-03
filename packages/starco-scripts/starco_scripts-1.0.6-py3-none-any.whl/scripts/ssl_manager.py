import subprocess
import os

def install_certbot():
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "certbot", "python3-certbot-nginx", "-y"])

def get_ssl_certificate(domain, email, cert_path):
    if not os.path.exists(cert_path):
        os.makedirs(cert_path)
    
    cmd = [
        "certbot", "certonly",
        "--nginx",
        "-d", domain,
        "--email", email,
        "--agree-tos",
        "-n",
        "--cert-path", cert_path
    ]
    
    subprocess.run(cmd)
    
    # Setup auto-renewal
    subprocess.run(["systemctl", "enable", "certbot.timer"])
    subprocess.run(["systemctl", "start", "certbot.timer"])

def main():
    print("\nSSL Certificate Manager")
    print("1. Install Certbot")
    print("2. Get New SSL Certificate")
    print("3. Back to Main Menu")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        install_certbot()
        print("Certbot installed successfully!")
    
    elif choice == "2":
        domain = input("Enter domain name (e.g., example.com): ")
        email = input("Enter email address: ")
        cert_path = input("Enter certificate storage path (e.g., /etc/ssl/certs/): ")
        
        get_ssl_certificate(domain, email, cert_path)
        print(f"SSL certificate obtained for {domain}")
        print("Auto-renewal has been enabled")
    
    elif choice == "3":
        return
    
    else:
        print("Invalid choice!")
