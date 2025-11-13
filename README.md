# LLM Data Processer

A Python library for seamlessly working with Large Language Models (LLMs) from multiple providers. Easily integrate Hugging Face models, Google Gemini, OpenAI, and more with a unified interface. Perfect for data analysis, chat applications, and AI-powered workflows.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-online-brightgreen.svg)](https://bartonchentw.github.io/LLM-data-processer/)

📖 **[Documentation](https://bartonchentw.github.io/LLM-data-processer/)** | 🚀 **[Quick Start](#quick-start)** | 📚 **[Examples](#usage-examples)**

## ✨ Features

- 🤖 **Multi-Provider Support**: Hugging Face Inference API, Google Gemini 2.5, OpenAI (extensible)
- 💬 **Interactive Chat Widget**: Built-in Jupyter notebook UI for chat interactions
- 📊 **Data Integration**: Attach pandas DataFrames and query your data with LLMs
- 📄 **PDF Processing**: Built-in utility to extract and analyze PDF documents
- 📝 **Guideline System**: Add custom guidelines to steer model behavior
- 🎨 **History Management**: Automatic conversation history tracking
- 🔧 **Easy Configuration**: Simple initialization with sensible defaults
- 📦 **Pip Installable**: Install as a package or use directly

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

## 🚀 Installation

### Option 1: Install from Source (Recommended for Development)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BartonChenTW/LLM-data-processer.git
   cd LLM-data-processer
   ```

2. **Create and activate a virtual environment:**
   
   **Windows PowerShell:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   
   **Windows CMD:**
   ```bat
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```
   
   **Linux/Mac:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Install PyTorch (for local transformers models):**
   ```bash
   # CPU only (lightweight)
   pip install torch --index-url https://download.pytorch.org/whl/cpu
   
   # OR with CUDA GPU support
   pip install torch
   ```

### Option 2: Install as Package

```bash
pip install -e .
```

## ⚙️ Configuration

### Set up API Keys

Create a `.env` file or set environment variables:

```bash
# For Hugging Face models
export HF_TOKEN="your_huggingface_token_here"

# For Google Gemini
export GEMINI_API_KEY="your_gemini_api_key_here"

# For OpenAI (if using)
export OPENAI_API_KEY="your_openai_api_key_here"
```

**Get API Keys:**
- Hugging Face: https://huggingface.co/settings/tokens
- Google Gemini: https://aistudio.google.com/app/apikey
- OpenAI: https://platform.openai.com/api-keys

## 🎯 Quick Start

### Basic Usage with Hugging Face

```python
from llm_helper import AIHelper

# Initialize with Llama or Mistral
ai = AIHelper(model_name='Llama-3.1')

# Simple question
response = ai.ask("What is machine learning?")
print(response)
```

### Using Google Gemini

```python
from llm_helper.ai_helper import AIHelper_Google

# Initialize Gemini with Google Search
ai = AIHelper_Google()

# Ask with web grounding
response = ai.ask("What are the latest AI trends in 2025?")
print(response)
```

### Interactive Chat in Jupyter

```python
from llm_helper import AIHelper

ai = AIHelper(model_name='Llama-3.1')

# Launch interactive widget
ai.chat_widget()
```

## 📚 Usage Examples

### Example 1: Data Analysis with DataFrames

```python
import pandas as pd
from llm_helper import AIHelper

# Create AI helper
ai = AIHelper(model_name='Llama-3.1')

# Load your data
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
})

# Attach data to AI context
ai.attach_data(df)

# Query your data
ai.ask("Who has the highest salary?")
ai.ask("What is the average age?")
```

### Example 2: Custom Guidelines

```python
ai = AIHelper(model_name='Llama-3.1')

# Add behavior guidelines
ai.add_guideline("Always respond in bullet points")
ai.add_guideline("Keep responses under 100 words")
ai.add_guideline("Focus on practical actionable advice")

# Ask with guidelines applied
ai.ask("How do I learn Python?", with_guideline=True)
```

### Example 3: Conversation History

```python
ai = AIHelper(model_name='Llama-3.1')

# Have a conversation
ai.ask("What is Python?")
ai.ask("What are its main uses?")  # Builds on previous context
ai.ask("Compare it to JavaScript")  # Maintains conversation flow

