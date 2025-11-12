"""
Google Gemini usage examples for LLM Data Processer.

This script demonstrates using Google Gemini with Google Search grounding.
"""

import os
from llm_helper.ai_helper import AIHelper_Google

# Ensure API key is set
if not os.getenv("GEMINI_API_KEY"):
    print("Warning: GEMINI_API_KEY environment variable not set!")
    print("Get your key at: https://aistudio.google.com/app/apikey")
    exit(1)

# Initialize Google Gemini helper
print("Initializing AIHelper_Google with Gemini 2.5 Flash...")
ai = AIHelper_Google(display_response=False)

# Example 1: Current events with Google Search
print("\n" + "="*60)
print("Example 1: Current Events (with Google Search)")
print("="*60)

print("\nQuery: What are the latest developments in AI in 2025?")
response = ai.ask("What are the latest developments in AI in 2025?")
print(f"\nResponse:\n{response}")

# Example 2: Fact-checking
print("\n" + "="*60)
print("Example 2: Fact-Checking with Web Search")
print("="*60)

print("\nQuery: What is the current price of Bitcoin?")
response = ai.ask("What is the current price of Bitcoin?")
print(f"\nResponse:\n{response}")

# Example 3: Research question
print("\n" + "="*60)
print("Example 3: Research Question")
print("="*60)

print("\nQuery: What are the benefits and risks of quantum computing?")
response = ai.ask("What are the benefits and risks of quantum computing?")
print(f"\nResponse:\n{response}")

# Example 4: Technical question
print("\n" + "="*60)
print("Example 4: Technical Documentation")
print("="*60)

print("\nQuery: How do I use GitHub Actions for CI/CD?")
response = ai.ask("How do I use GitHub Actions for CI/CD?")
print(f"\nResponse:\n{response}")

# Example 5: Comparison with conversation history
print("\n" + "="*60)
print("Example 5: Multi-turn Conversation")
print("="*60)

ai_chat = AIHelper_Google(display_response=False)

print("\nQ1: What is Python?")
response1 = ai_chat.ask("What is Python?")
print(f"A1: {response1[:200]}...\n")

print("Q2: What about JavaScript?")
response2 = ai_chat.ask("What about JavaScript?")
print(f"A2: {response2[:200]}...\n")

print("Q3: Which one should I learn first?")
response3 = ai_chat.ask("Which one should I learn first?")
print(f"A3: {response3[:200]}...")

# View conversation history
print("\n" + "="*60)
print("Conversation History")
print("="*60)
for i, (prompt, response) in enumerate(ai_chat.history, 1):
    print(f"\nTurn {i}:")
    print(f"  User: {prompt[:50]}...")
    print(f"  AI: {response[:100]}...")

print("\n✅ All Google Gemini examples completed!")
print("\nNote: Gemini uses Google Search for up-to-date information")
print("and fact-checking, making it ideal for current events and research.")
