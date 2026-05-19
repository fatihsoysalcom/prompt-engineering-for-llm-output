import openai
import os

# In a real-world scenario, you would set your API key as an environment variable.
# For this example, we'll use a placeholder. Replace with your actual key.
# os.environ.get("OPENAI_API_KEY")
openai.api_key = os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY_HERE")

def get_llm_response(prompt):
    """Sends a prompt to the OpenAI API and returns the response."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# --- Prompt Optimization Example ---

# Scenario: We want to extract specific information from a text.

text_to_analyze = """
Apple Inc. announced its quarterly earnings today. Revenue was $94.8 billion, a 2% increase year-over-year. Net income was $24.2 billion. The company's CEO, Tim Cook, expressed optimism about future growth. The stock symbol is AAPL.
"""

# --- Less Optimized Prompt ---
# This prompt is direct but might not be specific enough for complex extractions.
print("--- Less Optimized Prompt ---")
less_optimized_prompt = f"Extract information from the following text: {text_to_analyze}"
response_less_optimized = get_llm_response(less_optimized_prompt)
print(f"Response: {response_less_optimized}\n")

# --- More Optimized Prompt ---
# This prompt uses clear instructions, specifies the desired output format (JSON),
# and lists the exact fields to extract. This is a key aspect of prompt engineering.
print("--- More Optimized Prompt ---")
more_optimized_prompt = f"""
Analyze the following text and extract the company name, CEO name, revenue, and stock symbol.
Return the information in JSON format with keys: 'company_name', 'ceo_name', 'revenue', 'stock_symbol'.

Text: {text_to_analyze}
"""
response_more_optimized = get_llm_response(more_optimized_prompt)
print(f"Response: {response_more_optimized}\n")

# --- Prompt with Role Playing ---
# Assigning a role can guide the model's tone and focus.
print("--- Prompt with Role Playing ---")
role_playing_prompt = f"""
Act as a financial analyst. Summarize the key financial highlights from the following text, focusing on revenue and net income.

Text: {text_to_analyze}
"""
response_role_playing = get_llm_response(role_playing_prompt)
print(f"Response: {response_role_playing}\n")

print("Note: Replace 'YOUR_API_KEY_HERE' with your actual OpenAI API key or set the OPENAI_API_KEY environment variable.")
