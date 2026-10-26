"""Optional menu to run one of the 26 programs."""
import subprocess
import sys
from pathlib import Path

files = sorted(Path(__file__).parent.glob("[0-9][0-9]_*.py"))
print("NLP Lab Programs")
for i, path in enumerate(files, 1):
    print(f"{i:2}. {path.name}")
choice = input("Enter program number (1-26): ").strip()
try:
    selected = files[int(choice) - 1]
except (ValueError, IndexError):
    raise SystemExit("Invalid choice.")
subprocess.run([sys.executable, str(selected)], check=False)
