"""
Custom guidelines example for LLM Data Processer.

This script shows how to use guidelines to control model behavior and output format.
"""

import os
from llm_helper import AIHelper

# Ensure API key is set
if not os.getenv("HF_TOKEN"):
    print("Warning: HF_TOKEN environment variable not set!")
    exit(1)

# Example 1: Bullet Point Format
print("="*60)
print("Example 1: Formatting with Guidelines")
print("="*60)

ai = AIHelper(model_name='Llama-3.1', display_response=False)
ai.add_guideline("Always respond in bullet points")
ai.add_guideline("Keep each point under 20 words")
ai.add_guideline("Provide exactly 5 points")

print("\nGuidelines set:")
for i, guideline in enumerate(ai.guideline, 1):
    print(f"  {i}. {guideline}")

print("\nQuery: What are the benefits of Python?")
response = ai.ask("What are the benefits of Python?")
print(f"\nResponse:\n{response}")

# Example 2: Technical Writing Style
print("\n" + "="*60)
print("Example 2: Technical Writing Style")
print("="*60)

ai_tech = AIHelper(model_name='Llama-3.1', display_response=False)
ai_tech.add_guideline("Use formal technical language")
ai_tech.add_guideline("Include specific examples with code")
ai_tech.add_guideline("Structure: Definition → Example → Use Case")

print("\nGuidelines set:")
for i, guideline in enumerate(ai_tech.guideline, 1):
    print(f"  {i}. {guideline}")

print("\nQuery: Explain list comprehension in Python")
response = ai_tech.ask("Explain list comprehension in Python")
print(f"\nResponse:\n{response}")

# Example 3: Business Analysis Style
print("\n" + "="*60)
print("Example 3: Business Analysis Style")
print("="*60)

ai_business = AIHelper(model_name='Llama-3.1', display_response=False)
ai_business.add_guideline("Write for a business audience, not technical")
ai_business.add_guideline("Focus on ROI and business value")
ai_business.add_guideline("Use headings: Executive Summary, Analysis, Recommendation")
ai_business.add_guideline("Keep under 150 words total")

print("\nGuidelines set:")
for i, guideline in enumerate(ai_business.guideline, 1):
    print(f"  {i}. {guideline}")

print("\nQuery: Should we adopt AI in our company?")
response = ai_business.ask("Should we adopt AI in our company?")
print(f"\nResponse:\n{response}")

# Example 4: Educational Style
print("\n" + "="*60)
print("Example 4: Educational Teaching Style")
print("="*60)

ai_edu = AIHelper(model_name='Llama-3.1', display_response=False)
ai_edu.add_guideline("Explain as if teaching a beginner")
ai_edu.add_guideline("Use analogies and real-world examples")
ai_edu.add_guideline("Break down complex concepts into simple steps")
ai_edu.add_guideline("End with a 'Try it yourself' suggestion")

print("\nGuidelines set:")
for i, guideline in enumerate(ai_edu.guideline, 1):
    print(f"  {i}. {guideline}")

print("\nQuery: What is machine learning?")
response = ai_edu.ask("What is machine learning?")
print(f"\nResponse:\n{response}")

# Example 5: Toggling Guidelines
print("\n" + "="*60)
print("Example 5: Toggling Guidelines On/Off")
print("="*60)

ai_toggle = AIHelper(model_name='Llama-3.1', display_response=False)
ai_toggle.add_guideline("Respond in haiku format (5-7-5 syllables)")

print("Guidelines set: Haiku format")

print("\n--- With Guideline (Haiku) ---")
response_with = ai_toggle.ask("Describe coding", with_guideline=True, with_history=False)
print(f"Response: {response_with}")

print("\n--- Without Guideline (Normal) ---")
response_without = ai_toggle.ask("Describe coding", with_guideline=False, with_history=False)
print(f"Response: {response_without}")

print("\n✅ All guideline examples completed!")
print("\nKey Takeaway: Guidelines allow you to shape responses without")
print("changing the underlying model or making API calls with system prompts.")
