import os
import subprocess
import sys
import google.generativeai as genai
from crypt import get_api_key  # Import the secure API key function

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
        print(f"Installing {module_name}...")
        subprocess.run([sys.executable, "-m", "pip", "install", module_name], check=True)
        print(f"{module_name} installed successfully!")

# Ensure `google-generativeai` is installed
install_module("google-generativeai")

# Set API key securely using `secure_api.py`
genai.configure(api_key=get_api_key())

# Function to generate AI responses
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # Default instruction for better responses
    default_instruction = (
        "Be clear, precise, and accurate. Always trace the program execution and explain it step-by-step."
    )
    
    response = model.generate_content(f"{default_instruction}\n{prompt}")
    
    return response.text if response else "No response received."

# Main loop for continuous prompting
if __name__ == "__main__":
    while True:
        prompt = input("\nEnter your prompt (or type 'exit' to quit): ").strip()
        if prompt.lower() == "exit":
            print("Exiting. Have a great day!")
            break

        print("\nGemini AI Response:\n")
        print(get_gemini_response(prompt))
