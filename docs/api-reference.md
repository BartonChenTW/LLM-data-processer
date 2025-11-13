# API Reference

Complete reference for all classes and methods in LLM Data Processer.

## Utility Functions

### read_pdf2text()

Extract text content from a PDF file.

```python
read_pdf2text(pdf_path: str) -> str
```

**Parameters:**

- `pdf_path` (str): Path to the PDF file

**Returns:**

- `str`: Extracted text from all pages

**Raises:**

- `FileNotFoundError`: If PDF file doesn't exist
- `PDFSyntaxError`: If PDF is corrupted

**Example:**

```python
from llm_helper import read_pdf2text

text = read_pdf2text('document.pdf')
print(f"Extracted {len(text)} characters")
```

## AIHelper

Main class for interacting with Hugging Face models.

### Constructor

```python
AIHelper(model_name: str = 'Mistral-7B', display_response: bool = True)
```

**Parameters:**

- `model_name` (str, optional): Model to use. Options: `'Llama-3.1'`, `'Mistral-7B'`. Default: `'Mistral-7B'`
- `display_response` (bool, optional): Whether to display responses in Markdown. Default: `True`

**Example:**

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)
```

### Methods

#### ask()

Generate a response from the LLM.

```python
ask(
    prompt: str,
    display_response: bool = None,
    with_guideline: bool = True,
    with_data: bool = True,
    with_history: bool = True
) -> str
```

**Parameters:**

- `prompt` (str): Your question or instruction
- `display_response` (bool, optional): Override instance display setting
- `with_guideline` (bool, optional): Include custom guidelines. Default: `True`
- `with_data` (bool, optional): Include attached DataFrames. Default: `True`
- `with_history` (bool, optional): Include conversation history. Default: `True`

**Returns:**

- `str`: The model's response (if `display_response=False`)

**Example:**

```python
# Basic usage
response = ai.ask("What is Python?")

# Without history
response = ai.ask("Explain AI", with_history=False)

# Without guidelines or data
response = ai.ask("General question", with_guideline=False, with_data=False)
```

#### add_guideline()

Add a custom guideline to influence model behavior.

```python
add_guideline(guideline: str) -> None
```

**Parameters:**

- `guideline` (str): A string describing desired behavior

**Example:**

```python
ai.add_guideline("Respond in bullet points")
ai.add_guideline("Keep responses under 100 words")
```

#### attach_data()

Attach a pandas DataFrame to the AI context.

```python
attach_data(data: pd.DataFrame) -> None
```

**Parameters:**

- `data` (pd.DataFrame): DataFrame to attach

**Example:**

```python
import pandas as pd

df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
ai.attach_data(df)
ai.ask("Who is older?")
```

#### chat_widget()

Launch an interactive chat interface (Jupyter notebooks only).

```python
chat_widget() -> None
```

**Example:**

```python
ai.chat_widget()
```

**Features:**

- Text input area
- Checkboxes for guideline/data toggling
- Ask button
- Live output display

### Attributes

#### chat_history

```python
chat_history: List[Dict[str, str]]
```

List of conversation turns. Each entry is a dict with `role` and `content` keys.

**Example:**

```python
# View history
print(ai.chat_history)

# Clear history
ai.chat_history = []
```

#### guideline

```python
guideline: List[str]
```

List of custom guidelines.

**Example:**

```python
# View guidelines
print(ai.guideline)

# Clear guidelines
ai.guideline = []
```

#### attached_data

```python
attached_data: List[pd.DataFrame]
```

List of attached DataFrames.

**Example:**

```python
# View attached data
print(ai.attached_data)

# Clear data
ai.attached_data = []
```

#### llm_models

```python
llm_models: Dict[str, str]
```

Dictionary mapping model names to Hugging Face model IDs.

**Available Models:**

```python
{
    'Llama-3.1': 'meta-llama/Llama-3.1-8B-Instruct',
    'Mistral-7B': 'mistralai/Mistral-7B-Instruct-v0.2'
}
```

#### config

```python
config: Dict[str, Any]
```

Configuration dictionary for generation parameters.

**Default:**

```python
{
    'max_tokens': 2000,
    'temperature': 0.7
}
```

## AIHelper_Google

Class for Google Gemini with Google Search grounding.

### Constructor

```python
AIHelper_Google(
    model: str = 'gemini-2.5-flash',
    path_env: str = '',
    display_response: bool = True
)
```

**Parameters:**

- `model` (str, optional): Gemini model to use. Default: `'gemini-2.5-flash'`
- `path_env` (str, optional): Path to .env file. Default: `''`
- `display_response` (bool, optional): Whether to display responses. Default: `True`

**Example:**

```python
from llm_helper.ai_helper import AIHelper_Google

