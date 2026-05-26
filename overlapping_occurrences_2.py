"""
vypiš všechna tříznaková okénka
"""

text = "python"

for i in range(len(text) - 3 + 1):
    print(text[i:i + 3])


# ---------------------------------------------------
# obecná verze:
pattern = input()
window_size = len(pattern)

for i in range(len(text) - window_size + 1):
    current_window = text[i:i + window_size]