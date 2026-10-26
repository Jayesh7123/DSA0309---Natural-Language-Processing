"""Program 25: Text generation with an OpenAI GPT model.

Requires an API key in the OPENAI_API_KEY environment variable and internet access.
API usage may incur charges. Set OPENAI_MODEL to a model available to your account
if the default model name is unavailable.
"""
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(
        "OPENAI_API_KEY is not set. Set it in your environment before running.\n"
        "Windows PowerShell: $env:OPENAI_API_KEY='your_api_key'\n"
        "Do not put your key in source code or share it."
    )

client = OpenAI(api_key=api_key)
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
prompt = input("Enter a prompt for text generation: ").strip() or "Write a short paragraph about natural language processing."
try:
    response = client.responses.create(model=model, input=prompt)
    print("\nGenerated text:\n")
    print(response.output_text)
except Exception as exc:
    print("The API request failed:", exc)
    print("Check your API key, internet connection, model access, and API billing.")
