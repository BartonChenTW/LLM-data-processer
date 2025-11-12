"""
Data analysis example using pandas DataFrames with LLM Data Processer.

This script demonstrates how to attach data and query it using natural language.
"""

import os
import pandas as pd
from llm_helper import AIHelper

# Ensure API key is set
if not os.getenv("HF_TOKEN"):
    print("Warning: HF_TOKEN environment variable not set!")
    exit(1)

# Initialize AIHelper
print("Initializing AIHelper...")
ai = AIHelper(model_name='Llama-3.1', display_response=False)

# Example 1: Simple DataFrame
print("\n" + "="*60)
print("Example 1: Analyzing Employee Data")
print("="*60)

# Create employee data
employee_data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 30, 35, 28, 32],
    "Department": ["Engineering", "Sales", "Engineering", "HR", "Sales"],
    "Salary": [75000, 65000, 85000, 60000, 70000],
    "Years_Experience": [3, 5, 8, 4, 6]
}

df_employees = pd.DataFrame(employee_data)
print("\nEmployee Data:")
print(df_employees)

# Attach data to AI
ai.attach_data(df_employees)
print("\n✓ Data attached to AI context")

# Query 1: Who has highest salary?
print("\nQuery 1: Who has the highest salary?")
response = ai.ask("Who has the highest salary?", with_history=False)
print(f"Answer: {response}")

# Query 2: Average by department
print("\nQuery 2: What is the average salary by department?")
response = ai.ask("What is the average salary by department?", with_history=False)
print(f"Answer: {response}")

# Query 3: Analysis
print("\nQuery 3: Provide insights about this employee data")
response = ai.ask(
    "Analyze this employee data and provide 3 key insights",
    with_history=False
)
print(f"Answer: {response}")

# Example 2: Sales Data
print("\n" + "="*60)
print("Example 2: Analyzing Sales Performance")
print("="*60)

sales_data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Units_Sold": [150, 500, 300, 200, 450],
    "Price": [1200, 25, 75, 350, 150],
    "Revenue": [180000, 12500, 22500, 70000, 67500]
}

df_sales = pd.DataFrame(sales_data)
print("\nSales Data:")
print(df_sales)

# Create new AI instance for sales
ai_sales = AIHelper(model_name='Llama-3.1', display_response=False)
ai_sales.attach_data(df_sales)

# Query sales data
print("\nQuery: Which products should we focus on?")
response = ai_sales.ask(
    "Based on revenue and units sold, which products should we focus on for marketing?",
    with_history=False
)
print(f"Answer: {response}")

# Example 3: Multiple DataFrames
print("\n" + "="*60)
print("Example 3: Multiple DataFrames")
print("="*60)

# Customer satisfaction data
satisfaction_data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Rating": [4.5, 4.2, 4.7, 4.3, 4.6],
    "Reviews": [1250, 3200, 1800, 950, 2100]
}

df_satisfaction = pd.DataFrame(satisfaction_data)
print("\nCustomer Satisfaction Data:")
print(df_satisfaction)

# Attach both datasets
ai_multi = AIHelper(model_name='Llama-3.1', display_response=False)
ai_multi.attach_data(df_sales)
ai_multi.attach_data(df_satisfaction)

print("\n✓ Multiple datasets attached")

print("\nQuery: Combine sales and satisfaction data for recommendations")
response = ai_multi.ask(
    "Considering both sales revenue and customer ratings, which product represents the best opportunity?",
    with_history=False
)
print(f"Answer: {response}")

print("\n✅ All data analysis examples completed!")
