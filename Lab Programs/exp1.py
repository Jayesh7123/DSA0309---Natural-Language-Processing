"""Program 1: Regular expressions - match and search patterns in text."""
import re

text = "Contact us at student@example.com or call 9876543210."
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
phone_pattern = r"\b\d{10}\b"

email = re.search(email_pattern, text)
phone = re.search(phone_pattern, text)

print("Text:", text)
print("Email found:", email.group() if email else "No email found")
print("Phone found:", phone.group() if phone else "No phone found")
print("Words starting with 'C':", re.findall(r"\bC\w*", text))
