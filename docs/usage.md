# Usage Guide

This guide covers common usage patterns for LLM Data Processer.

## Basic Usage

### Initialize AIHelper

```python
from llm_helper import AIHelper

# Using Llama-3.1 (recommended)
ai = AIHelper(model_name='Llama-3.1')

# Using Mistral-7B
ai = AIHelper(model_name='Mistral-7B')

# Disable auto-display (for scripts)
ai = AIHelper(model_name='Llama-3.1', display_response=False)
```

### Ask Questions

```python
# Simple question
response = ai.ask("What is Python?")

# Without history
response = ai.ask("Explain AI", with_history=False)

# Get response as string
ai_script = AIHelper(display_response=False)
answer = ai_script.ask("What is 2+2?")
print(answer)
```

## PDF Document Processing

### Extract and Analyze PDFs

```python
from llm_helper import AIHelper, read_pdf2text

# Extract text from PDF
pdf_text = read_pdf2text('research_paper.pdf')

# Initialize AI and attach PDF content
ai = AIHelper(model_name='Llama-3.1')
ai.attach_data('Research Paper', pdf_text)

# Query the document
ai.ask('What are the key findings?')
ai.ask('Summarize the methodology')
ai.ask('List all references mentioned')
```

### Using with pdfplumber directly

```python
import pdfplumber
from llm_helper import AIHelper

pdf_text = ""
with pdfplumber.open('document.pdf') as pdf:
    for page in pdf.pages:
        pdf_text += page.extract_text() + "\n"

ai = AIHelper()
ai.attach_data('PDF', pdf_text)
ai.ask('Analyze this document')
```

## Data Integration

### Attach DataFrames

```python
import pandas as pd

# Create data
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
})

# Attach to AI
ai.attach_data(df)

# Query your data
ai.ask("Who has the highest salary?")
ai.ask("What is the average age?")
ai.ask("Show me insights about this data")
```

### Multiple DataFrames

```python
# Sales data
df_sales = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Revenue": [10000, 15000, 12000]
})

# Customer data
df_customers = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Rating": [4.5, 4.2, 4.8]
})

# Attach both
ai.attach_data(df_sales)
ai.attach_data(df_customers)

# Query across datasets
ai.ask("Which product has best revenue and rating?")
```

### Toggle Data Usage

```python
# Query without attached data
response = ai.ask("General question", with_data=False)

# Query with data
response = ai.ask("Analyze the data", with_data=True)
```

## Custom Guidelines

### Add Guidelines

```python
# Add guidelines
ai.add_guideline("Respond in bullet points")
ai.add_guideline("Keep responses under 100 words")
ai.add_guideline("Use simple language")

# Ask with guidelines
ai.ask("Explain machine learning", with_guideline=True)

# Ask without guidelines
ai.ask("Explain machine learning", with_guideline=False)
```

### Guideline Examples

#### Business Format
```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.add_guideline("Structure: Summary, Analysis, Recommendation")
ai.add_guideline("Focus on ROI and business value")
ai.add_guideline("Write for non-technical audience")

response = ai.ask("Should we adopt AI?")
```

#### Technical Format
```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.add_guideline("Include code examples")
ai.add_guideline("Explain technical concepts in depth")
ai.add_guideline("Provide references and sources")

response = ai.ask("How does neural network work?")
```

## Conversation History

### Multi-turn Conversations

```python
ai = AIHelper(model_name='Llama-3.1')

# First question
ai.ask("What is Python?")

# Follow-up (uses context from previous)
ai.ask("What are its main advantages?")

# Continue conversation
ai.ask("Show me an example")
```

### View History

```python
# View chat history
print(ai.chat_history)

# Clear history (reset conversation)
ai.chat_history = []
```

### Independent Questions

```python
# Ask without using conversation history
response = ai.ask("Independent question", with_history=False)
```

## Interactive Chat Widget

### Launch Widget

