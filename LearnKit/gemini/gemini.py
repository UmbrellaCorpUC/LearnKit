import os
import subprocess
import sys
import time

from .LangSec import get_api_key  # Adjust path as needed

# --- Module Installer ---
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
    python_exe = sys.executable

    # If pythonw.exe is used (common in GUI apps), switch to python.exe
    if python_exe.endswith("pythonw.exe"):
        python_exe = python_exe.replace("pythonw.exe", "python.exe")

    if not is_module_installed(module_name):
        print(f"📦 Installing {module_name} using {python_exe}...")
        try:
            subprocess.run([python_exe, "-m", "pip", "install", module_name], check=True)
            print(f"✅ {module_name} installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {module_name}. Error:\n{e}")
            sys.exit(1)

# --- Install google-generativeai ---
install_module("google-generativeai")

import google.generativeai as genai
genai.configure(api_key=get_api_key())

# --- Rate Limiting ---
MAX_REQUESTS_PER_MINUTE = 13
request_timestamps = []

def check_rate_limit():
    global request_timestamps
    now = time.time()
    request_timestamps = [t for t in request_timestamps if now - t < 60]

    if len(request_timestamps) >= MAX_REQUESTS_PER_MINUTE:
        wait_time = 60 - (now - request_timestamps[0])
        print(f"⚠️ Rate limit reached. Waiting {wait_time:.2f} seconds...")
        time.sleep(wait_time)

    request_timestamps.append(now)

# --- AI Response Handler ---
def get_gemini_response(prompt):
    check_rate_limit()

    model = genai.GenerativeModel("gemini-2.0-flash")

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

    return response.text if response else "⚠️ No response received."

# --- Prompt Loop ---
def Prompt():
    while True:
        prompt = input("\n🔹 Enter your prompt (or type 'exit' to quit): ").strip()
        if prompt.lower() == "exit":
            print("👋 Exiting. Have a great day!")
            break

        print("\n🧠 Gemini AI Response:\n")
        print(get_gemini_response(prompt))
