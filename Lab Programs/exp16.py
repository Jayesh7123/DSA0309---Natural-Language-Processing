"""Program 16: Named Entity Recognition (NER) using spaCy."""
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise SystemExit(
        "spaCy English model is missing. Install it with:\n"
        "python -m spacy download en_core_web_sm"
    )

text = input("Enter text: ").strip() or "Apple hired John Smith in London on Monday."
doc = nlp(text)
print("Entity\t\tLabel\t\tExplanation")
for ent in doc.ents:
    print(f"{ent.text}\t\t{ent.label_}\t\t{spacy.explain(ent.label_) or ent.label_}")
if not doc.ents:
    print("No named entities found.")
