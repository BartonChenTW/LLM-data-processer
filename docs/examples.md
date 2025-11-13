# Examples

Complete code examples demonstrating various use cases.

## Basic Usage Examples

### Simple Question-Answer

```python
from llm_helper import AIHelper

ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Ask a question
response = ai.ask("What is machine learning?")
print(response)
```

### Multiple Questions

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)

questions = [
    "What is Python?",
    "What is JavaScript?",
    "What is Java?"
]

for question in questions:
    response = ai.ask(question, with_history=False)
    print(f"Q: {question}")
    print(f"A: {response}\n")
```

### Conversation with Context

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Multi-turn conversation
print("Q1: What is a neural network?")
response1 = ai.ask("What is a neural network?")
print(f"A1: {response1}\n")

print("Q2: How does it learn?")
response2 = ai.ask("How does it learn?")  # Uses context from Q1
print(f"A2: {response2}\n")

print("Q3: Give me a simple example")
response3 = ai.ask("Give me a simple example")  # Builds on conversation
print(f"A3: {response3}")
```

## PDF Document Analysis Examples

### Basic PDF Extraction

```python
from llm_helper import AIHelper, read_pdf2text

# Read PDF
pdf_text = read_pdf2text('./reports/annual_report.pdf')

# Setup AI
ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.attach_data('Annual Report', pdf_text)

# Query document
print("Q: What are the key highlights?")
response = ai.ask("Summarize the key highlights from this annual report", with_history=False)
print(f"A: {response}\n")

print("Q: What were the financial results?")
response = ai.ask("What were the financial results?", with_history=False)
print(f"A: {response}")
```

### Multi-Document Analysis

```python
from llm_helper import AIHelper, read_pdf2text
import os

# Read multiple PDFs
pdf_dir = './research_papers/'
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Attach all PDFs
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    text = read_pdf2text(pdf_path)
    ai.attach_data(f'Paper: {pdf_file}', text)

# Comparative analysis
response = ai.ask("Compare the methodologies across all papers", with_history=False)
print(response)
```

### PDF with Custom Guidelines

```python
from llm_helper import AIHelper, read_pdf2text

ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Add analysis guidelines
ai.add_guideline("Extract only factual information")
ai.add_guideline("Cite page numbers when possible")
ai.add_guideline("Structure: Finding → Evidence → Implication")

# Attach PDF
pdf_text = read_pdf2text('technical_spec.pdf')
ai.attach_data('Technical Specification', pdf_text)

# Structured query
response = ai.ask("What are the system requirements?", with_history=False)
print(response)
```

## Data Analysis Examples

### Employee Data Analysis

```python
import pandas as pd
from llm_helper import AIHelper

# Create employee dataset
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 30, 35, 28, 32],
    "Department": ["Engineering", "Sales", "Engineering", "HR", "Sales"],
    "Salary": [75000, 65000, 85000, 60000, 70000],
    "Years_Experience": [3, 5, 8, 4, 6]
})

# Initialize AI and attach data
ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.attach_data('employees', df)

# Query the data
print("Question: Who has the highest salary?")
print(ai.ask("Who has the highest salary?", with_history=False))

print("\nQuestion: What is the average salary by department?")
print(ai.ask("What is the average salary by department?", with_history=False))

print("\nQuestion: Provide 3 key insights")
print(ai.ask("Analyze this data and provide 3 key insights", with_history=False))
```

### Sales Performance Analysis

```python
import pandas as pd
from llm_helper import AIHelper

# Sales data
df_sales = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Units_Sold": [150, 500, 300, 200, 450],
    "Price": [1200, 25, 75, 350, 150],
    "Revenue": [180000, 12500, 22500, 70000, 67500]
})

# Customer satisfaction
df_satisfaction = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Rating": [4.5, 4.2, 4.7, 4.3, 4.6],
    "Reviews": [1250, 3200, 1800, 950, 2100]
})

# Attach both datasets
ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.attach_data('sales', df_sales)
ai.attach_data('satisfaction', df_satisfaction)

# Cross-dataset analysis
question = "Considering both revenue and customer ratings, which product should we focus on?"
print(f"Question: {question}")
print(ai.ask(question, with_history=False))
```