# View history
print(ai.chat_history)
```

## 📖 API Documentation

### AIHelper (Hugging Face)

```python
AIHelper(
    model_name: str = 'Mistral-7B',
    display_response: bool = True
)
```

**Available Models:**
- `'Llama-3.1'` - Meta Llama 3.1 8B Instruct
- `'Mistral-7B'` - Mistral 7B Instruct v0.2

**Methods:**

#### `ask()`
```python
ask(
    prompt: str,
    display_response: bool = None,
    with_guideline: bool = True,
    with_data: bool = True,
    with_history: bool = True
) -> str
```
Generate a response from the LLM.

**Parameters:**
- `prompt`: Your question or instruction
- `display_response`: Whether to display output (default: True)
- `with_guideline`: Include custom guidelines in context
- `with_data`: Include attached data in context
- `with_history`: Include conversation history

#### `add_guideline()`
```python
add_guideline(guideline: str)
```
Add a custom guideline to influence model behavior.

#### `attach_data()`
```python
attach_data(data: pd.DataFrame)
```
Attach a pandas DataFrame to the AI context for querying.

#### `chat_widget()`
```python
chat_widget()
```
Launch an interactive chat interface in Jupyter notebooks.

### AIHelper_Google (Google Gemini)

```python
AIHelper_Google(
    model: str = 'gemini-2.5-flash',
    display_response: bool = True
)
```

**Methods:**

#### `ask()`
```python
ask(
    prompt: str,
    display_response: bool = None
) -> str
```
Generate a response using Google Gemini with Google Search grounding.

## 🛠️ Advanced Configuration

### Custom Temperature & Max Tokens

Edit `llm_helper/ai_helper.py`:

```python
config = {
    'max_tokens': 2000,    # Adjust response length
    'temperature': 0.7,     # 0.0 = deterministic, 1.0 = creative
}
```

### Add New Models

```python
llm_models = {
    'Llama-3.1': 'meta-llama/Llama-3.1-8B-Instruct',
    'Mistral-7B': 'mistralai/Mistral-7B-Instruct-v0.2',
    'YourModel': 'your-org/your-model-name'  # Add custom model
}
```

## 📂 Project Structure

```
LLM-data-processer/
├── llm_helper/
│   ├── __init__.py          # Package initialization
│   └── ai_helper.py         # Core AI helper classes
├── notebook/
│   └── llm_chat.ipynb       # Example chat notebook
├── examples/
│   ├── basic_usage.py       # Simple examples
│   ├── data_analysis.py     # DataFrame integration
│   └── custom_guidelines.py # Guideline examples
├── .env.example             # API key template
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── setup.py                 # Package installation
├── CHANGELOG.md             # Version history
├── CONTRIBUTING.md          # Contribution guide
├── LICENSE                  # MIT License
└── README.md                # This file
```

## 🐛 Troubleshooting

### ModuleNotFoundError: transformers
```bash
pip install transformers torch
```

### PyTorch/TensorFlow Warning
Install PyTorch for local model support:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### API Authentication Errors
Ensure your API keys are set:
```bash
echo $HF_TOKEN        # Should show your token
echo $GEMINI_API_KEY  # Should show your key
```

### Notebook Kernel Issues
1. Select the correct kernel in VS Code (`.venv` interpreter)
2. Restart the kernel: `Kernel → Restart`
3. Re-run imports

### Notebook Kernel Issues
1. Select the correct kernel in VS Code (`.venv` interpreter)
2. Restart the kernel: `Kernel → Restart`
3. Re-run imports

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Hugging Face for the Inference API
- Google for Gemini API
- The open-source AI community

## 📧 Contact

- GitHub: [@BartonChenTW](https://github.com/BartonChenTW)
- Issues: [GitHub Issues](https://github.com/BartonChenTW/LLM-data-processer/issues)

## 🗺️ Roadmap

- [ ] Add streaming response support
- [ ] Support for more LLM providers (Anthropic, Cohere)
- [ ] Enhanced data visualization
- [ ] Model fine-tuning utilities
- [ ] Export conversation history
- [ ] Multi-language support

---

**Star ⭐ this repository if you find it helpful!**
