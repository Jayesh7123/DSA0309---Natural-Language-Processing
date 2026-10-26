"""Program 11: Top-down parser for a small context-free grammar."""
import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | 'John' | 'Mary'
VP -> V NP | V
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'ball'
V -> 'saw' | 'likes' | 'runs'
""")
parser = RecursiveDescentParser(grammar)
sentence = input("Enter a sentence (lowercase grammar words, or John/Mary): ").strip() or "John saw a cat"
tokens = sentence.split()
trees = list(parser.parse(tokens))
if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("No parse found for this sentence using the supplied grammar.")