## Custom Guidelines Examples

### Bullet Point Format

```python
from llm_helper import AIHelper

ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Add formatting guidelines
ai.add_guideline('format', "Always respond in bullet points")
ai.add_guideline('length', "Keep each point under 20 words")
ai.add_guideline('count', "Provide exactly 5 points")

response = ai.ask("What are the benefits of Python?")
print(response)
```

### Business Report Format

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Business-oriented guidelines
ai.add_guideline('structure', "Structure: Executive Summary, Analysis, Recommendation")
ai.add_guideline('focus', "Focus on ROI and business value")
ai.add_guideline('language', "Use non-technical language")
ai.add_guideline('length', "Keep under 200 words")

response = ai.ask("Should our company adopt AI technology?")
print(response)
```

### Technical Documentation Style

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Technical writing guidelines
ai.add_guideline('code', "Include code examples")
ai.add_guideline('depth', "Explain with technical depth")
ai.add_guideline('structure', "Structure: Definition → Example → Use Case")

response = ai.ask("Explain Python decorators")
print(response)
```

### Toggle Guidelines

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.add_guideline('format', "Respond in haiku format (5-7-5 syllables)")

# With guideline (haiku)
print("With Guideline:")
print(ai.ask("Describe programming", with_guideline=True, with_history=False))

# Without guideline (normal)
print("\nWithout Guideline:")
print(ai.ask("Describe programming", with_guideline=False, with_history=False))
```

## Google Gemini Examples

### Current Events

```python
from llm_helper.ai_helper import AIHelper_Google

ai = AIHelper_Google(display_response=False)

# Search-grounded queries
print("Query: Latest AI developments in 2025")
response = ai.ask("What are the latest AI developments in 2025?")
print(response)

print("\nQuery: Current Bitcoin price")
response = ai.ask("What is the current price of Bitcoin?")
print(response)
```

### Research Questions

```python
ai = AIHelper_Google(display_response=False)

questions = [
    "What are the benefits of quantum computing?",
    "Latest research in renewable energy",
    "Current state of autonomous vehicles"
]

for question in questions:
    print(f"\nQ: {question}")
    response = ai.ask(question)
    print(f"A: {response[:200]}...")
```

### Multi-turn with Gemini

```python
ai = AIHelper_Google(display_response=False)

print("Q1: What is Python?")
response1 = ai.ask("What is Python?")
print(f"A1: {response1[:150]}...\n")

print("Q2: What about JavaScript?")
response2 = ai.ask("What about JavaScript?")
print(f"A2: {response2[:150]}...\n")

print("Q3: Which should I learn first?")
response3 = ai.ask("Which one should I learn first?")
print(f"A3: {response3[:150]}...")
```

## Interactive Chat Widget

### Basic Widget

```python
from llm_helper import AIHelper

ai = AIHelper(model_name='Llama-3.1')
ai.chat_widget()  # Launches interactive UI in Jupyter
```

### Widget with Pre-configured Context

```python
import pandas as pd
from llm_helper import AIHelper

# Prepare data and guidelines
df = pd.DataFrame({
    "City": ["Tokyo", "London", "NYC"],
    "Population": [14000000, 9000000, 8500000]
})

ai = AIHelper(model_name='Llama-3.1')
ai.attach_data('city_data', df)
ai.add_guideline('focus', "Focus on data-driven insights")
ai.add_guideline('compare', "Provide comparisons when relevant")

# Launch widget with context
ai.chat_widget()
```

## Advanced Patterns

### Batch Processing

```python
from llm_helper import AIHelper

ai = AIHelper(display_response=False)

# Process multiple prompts
prompts = [
    "Summarize: AI is transforming industries...",
    "Translate to French: Hello world",
    "Extract keywords: Machine learning uses algorithms..."
]

results = []
for prompt in prompts:
    response = ai.ask(prompt, with_history=False)
    results.append(response)

# Display results
for i, (prompt, result) in enumerate(zip(prompts, results), 1):
    print(f"{i}. {prompt[:30]}...")
    print(f"   Result: {result[:100]}...\n")
```

### Context Management

```python
ai = AIHelper(display_response=False)

