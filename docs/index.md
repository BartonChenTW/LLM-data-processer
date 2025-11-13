# Welcome to LLM Data Processer

A Python library for seamlessly working with Large Language Models (LLMs) from multiple providers. Easily integrate Hugging Face models, Google Gemini, OpenAI, and more with a unified interface.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/BartonChenTW/LLM-data-processer/blob/main/LICENSE)

## Features

- 🤖 **Multi-Provider Support**: Hugging Face, Google Gemini, OpenAI
- 💬 **Interactive Chat Widget**: Built-in Jupyter notebook UI
- 📊 **Data Integration**: Query pandas DataFrames with natural language
- 📄 **PDF Processing**: Extract and analyze PDF documents
- 🔍 **Structured Information Extraction**: Extract structured data with custom schemas and automatic retry logic
- 📝 **Guideline System**: Custom guidelines to control model behavior
- 🎨 **History Management**: Automatic conversation tracking
- 🔧 **Easy Configuration**: Simple initialization with sensible defaults

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from llm_helper import AIHelper

# Initialize with Llama-3.1
ai = AIHelper(model_name='Llama-3.1')

# Ask a question
response = ai.ask("What is machine learning?")
print(response)
```

### Interactive Chat

```python
# Launch chat widget in Jupyter
ai.chat_widget()
```

## Next Steps

- Check out the [Installation Guide](installation.md) for detailed setup
- Read the [Usage Guide](usage.md) for examples
- Explore the [API Reference](api-reference.md) for all methods
- See [Examples](examples.md) for real-world use cases

## Support

- 📖 [Documentation](https://bartonchenTW.github.io/LLM-data-processer/)
- 🐛 [Report Issues](https://github.com/BartonChenTW/LLM-data-processer/issues)
- 💬 [Discussions](https://github.com/BartonChenTW/LLM-data-processer/discussions)
