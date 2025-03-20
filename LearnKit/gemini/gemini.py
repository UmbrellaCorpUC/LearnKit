import os
import subprocess
import sys
import time

from .LangSec import get_api_key  # Import the secure API key function

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

import google.generativeai as genai
# Set API key securely using `secure_api.py`
genai.configure(api_key=get_api_key())

# Rate limiting variables
MAX_REQUESTS_PER_MINUTE = 13
request_timestamps = []

# Function to check rate limit
def check_rate_limit():
    global request_timestamps

    # Remove timestamps older than 60 seconds
    current_time = time.time()
    request_timestamps = [t for t in request_timestamps if current_time - t < 60]

    if len(request_timestamps) >= MAX_REQUESTS_PER_MINUTE:
        wait_time = 60 - (current_time - request_timestamps[0])
        print(f"⚠️ Rate limit reached! Waiting {wait_time:.2f} seconds before sending the next request...")
        time.sleep(wait_time)

    request_timestamps.append(time.time())

# Function to generate AI responses
def get_gemini_response(prompt):
    check_rate_limit()  # Ensure request limit isn't exceeded

    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # Default instruction for better responses
    default_instruction = (
    "Be clear, precise, and accurate. Always trace the program execution and explain it step-by-step.\n"
    "Ensure the response is well-structured and properly formatted for readability in CMD/IDLE:\n"
    "- Use appropriate line breaks between sections to avoid clutter.\n"
    "- Use bullet points or numbering for lists where necessary.\n"
    "- Separate important sections using clear headings or dividers.\n"
    "- Do not use excessive indentation or compact formatting that reduces readability.\n"
    "- If code is included, ensure it is properly formatted and clearly marked.\n"
    "- Keep responses concise, avoiding unnecessary repetition.\n"
    )
    
    response = model.generate_content(f"{default_instruction}\n{prompt}")
    
    return response.text if response else "No response received."

def Prompt():
    while True:
        prompt = input("\nEnter your prompt (or type 'exit' to quit): ").strip()
        if prompt.lower() == "exit":
            print("Exiting. Have a great day!")
            break

        print("\nGemini AI Response:\n")
        print(get_gemini_response(prompt))