# Conversation 1
ai.ask("What is Python?")
ai.ask("What are its features?")

# Save context
context_1 = ai.chat_history.copy()

# Start new conversation
ai.chat_history = []
ai.ask("What is JavaScript?")
ai.ask("What are its features?")

# Restore previous context
ai.chat_history = context_1
ai.ask("How do I install Python?")  # Continues first conversation
```

### Error Handling

```python
from llm_helper import AIHelper
import os

try:
    # Check API key
    if not os.getenv('HF_TOKEN'):
        raise ValueError("HF_TOKEN not set")
    
    ai = AIHelper(model_name='Llama-3.1', display_response=False)
    response = ai.ask("Test question")
    
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Data Pipeline

```python
import pandas as pd
from llm_helper import AIHelper

def analyze_dataframe(df: pd.DataFrame, questions: list) -> dict:
    """Analyze a DataFrame using AI."""
    ai = AIHelper(model_name='Llama-3.1', display_response=False)
    ai.attach_data('analysis_data', df)
    
    results = {}
    for question in questions:
        answer = ai.ask(question, with_history=False)
        results[question] = answer
    
    return results

# Use the pipeline
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
questions = ["What is the sum of column A?", "What is the average of column B?"]
results = analyze_dataframe(df, questions)

for q, a in results.items():
    print(f"Q: {q}")
    print(f"A: {a}\n")
```

## Structured Information Extraction Examples

### Basic Entity Extraction

```python
from llm_helper import InfoExtractor

# Initialize extractor
extractor = InfoExtractor(api_provider='google', model='gemini-2.5-flash')

# Define schema for company information
company_schema = {
    'tech_type': 'CompanyInfo',
    'fields': {
        'name': {'field_type': 'str', 'description': 'Company name'},
        'founded_year': {'field_type': 'int', 'description': 'Year founded'},
        'industry': {'field_type': 'str', 'description': 'Primary industry'},
        'products': {'field_type': 'List[str]', 'description': 'Main products/services'},
        'headquarters': {'field_type': 'str', 'description': 'HQ location'}
    }
}

# Setup prompts
base_prompts = {
    'system': 'You are an expert at extracting structured company information.',
    'human': '''Extract company information for {technology_name} from:

{info_source}

Format: {format_instructions}'''
}

fix_prompts = {
    'system': 'You fix malformed JSON to match company information schema.',
    'human': '''Fix this output for {technology_name}:

{malformed_output}

Expected format: {format_instructions}'''
}

# Configure extractor
extractor.load_data_schema(company_schema)
extractor.load_prompt_templates(base_prompts, fix_prompts)

# Extract from source
company_info = """
Tesla, Inc. was founded in 2003 and is headquartered in Austin, Texas.
The company produces electric vehicles, battery energy storage, and solar panels.
"""

extractor.load_info_source('Tesla', company_info)
result = extractor.extract_tech_info(max_retries=3)

# Display results
print(f"Company: {result.name}")
print(f"Founded: {result.founded_year}")
print(f"Industry: {result.industry}")
print(f"Products: {', '.join(result.products)}")
print(f"Headquarters: {result.headquarters}")
```

### Technology Comparison Extraction

