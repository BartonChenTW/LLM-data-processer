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
ai.attach_data(df)

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
ai.attach_data(df_sales)
ai.attach_data(df_satisfaction)

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
ai.add_guideline("Always respond in bullet points")
ai.add_guideline("Keep each point under 20 words")
ai.add_guideline("Provide exactly 5 points")

response = ai.ask("What are the benefits of Python?")
print(response)
```

### Business Report Format

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Business-oriented guidelines
ai.add_guideline("Structure: Executive Summary, Analysis, Recommendation")
ai.add_guideline("Focus on ROI and business value")
ai.add_guideline("Use non-technical language")
ai.add_guideline("Keep under 200 words")

response = ai.ask("Should our company adopt AI technology?")
print(response)
```

### Technical Documentation Style

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Technical writing guidelines
ai.add_guideline("Include code examples")
ai.add_guideline("Explain with technical depth")
ai.add_guideline("Structure: Definition → Example → Use Case")

response = ai.ask("Explain Python decorators")
print(response)
```

### Toggle Guidelines

```python
ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.add_guideline("Respond in haiku format (5-7-5 syllables)")

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
ai.attach_data(df)
ai.add_guideline("Focus on data-driven insights")
ai.add_guideline("Provide comparisons when relevant")

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
    ai.attach_data(df)
    
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
    ai.add_guideline("Provide actionable insights")
    ai.add_guideline("Use data to support conclusions")
    ai.add_guideline("Structure: Finding → Evidence → Recommendation")
    
    # Attach data
    ai.attach_data(df)
    
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
