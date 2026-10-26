"""Program 20: TF-IDF information retrieval and document ranking."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language used for data science.",
    "Natural language processing helps computers understand human language.",
    "Machine learning uses data to train predictive models.",
    "Information retrieval ranks documents based on a user's query.",
    "Python libraries support text analysis and natural language processing."
]
query = input("Enter a search query: ").strip() or "Python natural language processing"
vectorizer = TfidfVectorizer(stop_words="english")
matrix = vectorizer.fit_transform(documents + [query])
scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
ranked = sorted(enumerate(scores, start=1), key=lambda item: item[1], reverse=True)
print("Query:", query)
print("\nRanked documents:")
for rank, (doc_id, score) in enumerate(ranked, start=1):
    print(f"{rank}. Document {doc_id} (score={score:.3f}): {documents[doc_id - 1]}")