```python
from llm_helper import InfoExtractor

# Schema for storage technologies
storage_schema = {
    'tech_type': 'StorageTechnology',
    'fields': {
        'name': {'field_type': 'str', 'description': 'Technology name'},
        'type': {'field_type': 'str', 'description': 'Type (e.g., relational, document, key-value)'},
        'description': {'field_type': 'str', 'description': 'Brief description'},
        'advantages': {'field_type': 'List[str]', 'description': 'Key advantages'},
        'disadvantages': {'field_type': 'List[str]', 'description': 'Main limitations'},
        'use_cases': {'field_type': 'List[str]', 'description': 'Common use cases'},
        'scalability': {'field_type': 'str', 'description': 'Scalability characteristics'}
    }
}

# Setup extractor
extractor = InfoExtractor(api_provider='google')
extractor.load_data_schema(storage_schema)

base_prompts = {
    'system': 'Extract detailed storage technology information.',
    'human': 'Analyze {technology_name}: {info_source}\n{format_instructions}'
}

fix_prompts = {
    'system': 'Fix JSON output to match storage technology schema.',
    'human': 'Fix: {malformed_output}\nFormat: {format_instructions}'
}

extractor.load_prompt_templates(base_prompts, fix_prompts)

# Extract multiple technologies
technologies = {
    'PostgreSQL': "PostgreSQL is a powerful open-source relational database...",
    'MongoDB': "MongoDB is a document-oriented NoSQL database...",
    'Redis': "Redis is an in-memory key-value data store..."
}

results = []
for tech_name, tech_info in technologies.items():
    extractor.load_info_source(tech_name, tech_info)
    result = extractor.extract_tech_info(max_retries=3)
    results.append(result)

# Compare results
print("Technology Comparison:")
for tech in results:
    print(f"\n{tech.name} ({tech.type})")
    print(f"  Advantages: {', '.join(tech.advantages[:2])}...")
    print(f"  Best for: {', '.join(tech.use_cases[:2])}...")
```

### PDF Document Extraction

```python
from llm_helper import InfoExtractor, read_pdf2text

# Extract text from PDF
pdf_content = read_pdf2text('product_spec.pdf')

# Define product specification schema
product_schema = {
    'tech_type': 'ProductSpecification',
    'fields': {
        'product_name': {'field_type': 'str', 'description': 'Product name'},
        'model_number': {'field_type': 'str', 'description': 'Model/version number'},
        'features': {'field_type': 'List[str]', 'description': 'Key features'},
        'specifications': {'field_type': 'Dict[str, str]', 'description': 'Technical specs'},
        'price_range': {'field_type': 'str', 'description': 'Price range'},
        'warranty': {'field_type': 'str', 'description': 'Warranty information'}
    }
}

# Setup and extract
extractor = InfoExtractor(api_provider='google')
extractor.load_data_schema(product_schema)
extractor.load_prompt_templates(base_prompts, fix_prompts)
extractor.load_info_source('Product XYZ', pdf_content)

product_info = extractor.extract_tech_info(max_retries=3)

print(f"Product: {product_info.product_name} ({product_info.model_number})")
print(f"Features: {', '.join(product_info.features)}")
print(f"Price: {product_info.price_range}")
```

### Research Paper Analysis

```python
from llm_helper import InfoExtractor

# Schema for academic papers
paper_schema = {
    'tech_type': 'ResearchPaper',
    'fields': {
        'title': {'field_type': 'str', 'description': 'Paper title'},
        'authors': {'field_type': 'List[str]', 'description': 'Author names'},
        'year': {'field_type': 'int', 'description': 'Publication year'},
        'abstract': {'field_type': 'str', 'description': 'Brief summary'},
        'methodology': {'field_type': 'str', 'description': 'Research methodology'},
        'key_findings': {'field_type': 'List[str]', 'description': 'Main findings'},
        'limitations': {'field_type': 'List[str]', 'description': 'Study limitations'},
        'future_work': {'field_type': 'str', 'description': 'Suggested future research'}
    }
}

# Configure
extractor = InfoExtractor(api_provider='google')
extractor.load_data_schema(paper_schema)

base_prompts = {
    'system': 'Extract structured research paper information.',
    'human': 'Extract from {technology_name}:\n{info_source}\n{format_instructions}'
}

fix_prompts = {
    'system': 'Fix JSON to match research paper schema.',
    'human': 'Fix: {malformed_output}\nFormat: {format_instructions}'
}

extractor.load_prompt_templates(base_prompts, fix_prompts)

# Extract from paper abstract/content
paper_content = """
Title: Deep Learning for Natural Language Processing
Authors: John Smith, Jane Doe, Bob Wilson
Published: 2024

Abstract: This paper explores transformer architectures...
"""

extractor.load_info_source('NLP Research Paper', paper_content)
paper = extractor.extract_tech_info(max_retries=3)

print(f"Title: {paper.title}")
print(f"Authors: {', '.join(paper.authors)}")
print(f"Year: {paper.year}")
print(f"Key Findings:")
for finding in paper.key_findings:
    print(f"  - {finding}")
```

### Error Handling with Validation

