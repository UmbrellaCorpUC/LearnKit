import os
import subprocess
import sys
import webbrowser
from cryptography.fernet import Fernet

# Define file paths
TEXT_FOLDER = "text"
API_KEY_FILE = os.path.join(TEXT_FOLDER, "api_key.enc")
SECRET_KEY_FILE = os.path.join(TEXT_FOLDER, "secret.key")

# Ensure text folder exists
os.makedirs(TEXT_FOLDER, exist_ok=True)

def is_module_installed(module_name):
    """Checks if a module is installed."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "show", module_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_module(module_name):
    """Installs the module if not already installed."""
    if not is_module_installed(module_name):
        print(f"Installing {module_name}...")
        subprocess.run([sys.executable, "-m", "pip", "install", module_name], check=True)
        print(f"{module_name} installed successfully!")

# Ensure `cryptography` is installed
install_module("cryptography")

def generate_secret_key():
    """Generates and saves a secret key for encryption."""
    secret_key = Fernet.generate_key()
    with open(SECRET_KEY_FILE, "wb") as key_file:
        key_file.write(secret_key)
    return secret_key

def load_secret_key():
    """Loads the existing secret key or generates a new one."""
    return generate_secret_key() if not os.path.exists(SECRET_KEY_FILE) else open(SECRET_KEY_FILE, "rb").read()

def encrypt_api_key(api_key):
    """Encrypts and saves the API key securely."""
    cipher = Fernet(load_secret_key())
    with open(API_KEY_FILE, "wb") as file:
        file.write(cipher.encrypt(api_key.encode()))

def decrypt_api_key():
    """Decrypts and returns the stored API key."""
    if not os.path.exists(API_KEY_FILE):
        return None
    cipher = Fernet(load_secret_key())
    return cipher.decrypt(open(API_KEY_FILE, "rb").read()).decode()

def get_api_key():
    """Retrieves the API key, prompting the user if needed."""
    api_key = decrypt_api_key()

    if api_key is None:
        print("\n⚠️ First-time setup detected.")
        print("🔑 Please obtain your API key from: https://aistudio.google.com/apikey")
        
        # Open the API key URL automatically
        webbrowser.open("https://aistudio.google.com/apikey")

        api_key = input("Enter your API key: ").strip()
        encrypt_api_key(api_key)
        print("✅ API key saved securely!")

    return api_key
