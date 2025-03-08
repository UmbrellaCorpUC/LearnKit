import os
import subprocess
import sys
import warnings

def install_package(package):
    """Automatically installs the given Python package if not installed."""
    try:
        __import__(package)
        print(f"✅ {package} is already installed.")
    except ImportError:
        print(f"📦 Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} installed successfully!")

# Install ctransformers if not present
install_package("ctransformers")

# Import the installed library
try:
    from ctransformers import AutoModelForCausalLM
    print("🎉 ctransformers is successfully installed and imported!")
except ImportError:
    print("❌ Error: ctransformers installation failed.")
    sys.exit(1)  # Exit if the library fails to install

# Suppress warnings
warnings.simplefilter("ignore")
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Set Hugging Face cache directory
HF_CACHE_DIR = "F:/lang/"
os.environ["HF_HOME"] = HF_CACHE_DIR
print(f"HF_HOME: {os.environ['HF_HOME']}")

# ✅ Correct GGUF model path
MODEL_PATH = "F:/lang/mistral-7b-code-16k-qlora.Q4_K_M.gguf"

try:
    # ✅ Load the model
    llm = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        model_type="llama",  # ✅ Correct model type
        gpu_layers=0,  # ✅ Set GPU layers to 0 for CPU mode
    )

    print("✅ Model Loaded Successfully!")

    while True:
        # ✅ Get user input
        user_prompt = input("\nEnter your instruction (or type 'exit' to quit): ").strip()
        if user_prompt.lower() == "exit":
            print("🚀 Exiting the program. Have a great day!")
            break

        # ✅ Create an improved prompt
        default_instruction = """DO WHAT IS ASKED"""

        prompt = f"""### Instruction:
{default_instruction}

### User Request:
{user_prompt}

### Response:
"""
        # ✅ Generate response
        response = llm(
            prompt,
            temperature=0.3,
            top_k=40,
            top_p=0.9,
            max_new_tokens=500,
            stop=["\n\n", "### Instruction"],
        )

        response_text = response if isinstance(response, str) else response.get("text", "")

        # ✅ Generate explanation
        explanation_prompt = f"### Instruction:\nExplain the following Python code:\n```python\n{response_text}\n```\n\n### Response:\n"
        explanation = llm(
            explanation_prompt,
            temperature=0.3,
            top_k=40,
            top_p=0.9,
            max_new_tokens=500,
            stop=["\n\n", "### Instruction"],
        )

        explanation_text = explanation if isinstance(explanation, str) else explanation.get("text", "")

        # ✅ Generate execution trace
        trace_prompt = f"### Instruction:\nProvide a step-by-step execution trace for the following Python code:\n```python\n{response_text}\n```\n\n### Response:\n"
        trace = llm(
            trace_prompt,
            temperature=0.3,
            top_k=40,
            top_p=0.9,
            max_new_tokens=500,
            stop=["\n\n", "### Instruction"],
        )

        trace_text = trace if isinstance(trace, str) else trace.get("text", "")

        # ✅ Print the generated response, explanation, and trace
        print("\n🔹 **Generated Code:**\n", response_text)
        print("\n📝 **Explanation:**\n", explanation_text)
        print("\n🛠 **Execution Trace:**\n", trace_text)

except Exception as e:
    print(f"❌ Error: {e}")