```python
from llm_helper import AIHelper

ai = AIHelper(model_name='Llama-3.1')

# Launch interactive chat (Jupyter only)
ai.chat_widget()
```

### Widget Features

- **Text input**: Type your questions
- **Use Guideline checkbox**: Toggle guidelines on/off
- **Use Attached Data checkbox**: Toggle data context on/off
- **Ask button**: Submit your question
- **Output area**: View responses

## Google Gemini

### Basic Usage

```python
from llm_helper.ai_helper import AIHelper_Google

# Initialize
ai = AIHelper_Google()

# Ask with Google Search grounding
response = ai.ask("What are the latest AI developments?")
```

### Current Events

```python
# Gemini uses Google Search for current info
ai = AIHelper_Google(display_response=False)

response = ai.ask("What is the weather in Tokyo today?")
response = ai.ask("Latest cryptocurrency prices")
response = ai.ask("Recent AI research papers")
```

### View History

```python
# Check conversation history
for i, (prompt, response) in enumerate(ai.history, 1):
    print(f"Turn {i}:")
    print(f"  Q: {prompt}")
    print(f"  A: {response[:100]}...")
```

## Configuration

### Model Configuration

Edit `llm_helper/ai_helper.py` to customize:

```python
config = {
    'max_tokens': 2000,      # Max response length
    'temperature': 0.7,       # 0.0-1.0 (creative vs focused)
}
```

### Available Models

```python
llm_models = {
    'Llama-3.1': 'meta-llama/Llama-3.1-8B-Instruct',
    'Mistral-7B': 'mistralai/Mistral-7B-Instruct-v0.2'
}
```

## Structured Information Extraction

The `InfoExtractor` class enables extraction of structured data from text sources using custom Pydantic schemas with automatic retry logic for parsing errors.

### Basic Setup

```python
from llm_helper import InfoExtractor

# Initialize with Gemini (currently only supported provider)
extractor = InfoExtractor(
    api_provider='google',
    model='gemini-2.5-flash'
)
```

### Define Data Schema

```python
# Define your schema with field types and descriptions
schema_data = {
    'tech_type': 'StorageTechnology',
    'fields': {
        'name': {
            'field_type': 'str',
            'description': 'The name of the storage technology'
        },
        'description': {
            'field_type': 'str',
            'description': 'A brief description of what it is'
        },
        'advantages': {
            'field_type': 'List[str]',
            'description': 'List of key advantages'
        },
        'disadvantages': {
            'field_type': 'List[str]',
            'description': 'List of main limitations'
        },
        'use_cases': {
            'field_type': 'List[str]',
            'description': 'Common use cases or applications'
        }
    }
}

# Load the schema
extractor.load_data_schema(schema_data)
```

### Configure Prompts

```python
# Base prompt for initial extraction
base_prompts = {
    'system': 'You are an expert at extracting structured information.',
    'human': '''Extract information about {technology_name} from the following source:

{info_source}

Return the data in this format:
{format_instructions}'''
}

# Fix prompt for retry attempts
fix_prompts = {
    'system': 'You are an expert at fixing malformed JSON outputs.',
    'human': '''The following output for {technology_name} has formatting errors:

{malformed_output}

Fix it to match this format:
{format_instructions}'''
}

extractor.load_prompt_templates(base_prompts, fix_prompts)
```

### Load Information Source

```python
# Provide the technology name and source text
info_text = """
PostgreSQL is an open-source relational database...
[your source text here]
"""

extractor.load_info_source(
    technology_name='PostgreSQL',
    info_source=info_text
)
```

### Extract Information

```python
# Extract with automatic retry on parsing errors
try:
    result = extractor.extract_tech_info(max_retries=3)
    
    # Access structured fields
    print(f"Technology: {result.name}")
    print(f"Description: {result.description}")
    print(f"Advantages: {', '.join(result.advantages)}")
    print(f"Use Cases: {', '.join(result.use_cases)}")
    
except Exception as e:
    print(f"Extraction failed: {e}")
```

