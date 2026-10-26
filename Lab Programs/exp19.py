"""Program 19: Word sense disambiguation using the simplified Lesk algorithm."""
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

def simplified_lesk(context, ambiguous_word):
    context_words = {
        w.lower() for w in re.findall(r"\b[a-zA-Z]+\b", context)
        if len(w) > 1
    }
    best_synset, best_score = None, -1
    for synset in wn.synsets(ambiguous_word):
        signature = set(re.findall(r"\b[a-zA-Z]+\b",
                                   synset.definition().lower()))
        for example in synset.examples():
            signature.update(re.findall(r"\b[a-zA-Z]+\b", example.lower()))
        score = len(context_words & signature)
        if score > best_score:
            best_synset, best_score = synset, score
    return best_synset, best_score

context = input("Enter a sentence containing an ambiguous word: ").strip() or "He deposited money at the bank"
word = input("Enter the ambiguous word: ").strip() or "bank"
result, score = simplified_lesk(context, word)
if result:
    print("Context:", context)
    print("Word:", word)
    print("Selected sense:", result.name())
    print("Definition:", result.definition())
    print("Overlap score:", score)
else:
    print("No WordNet senses found for this word. Run: python setup_nltk.py")
