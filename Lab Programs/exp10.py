"""Program 10: Demonstration of transformation-based tagging with a simple rule."""
import re

def initial_tag(word):
    w = word.lower()
    if w in {"the", "a", "an"}:
        return "DET"
    if w in {"is", "are", "was", "were", "run", "runs", "eat", "eats"} or w.endswith("ing"):
        return "VERB"
    return "NOUN"

def transform_tags(tokens):
    tags = [initial_tag(w) for w in tokens]
    # Transformation rule: change a noun to a verb if it follows "to".
    for i in range(1, len(tokens)):
        if tokens[i - 1].lower() == "to" and tags[i] == "NOUN":
            tags[i] = "VERB"
    return list(zip(tokens, tags))

text = input("Enter a sentence: ").strip() or "The students to study"
tokens = re.findall(r"\b[\w']+\b|[^\w\s]", text)
print("Initial tags and transformation rule result:")
for word, tag in transform_tags(tokens):
    print(f"{word}\t{tag}")
