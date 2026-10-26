"""Program 7: Part-of-speech tagging with NLTK."""
import nltk

# NLTK data packages are downloaded by setup_nltk.py or can be downloaded below.
from nltk import word_tokenize, pos_tag

try:
    text = input("Enter a sentence: ").strip() or "The quick brown fox jumps over the lazy dog."
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    print("Word\tPOS tag")
    for word, tag in tagged:
        print(f"{word}\t{tag}")
except LookupError as exc:
    print("Required NLTK data is missing. Run: python setup_nltk.py")
    print(exc)
