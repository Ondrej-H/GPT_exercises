"""
vrátí list s 5 prvky (v tomto pořadí):

 1) poslední 3 prvky
 2) otočený list
 3) každý druhý prvek
 4) list bez posledního prvku
 5) prostředek (bez prvního a posledního)
"""
def analyze_numbers(lst):
    return [
        lst[-3:],
        lst[::-1],
        lst[::2],
        lst[:-1],
        lst[1:-1]
    ]


list1 = [10, 20, 30, 40, 50, 60]
print(analyze_numbers(list1))