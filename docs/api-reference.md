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

## InfoExtractor

Class for extracting structured information from text using custom Pydantic schemas with automatic retry logic.

### Constructor

```python
InfoExtractor(
    api_provider: str = 'google',
    model: str = 'gemini-2.5-flash',
    path_env: str = ''
)
```

**Parameters:**

- `api_provider` (str, optional): LLM provider. Currently supports `'google'`. Default: `'google'`
- `model` (str, optional): Model name. Default: `'gemini-2.5-flash'`
- `path_env` (str, optional): Path to .env file. Default: `''`

**Raises:**

- `ValueError`: If unsupported API provider is specified

**Example:**

```python
from llm_helper import InfoExtractor

extractor = InfoExtractor(
    api_provider='google',
    model='gemini-2.5-flash'
)
```

### Methods

#### load_data_schema()

Dynamically creates a Pydantic model based on provided schema data.

```python
load_data_schema(schema_data: Dict[str, Any]) -> BaseModel
```

**Parameters:**

- `schema_data` (dict): Schema definition with `tech_type` and `fields`
  - `tech_type` (str): Name for the Pydantic model
  - `fields` (dict): Field definitions with `field_type` and `description`

**Returns:**

- `BaseModel`: Dynamically created Pydantic model class

**Example:**

```python
schema = {
    'tech_type': 'DatabaseInfo',
    'fields': {
        'name': {
            'field_type': 'str',
            'description': 'Database name'
        },
        'version': {
            'field_type': 'str',
            'description': 'Current version'
        },
        'features': {
            'field_type': 'List[str]',
            'description': 'Key features'
        }
    }
}

extractor.load_data_schema(schema)
```

**Supported Field Types:**

- `str`: String fields
- `int`: Integer fields
- `float`: Floating point numbers
- `bool`: Boolean fields
- `List[str]`: List of strings
- `List[int]`: List of integers
- `Dict[str, str]`: String dictionaries

#### load_prompt_templates()

Load prompt templates for extraction and error fixing.

```python
load_prompt_templates(
    base_prompt_dict: Dict[str, str],
    fix_prompt_dict: Dict[str, str]
) -> None
```

**Parameters:**

- `base_prompt_dict` (dict): Initial extraction prompt with `system` and `human` keys
- `fix_prompt_dict` (dict): Retry/fix prompt with `system` and `human` keys

**Template Variables:**

Base prompt:
- `{technology_name}`: Name of item being extracted
- `{info_source}`: Source text
- `{format_instructions}`: Auto-generated Pydantic format

Fix prompt:
- `{technology_name}`: Name of item
- `{malformed_output}`: Previous failed output
- `{format_instructions}`: Expected format

**Example:**

```python
base_prompts = {
    'system': 'You are an expert at extracting structured data.',
    'human': '''Extract information about {technology_name}:

Source: {info_source}

Format: {format_instructions}'''
}

fix_prompts = {
    'system': 'You fix malformed JSON outputs.',
    'human': '''Fix this output for {technology_name}:

{malformed_output}

Expected format: {format_instructions}'''
}

extractor.load_prompt_templates(base_prompts, fix_prompts)
```

#### load_info_source()

Load the information source and technology name for extraction.

```python
load_info_source(technology_name: str, info_source: str) -> None
```

**Parameters:**

- `technology_name` (str): Name/identifier of the technology or entity
- `info_source` (str): Source text to extract information from

**Example:**

```python
info_text = """
Redis is an in-memory data structure store...
"""

extractor.load_info_source('Redis', info_text)
```

#### validate_setup()

Validates that all required components are configured before extraction.

```python
validate_setup() -> bool
```

**Returns:**

- `bool`: `True` if all components are ready

**Raises:**

- `ValueError`: If any required component is missing, with detailed error messages

**Validates:**

- DataSchema is loaded
- Parser is initialized
- Base prompt is configured
- Fix prompt is configured
- Technology name is set
- Info source is provided

**Example:**

```python
try:
    extractor.validate_setup()
    print("✓ Setup complete")
except ValueError as e:
    print(f"Setup error: {e}")
```

#### extract_tech_info()

Attempts to extract structured information with automatic retry on parsing errors.

```python
extract_tech_info(max_retries: int = 3) -> BaseModel
```

**Parameters:**

- `max_retries` (int, optional): Maximum retry attempts for fixing malformed outputs. Default: `3`

**Returns:**

- `BaseModel`: Pydantic model instance with extracted data

**Raises:**

