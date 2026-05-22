"""
Spočítej, kolikrát se v textu objeví: aa
"""

text = "aaaa"
pattern = "aa"
occurencies = 0

for i in range(len(text) + 1 - len(pattern)):
    if text[i:i + len(pattern)] == pattern:
        occurencies += 1
    

print(occurencies)