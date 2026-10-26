"""Program 3: Basic morphological analysis using NLTK."""
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import wordpunct_tokenize

text = input("Enter a sentence: ").strip() or "The cats were running and played happily."
stemmer = PorterStemmer()
print("Word\t\tStem")
for word in wordpunct_tokenize(text):
    if word.isalpha():
        print(f"{word}\t\t{stemmer.stem(word)}")
