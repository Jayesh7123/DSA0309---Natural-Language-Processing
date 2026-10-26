"""Program 21: Extract noun phrases and simple semantic roles using spaCy."""
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise SystemExit("Install the spaCy model: python -m spacy download en_core_web_sm")

text = input("Enter a sentence: ").strip() or "The student reads a book in the library."
doc = nlp(text)
print("Noun phrases:")
for chunk in doc.noun_chunks:
    root = chunk.root
    print(f"- {chunk.text!r}: head={root.text!r}, lemma={root.lemma_!r}, dependency={root.dep_!r}")
print("\nVerbs and their syntactic arguments:")
for token in doc:
    if token.pos_ == "VERB":
        subjects = [child.text for child in token.children if child.dep_ in ("nsubj", "nsubjpass")]
        objects = [child.text for child in token.children if child.dep_ in ("dobj", "obj", "attr", "pobj")]
        print(f"- verb={token.lemma_}, subject={subjects or 'not identified'}, object={objects or 'not identified'}")
