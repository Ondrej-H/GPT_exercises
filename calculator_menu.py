"""
Mini program 2 — Kalkulačka s menu

Procvičíš: while, if, převod na int, logiku programu

Zadání:

Program se stále ptá:

1 - Add
2 - Subtract
3 - Exit
Choose:

Chování:
Když uživatel zvolí 1
zeptá se na dvě čísla a vypíše součet.

Když zvolí 2
zeptá se na dvě čísla a vypíše rozdíl.

Když zvolí 3
program skončí:
Goodbye

Jiná volba:
Invalid choice
a menu znovu.
"""

choice = None
while True:
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Exit")
    choice = input("Choose: ")

    if choice == "1":
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))
        result = n1 + n2
        print(f"{n1} + {n2} = {result}")
    elif choice == "2":
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))
        result = n1 - n2
        print(f"{n1} - {n2} = {result}")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice")

