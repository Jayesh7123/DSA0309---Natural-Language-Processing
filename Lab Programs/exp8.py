"""Program 8: Simple stochastic POS tagger using unigram tag probabilities."""
from collections import Counter, defaultdict
import re
import random

# Tiny labelled training corpus: (word, tag) examples.
training = [
    ("the", "DET"), ("a", "DET"), ("dog", "NOUN"), ("cat", "NOUN"),
    ("student", "NOUN"), ("runs", "VERB"), ("eats", "VERB"),
    ("likes", "VERB"), ("quickly", "ADV"), ("happy", "ADJ"),
    ("small", "ADJ"), ("blue", "ADJ"), ("in", "ADP"), ("on", "ADP"),
    ("is", "VERB"), ("and", "CONJ"), ("she", "PRON"), ("he", "PRON"),
    ("they", "PRON"), ("book", "NOUN"), ("read", "VERB")
]
tag_counts = defaultdict(Counter)
for word, tag in training:
    tag_counts[word][tag] += 1
global_tags = Counter(tag for _, tag in training)
random.seed(7)

def guess_tag(word):
    w = word.lower()
    if w in tag_counts:
        choices = list(tag_counts[w].keys())
        weights = [tag_counts[w][t] for t in choices]
        return random.choices(choices, weights=weights, k=1)[0]
    if w.endswith("ly"):
        return "ADV"
    if w.endswith(("ing", "ed")):
        return "VERB"
    if w.endswith(("ous", "ful", "ive", "able", "al")):
        return "ADJ"
    return global_tags.most_common(1)[0][0]

text = input("Enter a sentence: ").strip() or "The small dog runs quickly"
for word in re.findall(r"\b[\w']+\b|[^\w\s]", text):
    print(f"{word}\t{guess_tag(word)}")
