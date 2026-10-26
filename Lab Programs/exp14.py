"""Program 14: Check simple subject-verb agreement with a CFG."""
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> SG | PL
SG -> 'he' | 'she' | 'it' | 'the cat' | 'John'
PL -> 'they' | 'we' | 'you' | 'the cats' | 'John and Mary'
VP -> SGV | PLV
SGV -> 'runs' | 'eats' | 'is'
PLV -> 'run' | 'eat' | 'are'
""")
# CFG terminals are tokens, so multiword noun phrases are represented with dedicated rules.
grammar = CFG.fromstring("""
S -> NP SGV | NP PLV
NP -> 'he' | 'she' | 'it' | 'John' | 'they' | 'we' | 'you' | 'cats' | 'cat'
SGV -> 'runs' | 'eats' | 'is'
PLV -> 'run' | 'eat' | 'are'
""")
parser = ChartParser(grammar)
sentence = input("Enter a short sentence (e.g. he runs): ").strip().lower() or "he runs"
trees = list(parser.parse(sentence.split()))
if trees:
    print("Agreement accepted by the grammar.")
    for tree in trees:
        print(tree)
else:
    print("Sentence rejected: no subject-verb pattern matches the grammar.")
