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

"""2"""
#all_rolls
#total_rolls
#average
#highest
#lowest
#last_3_rolls
#reversed_rolls
#every_second

"""3"""
#count_sixes
#count_ones
#lucky_rolls - even AND 5s


"""2"""
#all_rolls (list)
all_rolls = []

#add roll
def add_roll(all_rolls, roll):
    if roll.isdigit() and 1 <= int(roll) <= 6:
        all_rolls.append(int(roll))

    else:
        print("Invalid roll!")


#number of rolls - len(all_rolls)


#total_rolls
def count_sum(all_rolls):
    total = 0
    
    for roll in all_rolls:
        total += roll
    
    return total
        

#average
def count_average(all_rolls):
    average = count_sum(all_rolls) / len(all_rolls)
    
    return average


#highest - max(all_rolls)
    
#lowest - min(all_rolls)

#last_3_rolls - all_rolls[-3:]

#reversed_rolls - all_rolls[::-1]

#every_second - all_rolls[::2]


"""3"""
#count_sixes
def count_sixes(all_rolls):
    sixes_count = 0
    
    for roll in all_rolls:
        if roll == 6:
            sixes_count += 1
    
    return sixes_count


#count_ones
def count_ones(all_rolls):
    ones_count = 0

    for roll in all_rolls:
        if roll == 1:
            ones_count += 1

    return ones_count


#lucky_rolls - even numbers and fives
def find_lucky_rolls(all_rolls):
    luckies = []
    
    for roll in all_rolls:
        
        if roll % 2 == 0 or roll == 5:
            luckies.append(roll)

    return luckies


print()
print("Welcome to Dice Statistics!")

while True:
    print("""
1 - Add roll
2 - Show statistics
3 - Show special rolls
4 - Exit
""")
    menu_choice = input("Choose: ")
    
    if menu_choice.isdigit():
        if 1 <= int(menu_choice) <= 4:

            # 1 - Add roll
            if menu_choice == "1":

                roll = input("Enter roll (1 - 6): ")
                add_roll(all_rolls, roll)
                # add_roll(list, roll) function do this:
                """if roll.isdigit() and 1 <= int(roll) <= 6:
                    all_rolls.append(roll)
                else:
                    print("Invalid roll!")"""

            # 2 - Show statistics
            elif menu_choice == "2":

                if all_rolls:
                    print(f"All rolls: {all_rolls}")
                    print(f"Number of rolls: {len(all_rolls)}")
                    print(f"Sum of rolls: {count_sum(all_rolls)}")
                    print(f"Average: {count_average(all_rolls)}")
                    print(f"Highest roll: {max(all_rolls)}")
                    print(f"Lowest roll: {min(all_rolls)}")
                    print(f"Last 3 rolls: {all_rolls[-3:]}")
                    print(f"Reversed rolls: {all_rolls[::-1]}")
                    print(f"Every second roll: {all_rolls[::2]}")
                
                else:
                    print("No rolls yet!")

            
            # 3 - Show special rolls
            elif menu_choice == "3":
                print(f"Number of sixes: {count_sixes(all_rolls)}")
                print(f"Number of ones: {count_ones(all_rolls)}")
                print(f"Lucky rolls: {find_lucky_rolls(all_rolls)}")


            # 4 - Exit
            elif menu_choice == "4":
                print("Goodbye!")
                break


        else:
            print("Invalid input!")
    else:
        print("Invalid input!")


