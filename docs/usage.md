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
