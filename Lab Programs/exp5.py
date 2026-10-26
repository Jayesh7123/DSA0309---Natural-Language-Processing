"""Program 5: Porter stemming using NLTK."""
from nltk.stem import PorterStemmer

words = input("Enter words separated by spaces: ").split() or ["playing", "played", "plays", "studies", "happiness"]
stemmer = PorterStemmer()
for word in words:
    print(f"{word} -> {stemmer.stem(word)}")
