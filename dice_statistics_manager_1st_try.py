"""
Dice Statistic Manager
----------------------

Po spuštění: "Welcome to Dice Statistics!"

Pak stále dokola:
1 - Add roll
2 - Show statistics
3 - Show special rolls
4 - Exit
Choose:

1 - Add roll - Povolené jsou pouze hodnoty: 1 až 6 -> uložit do listu.
    Jinak: "Invalid roll!" a znovu menu

2 - Show statistics - Pokud list není prázdný, vypiš:
All rolls: [...]
Total rolls: X
Average: X
Highest roll: X
Lowest roll: X
Last 3 rolls: [...]
Reversed rolls: [...]
Every second roll: [...]


3 - Show special rolls
Vypiš:
Kolik padlo:
šestek
jedniček

a také:
Lucky rolls:
Sem vypiš všechny hody:
které jsou sudé
NEBO jsou 5


4 - Exit - "Goodbye!"
"""

def count_average(list1):
    total = 0

    for element in list1:
        total += element

    average = total / len(list)
    
    return average


print()
print("Welcome to Dice Statistics!")

valid_rolls = list(range(1,7))
saved_rolls = []
total_rolls = 0
#print(type(valid_rolls))
"""if saved_rolls:              prázdný list po if vrací False
    print("List je plný")
else:
    print("List je prázdný")"""
x = 0
while x == 0:
    print("""
1 - Add roll
2 - Show statistics
3 - Show special rolls
4 - Exit
""")

    choice_menu = input("Choose: ")

    if choice_menu == "1":
        roll = input("Enter roll (1 - 6): ")
        
        if roll.isdigit():
            if int(roll) in valid_rolls:
                saved_rolls.append(int(roll))
        
        else:
            print("Invalid roll!")
            

    elif choice_menu == "2":
        if saved_rolls:
            for roll in saved_rolls:
                total_rolls += roll

    
    x += 1

print(saved_rolls)







print()