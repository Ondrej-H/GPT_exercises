"""
dělitelné 2 → "Even"
dělitelné 5 → "Five"
obojí → "EvenFive"
obsahuje "5" (ale není dělitelné ani jedním) → "Almost Five"
jinak → číslo
"""

def check(num):
    if num % 2 == 0 and num % 5 == 0:
        return "EvenFive"
    
    elif num % 2 == 0:
        return "Even"
    
    elif num % 5 == 0:
        return "Five" 
    
    elif "5" in str(num):
        return "Almost Five"

    else:
        return str(num)
    

number = int(input())
for each_number in range(1, number + 1):
    print(check(each_number))