"""Program 2: Finite automaton that accepts strings ending in 'ab'."""
def accepts_ending_ab(value: str) -> bool:
    # State tracks the longest suffix that is also a prefix of "ab".
    state = 0  # 0: no match, 1: suffix 'a', 2: suffix 'ab' (accepting)
    for char in value:
        if state == 0:
            state = 1 if char == "a" else 0
        elif state == 1:
            if char == "a":
                state = 1
            elif char == "b":
                state = 2
            else:
                state = 0
        else:  # state == 2; next character may extend/change the suffix
            state = 1 if char == "a" else (2 if char == "b" else 0)
    return state == 2

sample = input("Enter a string using only a and b: ").strip()
if any(ch not in "ab" for ch in sample):
    print("Invalid input: use only 'a' and 'b'.")
else:
    print("Accepted" if accepts_ending_ab(sample) else "Rejected")
