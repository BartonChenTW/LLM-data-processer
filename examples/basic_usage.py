"""
Basic usage examples for LLM Data Processer.

This script demonstrates the fundamental operations of the AIHelper class.
"""

import os
from llm_helper import AIHelper

# Ensure API key is set
if not os.getenv("HF_TOKEN"):
    print("Warning: HF_TOKEN environment variable not set!")
    print("Get your token at: https://huggingface.co/settings/tokens")
    exit(1)

# Initialize AIHelper with Llama-3.1
print("Initializing AIHelper with Llama-3.1...")
ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Example 1: Simple question
print("\n" + "="*50)
print("Example 1: Simple Question")
print("="*50)
response = ai.ask("What is Python programming language?")
print(f"Response: {response}")

# Example 2: Question without history
print("\n" + "="*50)
print("Example 2: Independent Question (no history)")
print("="*50)
response = ai.ask(
    "Explain machine learning in simple terms",
    with_history=False
)
print(f"Response: {response}")

# Example 3: Conversation with history
print("\n" + "="*50)
print("Example 3: Multi-turn Conversation")
print("="*50)
ai_chat = AIHelper(model_name='Llama-3.1', display_response=False)
response1 = ai_chat.ask("What is a neural network?")
print(f"Q1: What is a neural network?")
print(f"A1: {response1[:200]}...")

response2 = ai_chat.ask("Can you give me an example?")
print(f"\nQ2: Can you give me an example?")
print(f"A2: {response2[:200]}...")

# Example 4: Display mode (for notebooks)
print("\n" + "="*50)
print("Example 4: Display Mode (best for notebooks)")
print("="*50)
ai_display = AIHelper(model_name='Llama-3.1', display_response=True)
print("Asking: 'What are the benefits of AI?'")
ai_display.ask("What are the benefits of AI?")

print("\n✅ All examples completed successfully!")
