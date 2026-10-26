"""Program 12: Earley parser for a context-free grammar."""
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | 'John' | 'Mary'
VP -> V NP | V
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'ball'
V -> 'saw' | 'likes' | 'runs'
""")
parser = EarleyChartParser(grammar)
sentence = input("Enter a sentence (e.g. John saw a cat): ").strip() or "John saw a cat"
trees = list(parser.parse(sentence.split()))
if trees:
    for tree in trees:
        print(tree)
else:
    print("No parse found for this sentence using the supplied grammar.")
