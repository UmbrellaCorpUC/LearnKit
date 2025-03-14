import os
import base64
import subprocess
import sys

# Function to check if a module is installed
def is_module_installed(module_name):
    try:
        subprocess.run([sys.executable, "-m", "pip", "show", module_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Install the module only if it's not installed
def install_module(module_name):
    if not is_module_installed(module_name):
        print(f"Installing {module_name}...")  # Print message before installing
        subprocess.run([sys.executable, "-m", "pip", "install", module_name], check=True)
        print(f"{module_name} installed successfully!")

# Ensure `cryptography` is installed
install_module("cryptography")

# Now that cryptography is installed, import it
from cryptography.fernet import Fernet

# Define file paths
TEXT_FOLDER = "text"
API_KEY_FILE = os.path.join(TEXT_FOLDER, "api_key.enc")
SECRET_KEY_FILE = os.path.join(TEXT_FOLDER, "secret.key")

# Ensure text folder exists
if not os.path.exists(TEXT_FOLDER):
    os.makedirs(TEXT_FOLDER)

def generate_secret_key():
    """Generates a secret key for encryption and stores it securely."""
    if not os.path.exists(TEXT_FOLDER):
        os.makedirs(TEXT_FOLDER)  # ✅ Ensure the folder exists before writing

    secret_key = Fernet.generate_key()
    with open(SECRET_KEY_FILE, "wb") as key_file:
        key_file.write(secret_key)
    return secret_key

def load_secret_key():
    """Loads the secret key, or generates a new one if not found."""
    if not os.path.exists(SECRET_KEY_FILE):
        return generate_secret_key()
    with open(SECRET_KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_api_key(api_key):
    """Encrypts the API key using the secret key and saves it."""
    secret_key = load_secret_key()
    cipher = Fernet(secret_key)
    encrypted_key = cipher.encrypt(api_key.encode())

    with open(API_KEY_FILE, "wb") as file:
        file.write(encrypted_key)

def decrypt_api_key():
    """Decrypts and returns the stored API key."""
    if not os.path.exists(API_KEY_FILE):
        return None
    
    secret_key = load_secret_key()
    cipher = Fernet(secret_key)

    with open(API_KEY_FILE, "rb") as file:
        encrypted_key = file.read()

    return cipher.decrypt(encrypted_key).decode()

def get_api_key():
    """Checks if the API key exists; if not, prompts the user to enter it."""
    api_key = decrypt_api_key()
    
    if api_key is None:
        print("\n⚠️ It looks like you're running this script for the first time.")
        print("🔑 Please get your API key from: https://aistudio.google.com/apikey")
        api_key = input("Enter your API key: ").strip()
        
        encrypt_api_key(api_key)
        print("✅ API key saved securely!")

    return api_key
