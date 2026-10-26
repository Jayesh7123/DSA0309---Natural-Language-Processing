"""Program 15: Probabilistic context-free grammar (PCFG) parsing."""
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'John' [0.4]
VP -> V NP [0.7] | V [0.3]
Det -> 'the' [0.5] | 'a' [0.5]
N -> 'cat' [0.5] | 'dog' [0.5]
V -> 'saw' [0.5] | 'runs' [0.5]
""")
parser = ViterbiParser(grammar)
sentence = input("Enter a sentence (e.g. John runs): ").strip() or "John runs"
trees = list(parser.parse(sentence.split()))
if trees:
    for tree in trees:
        print(tree)
        print("Probability:", tree.prob())
else:
    print("No parse found for this sentence using the supplied PCFG.")