### Complete Example

```python
from llm_helper import InfoExtractor

# Initialize
extractor = InfoExtractor(api_provider='google')

# Define schema
schema = {
    'tech_type': 'DatabaseTechnology',
    'fields': {
        'name': {'field_type': 'str', 'description': 'Database name'},
        'type': {'field_type': 'str', 'description': 'SQL or NoSQL'},
        'features': {'field_type': 'List[str]', 'description': 'Key features'},
        'pricing': {'field_type': 'str', 'description': 'Pricing model'}
    }
}

# Configure
extractor.load_data_schema(schema)
extractor.load_prompt_templates(base_prompts, fix_prompts)

# Extract from multiple sources
databases = ['MongoDB', 'Redis', 'Cassandra']
results = []

for db_name in databases:
    # Get info from web, PDF, or other source
    info = get_database_info(db_name)
    
    extractor.load_info_source(db_name, info)
    result = extractor.extract_tech_info(max_retries=3)
    results.append(result)

# Process results
for tech in results:
    print(f"{tech.name}: {tech.type}")
    print(f"Features: {', '.join(tech.features)}")
```

### Validation and Error Handling

```python
# Validate setup before extraction
try:
    extractor.validate_setup()
    print("✓ All components configured correctly")
except ValueError as e:
    print(f"Setup error: {e}")

# The validate_setup() checks for:
# - DataSchema loaded
# - Parser initialized
# - Base prompt configured
# - Fix prompt configured
# - Technology name set
# - Info source provided
```

### Advanced Schema Types

```python
# Complex nested schemas
advanced_schema = {
    'tech_type': 'CompanyProfile',
    'fields': {
        'name': {'field_type': 'str', 'description': 'Company name'},
        'founded_year': {'field_type': 'int', 'description': 'Year founded'},
        'revenue': {'field_type': 'float', 'description': 'Annual revenue in millions'},
        'products': {'field_type': 'List[str]', 'description': 'Main products'},
        'is_public': {'field_type': 'bool', 'description': 'Publicly traded'},
        'headquarters': {'field_type': 'str', 'description': 'HQ location'},
        'employee_count': {'field_type': 'int', 'description': 'Number of employees'}
    }
}
```

## Best Practices

### 1. Use Appropriate Models

- **Llama-3.1**: General purpose, good reasoning
- **Mistral-7B**: Fast responses, good for simple tasks
- **Gemini**: Current events, fact-checking, web search

### 2. Manage Context

```python
# For independent queries
ai.ask(prompt, with_history=False)

# For conversations
ai.ask(prompt, with_history=True)
```

### 3. Use Guidelines Effectively

```python
# Define behavior upfront
ai.add_guideline("Be concise")
ai.add_guideline("Use examples")

# Toggle when needed
ai.ask(prompt, with_guideline=True)
```

### 4. Optimize for Scripts

```python
# Disable display for automation
ai = AIHelper(display_response=False)

# Get responses as strings
responses = []
for question in questions:
    answer = ai.ask(question, with_history=False)
    responses.append(answer)
```

## Common Patterns

### Pattern 1: Data Analysis Report

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.add_guideline("Provide insights in 3 sections: Summary, Trends, Recommendations")
ai.attach_data(df)

report = ai.ask("Analyze this dataset and provide a report")
```

### Pattern 2: Batch Processing

```python
ai = AIHelper(display_response=False)

questions = [
    "What is AI?",
    "What is ML?",
    "What is DL?"
]

answers = [ai.ask(q, with_history=False) for q in questions]
```

### Pattern 3: Interactive Exploration

```python
ai = AIHelper(model_name='Llama-3.1')
ai.attach_data(df)

# Launch widget for exploration
ai.chat_widget()
```

## Next Steps

- See [Examples](examples.md) for complete code samples
- Check [API Reference](api-reference.md) for all methods
- Read [Contributing Guide](contributing.md) to extend functionality
