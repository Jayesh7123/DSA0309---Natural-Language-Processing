"""Download NLTK datasets used by these lab programs."""
import nltk

packages = [
    "punkt",
    "punkt_tab",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
    "wordnet",
    "omw-1.4",
    "stopwords",
]
for package in packages:
    try:
        print(f"Downloading/checking {package}...")
        nltk.download(package, quiet=False)
    except Exception as exc:
        print(f"Could not download {package}: {exc}")
print("NLTK data setup complete.")
