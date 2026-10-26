"""Program 23: Heuristic evaluation of text coherence using sentence similarity."""
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = input("Enter a paragraph (2 or more sentences): ").strip() or (
    "The weather was sunny today. The sun made the park warm. "
    "Many people enjoyed walking in the park."
)
sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
print("Sentences:", len(sentences))
if len(sentences) < 2:
    print("Please provide at least two sentences to evaluate coherence.")
else:
    matrix = TfidfVectorizer(stop_words="english").fit_transform(sentences)
    similarities = cosine_similarity(matrix)
    pair_scores = [similarities[i, i + 1] for i in range(len(sentences) - 1)]
    average = sum(pair_scores) / len(pair_scores)
    print("Adjacent sentence similarities:", [round(s, 3) for s in pair_scores])
    print(f"Average coherence proxy (cosine similarity): {average:.3f}")
    print("Note: This is a simple lexical-overlap proxy, not a full linguistic coherence model.")