```python
from llm_helper import InfoExtractor
from langchain_core.exceptions import OutputParserException

extractor = InfoExtractor(api_provider='google')

# Define schema
schema = {
    'tech_type': 'DatabaseInfo',
    'fields': {
        'name': {'field_type': 'str', 'description': 'Database name'},
        'type': {'field_type': 'str', 'description': 'Database type'}
    }
}

extractor.load_data_schema(schema)
extractor.load_prompt_templates(base_prompts, fix_prompts)

# Validate setup before extraction
try:
    extractor.validate_setup()
    print("✓ Setup validated successfully")
except ValueError as e:
    print(f"Setup validation failed: {e}")
    exit(1)

# Extract with error handling
extractor.load_info_source('MySQL', "MySQL is a relational database...")

try:
    result = extractor.extract_tech_info(max_retries=3)
    print(f"✓ Successfully extracted: {result.name} ({result.type})")
except OutputParserException as e:
    print(f"✗ Extraction failed after retries: {e}")
except Exception as e:
    print(f"✗ Unexpected error: {e}")
```

### Batch Extraction Pipeline

```python
from llm_helper import InfoExtractor
from typing import List, Dict

def batch_extract_technologies(
    tech_data: Dict[str, str],
    schema: dict,
    max_retries: int = 3
) -> List:
    """Extract structured info from multiple sources."""
    
    extractor = InfoExtractor(api_provider='google')
    extractor.load_data_schema(schema)
    
    # Configure prompts
    base_prompts = {
        'system': 'Extract structured technology information.',
        'human': 'Extract {technology_name} from: {info_source}\n{format_instructions}'
    }
    fix_prompts = {
        'system': 'Fix malformed JSON.',
        'human': 'Fix: {malformed_output}\nFormat: {format_instructions}'
    }
    extractor.load_prompt_templates(base_prompts, fix_prompts)
    
    results = []
    for name, info in tech_data.items():
        try:
            extractor.load_info_source(name, info)
            result = extractor.extract_tech_info(max_retries=max_retries)
            results.append(result)
            print(f"✓ Extracted: {name}")
        except Exception as e:
            print(f"✗ Failed for {name}: {e}")
    
    return results

# Define schema
tech_schema = {
    'tech_type': 'TechnologyProfile',
    'fields': {
        'name': {'field_type': 'str', 'description': 'Technology name'},
        'category': {'field_type': 'str', 'description': 'Category'},
        'features': {'field_type': 'List[str]', 'description': 'Key features'}
    }
}

# Batch process
tech_sources = {
    'Docker': "Docker is a containerization platform...",
    'Kubernetes': "Kubernetes is an orchestration system...",
    'Jenkins': "Jenkins is a CI/CD automation server..."
}

results = batch_extract_technologies(tech_sources, tech_schema)

# Display results
for tech in results:
    print(f"\n{tech.name} - {tech.category}")
    print(f"Features: {', '.join(tech.features)}")
```

## Complete Application Example

```python
"""
Complete data analysis application using LLM Data Processer.
"""

import pandas as pd
from llm_helper import AIHelper

def main():
    # Load data
    df = pd.read_csv("your_data.csv")  # Replace with your data
    
    # Initialize AI
    ai = AIHelper(model_name='Llama-3.1', display_response=False)
    
    # Configure behavior
    ai.add_guideline('insights', "Provide actionable insights")
    ai.add_guideline('support', "Use data to support conclusions")
    ai.add_guideline('structure', "Structure: Finding → Evidence → Recommendation")
    
    # Attach data
    ai.attach_data('dataset', df)
    
    # Generate report
    report = ai.ask("""
        Analyze this dataset and provide:
        1. Key statistics summary
        2. Notable trends or patterns
        3. Three actionable recommendations
    """, with_history=False)
    
    # Output
    print("="*60)
    print("DATA ANALYSIS REPORT")
    print("="*60)
    print(report)
    print("="*60)

if __name__ == "__main__":
    main()
```

## Next Steps

- Check the [API Reference](api-reference.md) for all available methods
- Read the [Usage Guide](usage.md) for detailed explanations
- See [Contributing](contributing.md) to add your own examples