ai = AIHelper_Google(display_response=False)
```

### Methods

#### ask()

Generate a response using Google Gemini.

```python
ask(prompt: str, display_response: bool = None) -> str
```

**Parameters:**

- `prompt` (str): Your question or instruction
- `display_response` (bool, optional): Override instance display setting

**Returns:**

- `str`: The model's response (if `display_response=False`)

**Example:**

```python
# Current events with Google Search
response = ai.ask("What are the latest AI developments in 2025?")

# Fact-checking
response = ai.ask("What is the population of Japan?")
```

### Attributes

#### history

```python
history: List[Tuple[str, str]]
```

List of (prompt, response) tuples representing conversation history.

**Example:**

```python
# View history
for prompt, response in ai.history:
    print(f"Q: {prompt}")
    print(f"A: {response}\n")
```

#### config

```python
config: types.GenerateContentConfig
```

Google Gemini configuration object.

**Default Settings:**

```python
{
    'temperature': 0.3,
    'top_p': 0.9,
    'top_k': 40,
    'candidate_count': 1,
    'max_output_tokens': 2000,
    'tools': [GoogleSearch()]
}
```

## Configuration Objects

### LLM Models

```python
llm_models = {
    'Llama-3.1': 'meta-llama/Llama-3.1-8B-Instruct',
    'Mistral-7B': 'mistralai/Mistral-7B-Instruct-v0.2'
}
```

### Hugging Face Config

```python
config = {
    'max_tokens': 2000,      # Maximum response length
    'temperature': 0.7       # Randomness (0.0-1.0)
}
```

**Temperature Guide:**

- `0.0-0.3`: Focused, deterministic
- `0.4-0.7`: Balanced (recommended)
- `0.8-1.0`: Creative, varied

### Google Gemini Config

```python
config_google = types.GenerateContentConfig(
    temperature=0.3,
    top_p=0.9,
    top_k=40,
    candidate_count=1,
    max_output_tokens=2000,
    tools=[types.Tool(google_search=types.GoogleSearch())]
)
```

## Environment Variables

### Required

- `HF_TOKEN`: Hugging Face API token
- `GEMINI_API_KEY`: Google Gemini API key

### Optional

- `OPENAI_API_KEY`: OpenAI API key (for future providers)

**Set in Shell:**

```bash
export HF_TOKEN="your_token"
export GEMINI_API_KEY="your_key"
```

**Or in Python:**

```python
import os
os.environ['HF_TOKEN'] = 'your_token'
os.environ['GEMINI_API_KEY'] = 'your_key'
```

## Error Handling

### Common Exceptions

```python
try:
    ai = AIHelper(model_name='Llama-3.1')
    response = ai.ask("Test question")
except ImportError as e:
    print(f"Missing dependency: {e}")
except KeyError as e:
    print(f"API key not found: {e}")
except Exception as e:
    print(f"Error: {e}")
```

### Authentication Errors

If API keys are missing or invalid:

```python
# Check if keys are set
import os
if not os.getenv('HF_TOKEN'):
    raise ValueError("HF_TOKEN not set. Get one at https://huggingface.co/settings/tokens")
```

## Type Hints

For type checking and IDE support:

```python
from typing import List, Dict, Optional
import pandas as pd

def process_data(ai: AIHelper, df: pd.DataFrame) -> str:
    ai.attach_data(df)
    response: str = ai.ask("Analyze this data", display_response=False)
    return response
```

## Next Steps

- See [Usage Guide](usage.md) for practical examples
- Check [Examples](examples.md) for complete code samples
- Read [Contributing](contributing.md) to extend the API
