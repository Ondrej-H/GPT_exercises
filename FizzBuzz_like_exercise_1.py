"""
dělitelné 4 → "Four"
dělitelné 6 → "Six"
obojí → "FourSix"
obsahuje "6" (ale není dělitelné 4 ani 6) → "Almost Six"
jinak → číslo
"""

def test(num):
    if num % 4 == 0 and num % 6 == 0:
        return "FourSix"

    if num % 4 == 0:
        return "Four"
    
    if num % 6 == 0:
        return "Six"
    
    if "6" in str(num):
        return "Almost Six"
    
    return str(num)

number = int(input())
for each_number in range(1, number + 1):
    print(test(each_number))

