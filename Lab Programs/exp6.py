"""Program 6: Simple bigram language model for text generation."""
from collections import defaultdict, Counter
import random
import re

corpus = input("Enter a short training sentence: ").strip()
if not corpus:
    corpus = "the cat sat on the mat the cat ate fish the dog sat on the rug"
tokens = re.findall(r"\b\w+\b|[.!?]", corpus.lower())
if len(tokens) < 2:
    raise SystemExit("Please enter at least two tokens.")

bigrams = defaultdict(Counter)
for current, nxt in zip(tokens, tokens[1:]):
    bigrams[current][nxt] += 1

random.seed(7)
current = tokens[0]
generated = [current]
for _ in range(20):
    choices = bigrams.get(current)
    if not choices:
        break
    next_tokens = list(choices.keys())
    weights = list(choices.values())
    current = random.choices(next_tokens, weights=weights, k=1)[0]
    generated.append(current)
    if current in {".", "!", "?"}:
        break
print("Training text:", corpus)
print("Generated text:", " ".join(generated).replace(" .", ".").replace(" !", "!").replace(" ?", "?"))
