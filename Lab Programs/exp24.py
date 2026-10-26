"""Program 24: Rule-based dialog act recognition."""
import re

def classify_utterance(text):
    t = text.strip().lower()
    if not t:
        return "EMPTY"
    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", t):
        return "GREETING"
    if re.search(r"\b(thank you|thanks|thank)\b", t):
        return "THANKING"
    if re.search(r"\b(bye|goodbye|see you)\b", t):
        return "GOODBYE"
    if re.search(r"\b(please|could you|can you|would you)\b", t):
        return "REQUEST"
    if t.endswith("?") or re.match(r"^(who|what|when|where|why|how|is|are|do|does|did|can)\b", t):
        return "QUESTION"
    if re.search(r"\b(yes|yeah|correct|sure|okay)\b", t):
        return "AFFIRMATION"
    if re.search(r"\b(no|nope|incorrect|not really)\b", t):
        return "NEGATION"
    return "STATEMENT"

utterance = input("Enter a dialog utterance: ").strip() or "Could you help me, please?"
print("Utterance:", utterance)
print("Dialog act:", classify_utterance(utterance))
