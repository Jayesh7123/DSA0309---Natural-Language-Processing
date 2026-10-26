"""Program 22: Simple rule-based reference (pronoun) resolution."""
import re

text = input("Enter a short text: ").strip() or "Alice went to the library. She borrowed a book. The book was interesting. It had pictures."
sentences = re.split(r"(?<=[.!?])\s+", text)
antecedents = []
pronouns = {"he", "she", "it", "they", "him", "her", "them"}
print("Text:", text)
for sentence in sentences:
    words = re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", sentence)
    replacements = []
    for word in words:
        if word.lower() in pronouns:
            candidate = next((noun for noun in reversed(antecedents)), None)
            replacements.append(f"{word} -> {candidate or 'antecedent not found'}")
    print("Sentence:", sentence)
    for replacement in replacements:
        print("  Reference:", replacement)
    # A lightweight heuristic: collect non-pronoun capitalized words and common nouns.
    for word in words:
        if word.lower() not in pronouns and word.lower() not in {"the", "a", "an", "and", "to", "was", "went", "borrowed", "had", "is", "are"}:
            antecedents.append(word)
