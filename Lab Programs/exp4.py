"""Program 4: Finite-state rule system to generate English noun plurals."""
import re

def pluralize(noun: str) -> str:
    lower = noun.lower()
    if re.search(r"[^aeiou]y$", lower):
        return noun[:-1] + ("IES" if noun.isupper() else "ies")
    if re.search(r"(s|x|z|ch|sh)$", lower):
        return noun + ("ES" if noun.isupper() else "es")
    if lower.endswith("fe"):
        return noun[:-2] + ("VES" if noun.isupper() else "ves")
    if lower.endswith("f") and lower not in {"roof", "belief", "chief"}:
        return noun[:-1] + ("VES" if noun.isupper() else "ves")
    return noun + ("S" if noun.isupper() else "s")

nouns = input("Enter nouns separated by commas: ").strip() or "cat,bus,baby,box,leaf"
for noun in [n.strip() for n in nouns.split(",") if n.strip()]:
    print(f"{noun} -> {pluralize(noun)}")
