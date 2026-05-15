"""
vrátí list s 5 prvky (v tomto pořadí):

 1) poslední 3 prvky
 2) otočený list
 3) každý druhý prvek
 4) list bez posledního prvku
 5) prostředek (bez prvního a posledního)
"""
def analyze_numbers(lst):
    list_analyzed = []

    # 1) last_3
    list_analyzed.append(lst[-3:])

    # 2) reversed
    list_analyzed.append(lst[::-1])

    # 3) every second
    list_analyzed.append(lst[::2])

    # 4) without last element
    list_analyzed.append(lst[:-1])

    # 5) without first and last
    list_analyzed.append(lst[1:-1])

    return list_analyzed


list1 = [10, 20, 30, 40, 50, 60]
print(analyze_numbers(list1))