import os
import subprocess
import sys
import webbrowser


# Store in user home for consistency
HOME = os.path.expanduser("~")
TEXT_FOLDER = os.path.join(HOME, ".learnkit_text")
API_KEY_FILE = os.path.join(TEXT_FOLDER, "api_key.enc")
SECRET_KEY_FILE = os.path.join(TEXT_FOLDER, "secret.key")

# Create folder if not exists
os.makedirs(TEXT_FOLDER, exist_ok=True)

def is_module_installed(module_name):
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "show", module_name], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def install_module(module_name):
    if not is_module_installed(module_name):
        print(f"Installing {module_name}...")
        subprocess.run([sys.executable, "-m", "pip", "install", module_name], check=True)
        print(f"{module_name} installed successfully!")

# Ensure cryptography is installed
try:
    from cryptography.fernet import Fernet
except Exception:
    
    install_module("cryptography")

def generate_secret_key():
    secret_key = Fernet.generate_key()
    with open(SECRET_KEY_FILE, "wb") as key_file:
        key_file.write(secret_key)
    return secret_key

def load_secret_key():
    if not os.path.exists(SECRET_KEY_FILE):
        return generate_secret_key()
    with open(SECRET_KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_api_key(api_key):
    cipher = Fernet(load_secret_key())
    with open(API_KEY_FILE, "wb") as file:
        file.write(cipher.encrypt(api_key.encode()))

def decrypt_api_key():
    if not os.path.exists(API_KEY_FILE):
        return None
    cipher = Fernet(load_secret_key())
    with open(API_KEY_FILE, "rb") as file:
        encrypted = file.read()
    return cipher.decrypt(encrypted).decode()

# Cache decrypted API key for the session
_api_key_cache = None

def get_api_key():
    global _api_key_cache
    if _api_key_cache is not None:
        return _api_key_cache

    api_key = decrypt_api_key()

    if api_key is None:
        print("\n⚠️ First-time setup detected.")
        print("🔑 Please obtain your API key from: https://aistudio.google.com/apikey")
        webbrowser.open("https://aistudio.google.com/apikey")

        api_key = input("Enter your API key: ").strip()
        encrypt_api_key(api_key)
        print("✅ API key saved securely!")

    _api_key_cache = api_key
    return api_key
