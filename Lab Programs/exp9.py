"""Program 9: Rule-based POS tagging using regular expressions (NLTK)."""
import nltk
from nltk.tag import RegexpTagger

patterns = [
    (r".*ing$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*ly$", "RB"),
    (r".*(ous|ful|able|ive)$", "JJ"),
    (r"^(a|an|the)$", "DT"),
    (r"^(and|or|but)$", "CC"),
    (r"^(in|on|at|by|with|from)$", "IN"),
    (r".*s$", "NNS"),
    (r".*", "NN"),
]
tagger = RegexpTagger(patterns)
text = input("Enter a sentence: ").strip() or "The happy student is running quickly"
tokens = nltk.wordpunct_tokenize(text)
print("Word\tPOS tag")
for word, tag in tagger.tag(tokens):
    print(f"{word}\t{tag}")