- `ValueError`: If setup validation fails
- `OutputParserException`: If extraction fails after all retries

**Workflow:**

1. Validates setup
2. Generates initial extraction using base prompt
3. Attempts to parse JSON output
4. On failure, uses fix prompt to correct output
5. Retries up to `max_retries` times
6. Returns validated Pydantic object

**Example:**

```python
try:
    result = extractor.extract_tech_info(max_retries=3)
    
    print(f"Name: {result.name}")
    print(f"Description: {result.description}")
    print(f"Features: {', '.join(result.features)}")
    
except OutputParserException as e:
    print(f"Extraction failed: {e}")
except ValueError as e:
    print(f"Setup error: {e}")
```

### Attributes

#### DataSchema

```python
DataSchema: Optional[BaseModel]
```

Dynamically created Pydantic model. Initially `None`, set by `load_data_schema()`.

#### llm

```python
llm: ChatGoogleGenerativeAI
```

LangChain LLM instance for generation.

#### parser

```python
parser: JsonOutputParser
```

JSON parser with Pydantic validation. Created by `load_data_schema()`.

#### technology_name

```python
technology_name: str
```

Name of the entity being extracted. Set by `load_info_source()`.

#### info_source

```python
info_source: str
```

Source text for extraction. Set by `load_info_source()`.

#### base_prompt

```python
base_prompt: ChatPromptTemplate
```

LangChain prompt for initial extraction. Set by `load_prompt_templates()`.

#### fix_prompt

```python
fix_prompt: ChatPromptTemplate
```

LangChain prompt for fixing malformed outputs. Set by `load_prompt_templates()`.

### Complete Example

```python
from llm_helper import InfoExtractor

# Initialize
extractor = InfoExtractor(api_provider='google')

# Define schema
schema = {
    'tech_type': 'StorageTechnology',
    'fields': {
        'name': {'field_type': 'str', 'description': 'Technology name'},
        'type': {'field_type': 'str', 'description': 'Storage type'},
        'advantages': {'field_type': 'List[str]', 'description': 'Key benefits'},
        'disadvantages': {'field_type': 'List[str]', 'description': 'Limitations'}
    }
}

# Configure prompts
base_prompts = {
    'system': 'Extract structured storage technology information.',
    'human': 'Extract data for {technology_name} from: {info_source}\n{format_instructions}'
}

fix_prompts = {
    'system': 'Fix malformed JSON to match the schema.',
    'human': 'Fix this: {malformed_output}\nFormat: {format_instructions}'
}

# Setup
extractor.load_data_schema(schema)
extractor.load_prompt_templates(base_prompts, fix_prompts)

# Extract
info = "PostgreSQL is a powerful open-source relational database..."
extractor.load_info_source('PostgreSQL', info)

# Get structured result
result = extractor.extract_tech_info(max_retries=3)
print(f"✓ Extracted: {result.name} ({result.type})")
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
add_guideline(guideline_name: str, guideline: str) -> None
```

**Parameters:**

- `guideline_name` (str): Unique name/key for the guideline
- `guideline` (str): A string describing desired behavior

**Example:**

```python
ai.add_guideline('format', "Respond in bullet points")
ai.add_guideline('length', "Keep responses under 100 words")
ai.add_guideline('tone', "Use professional language")
```

#### attach_data()

Attach a pandas DataFrame or string data to the AI context.

```python
attach_data(data_name: str, attached_data: Union[pd.DataFrame, str]) -> None
```

**Parameters:**

- `data_name` (str): Unique name/key for the attached data
- `attached_data` (pd.DataFrame or str): Data to attach (DataFrame or string)

**Example:**

```python
import pandas as pd

# Attach DataFrame
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
ai.attach_data('employees', df)

# Attach string data
ai.attach_data('context', "Company founded in 2020...")

ai.ask("Who is older in the employee data?")
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
guideline: Dict[str, str]
```

Dictionary of custom guidelines with name/key mapping to guideline text.

**Example:**

```python
# View guidelines
print(ai.guideline)
# Output: {'format': 'Respond in bullet points', 'length': 'Keep under 100 words'}

# Clear guidelines
ai.guideline = {}
```

#### attached_data

```python
attached_data: Dict[str, Union[pd.DataFrame, str]]
```

Dictionary of attached data with name/key mapping to DataFrame or string data.

**Example:**

```python
# View attached data
print(ai.attached_data.keys())
# Output: dict_keys(['employees', 'sales_data'])

# Clear data
ai.attached_data = {}
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
