# DSA03 – Natural Language Processing Lab Programs

This folder contains 26 Python programs corresponding to the supplied lab list.

## Recommended setup (VS Code, Windows)

1. Install Python 3.11 or 3.12 (recommended for broad package compatibility) and VS Code.
2. Extract this ZIP to a normal folder.
3. Open the extracted `NLP_Lab_Programs` folder in VS Code.
4. Open Terminal → New Terminal and create a virtual environment:

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   python setup_nltk.py
   python -m spacy download en_core_web_sm
   ```

   If PowerShell blocks activation, use Command Prompt terminal and run:
   ```bat
   .venv\Scripts\activate.bat
   ```

## Run a program

In the VS Code terminal, run one file at a time, for example:

```powershell
python 01_regular_expressions.py
python 07_pos_tagging_nltk.py
python 16_spacy_named_entity_recognition.py
```

You can also open a `.py` file and click **Run Python File**. Use the terminal so you can enter input.

## Programs

1. Regular expressions
2. Finite automaton accepting strings ending in `ab`
3. Morphological analysis using NLTK stemming
4. Finite-state-style noun plural generation
5. Porter stemming
6. Bigram text generation
7. NLTK part-of-speech tagging
8. Stochastic POS tagging (small demonstration model)
9. Rule-based POS tagging with regular expressions
10. Transformation-based tagging (simple transformation rule)
11. Top-down CFG parser
12. Earley CFG parser
13. CFG parse-tree generation
14. Grammar-based subject-verb agreement check
15. Probabilistic CFG parsing
16. spaCy named entity recognition
17. WordNet synsets and meanings
18. Simple FOPC expression parser
19. Simplified Lesk word-sense disambiguation
20. TF-IDF information retrieval
21. Syntax-driven semantic analysis using noun phrases and dependency roles
22. Heuristic reference resolution
23. Heuristic text-coherence evaluation
24. Rule-based dialog-act recognition
25. OpenAI API text generation (requires API key, internet, and may incur charges)
26. English-to-French machine translation with Hugging Face Transformers (downloads a model on first run)

## Important notes

- Programs 1, 2, 4, 6, 8, 10, 18, 22, and 24 use Python standard-library code and do not need external packages.
- Programs 3, 5, 7, 9, 11–15, 17, and 19 use NLTK. Run `python setup_nltk.py` once after installation.
- Programs 20 and 23 use scikit-learn.
- Programs 16 and 21 use spaCy and its `en_core_web_sm` language model.
- Program 25 requires an OpenAI API key and an API account with available usage. It is not a fully offline program, and API usage may cost money. The lab title says GPT-3, but the code uses the current OpenAI Python SDK and a configurable model (`OPENAI_MODEL`); model access depends on your account.
- Program 26 requires internet for initial model download and may need PyTorch. First model load can take time and disk space.
- Some NLP tasks here are intentionally small educational demonstrations, not production-grade linguistic systems. In particular, stochastic tagging, FOPC parsing, reference resolution, coherence scoring, and dialog-act recognition use simplified rules/models.
- Use a supported Python version such as 3.11 or 3.12. Very new Python versions may not yet be supported by all machine-learning dependencies.
