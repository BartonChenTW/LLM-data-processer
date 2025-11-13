# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BartonChenTW/LLM-data-processer.git
cd LLM-data-processer
```

### 2. Create Virtual Environment

=== "Windows PowerShell"
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

=== "Windows CMD"
    ```bat
    python -m venv .venv
    .venv\Scripts\activate.bat
    ```

=== "Linux/Mac"
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install Optional Dependencies

#### PyTorch (for local models)

For local model support, install PyTorch:

=== "CPU Only"
    ```bash
    pip install torch --index-url https://download.pytorch.org/whl/cpu
    ```

=== "GPU (CUDA)"
    ```bash
    pip install torch torchvision torchaudio
    ```

#### PDF Processing

PDF support is already included in requirements.txt:

```bash
# Already installed with requirements.txt
pdfplumber>=0.10.0
```

#### LangChain (for advanced document processing)

For document splitting and advanced RAG workflows:

```bash
pip install langchain langchain-community pypdf
```

### 5. Install as Package (Optional)

To install as an editable package:

```bash
pip install -e .
```

## API Key Setup

### Required API Keys

You need at least one of these API keys depending on which provider you use:

#### Hugging Face Token

1. Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Create a new token (read access is sufficient)
3. Set the environment variable:

=== "Windows PowerShell"
    ```powershell
    $env:HF_TOKEN="your_token_here"
    ```

=== "Windows CMD"
    ```bat
    set HF_TOKEN=your_token_here
    ```

=== "Linux/Mac"
    ```bash
    export HF_TOKEN="your_token_here"
    ```

#### Google Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Create an API key
3. Set the environment variable:

=== "Windows PowerShell"
    ```powershell
    $env:GEMINI_API_KEY="your_key_here"
    ```

=== "Windows CMD"
    ```bat
    set GEMINI_API_KEY=your_key_here
    ```

=== "Linux/Mac"
    ```bash
    export GEMINI_API_KEY="your_key_here"
    ```

### Using .env File

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` with your keys:

```ini
HF_TOKEN=your_huggingface_token_here
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Verify Installation

Run this to verify everything is installed correctly:

```python
# Test imports
from llm_helper import AIHelper
import pandas as pd
import transformers

print("✅ All packages installed successfully!")
```

## Troubleshooting

### ModuleNotFoundError: transformers

```bash
pip install transformers torch
```

### PyTorch/TensorFlow Warning

Install PyTorch to suppress the warning:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### API Authentication Errors

Check if your API keys are set:

=== "Windows PowerShell"
    ```powershell
    echo $env:HF_TOKEN
    echo $env:GEMINI_API_KEY
    ```

=== "Linux/Mac"
    ```bash
    echo $HF_TOKEN
    echo $GEMINI_API_KEY
    ```

### Jupyter Kernel Issues

1. Install ipykernel in your venv:
   ```bash
   pip install ipykernel
   ```

2. Add the kernel:
   ```bash
   python -m ipykernel install --user --name=llm-processer
   ```

3. Select the kernel in Jupyter/VS Code

## Next Steps

- Continue to the [Usage Guide](usage.md)
- Check out [Examples](examples.md)
- Read the [API Reference](api-reference.md)
