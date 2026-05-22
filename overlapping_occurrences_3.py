"""
najdi největší číslo v sousední dvojici
"""

lst = [1, 5, 2, 9, 3]

for i in range(len(lst) -2 + 1):
    if lst[i] > lst[i + 1]:
        print(lst[i])
    elif lst[i] < lst[i + 1]:
        print(lst[i + 1])
    else:
        print("equal")
