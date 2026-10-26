"""Program 18: Simple FOPC (First-Order Predicate Calculus) parser."""
import re

TOKEN_RE = re.compile(r"\s*(forall|exists|->|[A-Za-z_]\w*|[(),.&~])")

def tokenize(expr):
    tokens, pos = [], 0
    while pos < len(expr):
        match = TOKEN_RE.match(expr, pos)
        if not match:
            if expr[pos:].strip() == "":
                break
            raise ValueError(f"Unexpected character at position {pos}: {expr[pos]!r}")
        tokens.append(match.group(1))
        pos = match.end()
    return tokens

def parse_expression(tokens):
    # Recursive-descent parser for atoms, negation, quantifiers, conjunction, implication.
    index = 0
    def parse_atom():
        nonlocal index
        if index < len(tokens) and tokens[index] == "~":
            index += 1
            return ("NOT", parse_atom())
        if index < len(tokens) and tokens[index] in ("forall", "exists"):
            quantifier = tokens[index]; index += 1
            if index >= len(tokens):
                raise ValueError("Expected variable after quantifier")
            variable = tokens[index]; index += 1
            body = parse_atom()
            return (quantifier.upper(), variable, body)
        if index < len(tokens) and tokens[index] == "(":
            index += 1
            expr = parse_implication()
            if index >= len(tokens) or tokens[index] != ")":
                raise ValueError("Expected ')'")
            index += 1
            return expr
        if index >= len(tokens) or not re.fullmatch(r"[A-Za-z_]\w*", tokens[index]):
            raise ValueError("Expected predicate or identifier")
        name = tokens[index]; index += 1
        args = []
        if index < len(tokens) and tokens[index] == "(":
            index += 1
            while index < len(tokens) and tokens[index] != ")":
                if tokens[index] != ",":
                    args.append(tokens[index])
                index += 1
            if index >= len(tokens):
                raise ValueError("Expected ')' after predicate arguments")
            index += 1
        return ("PRED", name, tuple(args))
    def parse_conjunction():
        nonlocal index
        left = parse_atom()
        while index < len(tokens) and tokens[index] == "&":
            index += 1
            left = ("AND", left, parse_atom())
        return left
    def parse_implication():
        nonlocal index
        left = parse_conjunction()
        if index < len(tokens) and tokens[index] == "->":
            index += 1
            return ("IMPLIES", left, parse_implication())
        return left
    result = parse_implication()
    if index != len(tokens):
        raise ValueError(f"Unexpected token: {tokens[index]}")
    return result

expression = input("Enter FOPC expression (e.g. forall x (Human(x) -> Mortal(x))): ").strip()
if not expression:
    expression = "forall x (Human(x) -> Mortal(x))"
try:
    print("Tokens:", tokenize(expression))
    print("Parse tree:", parse_expression(tokenize(expression)))
except ValueError as error:
    print("Invalid expression:", error)
