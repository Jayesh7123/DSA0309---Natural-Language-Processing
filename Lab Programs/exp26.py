"""Program 26: English-to-French machine translation using Hugging Face Transformers."""
from transformers import pipeline

MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"

def main():
    text = input("Enter English text to translate: ").strip() or "Hello, how are you?"
    print("Loading translation model (first run may download several files)...")
    translator = pipeline("translation", model=MODEL_NAME)
    result = translator(text, max_length=256)
    print("English:", text)
    print("French:", result[0]["translation_text"])

if __name__ == "__main__":
    main()
