"""Program 17: Access WordNet synsets and meanings using NLTK."""
from nltk.corpus import wordnet as wn

word = input("Enter a word: ").strip() or "bank"
synsets = wn.synsets(word)
if not synsets:
    print("No WordNet synsets found. Check spelling or run: python setup_nltk.py")
else:
    for syn in synsets[:10]:
        print(f"\nSynset: {syn.name()}")
        print("Definition:", syn.definition())
        print("Examples:", "; ".join(syn.examples()) or "None")
