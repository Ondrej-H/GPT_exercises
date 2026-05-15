
print()
print("Welcome to dice roll history!")
print("Enter a number or enter q to quit the program")

def count_average(lst):
    total = 0

    for element in lst:
        total += element
    if len(lst) >= 1:
        average = total / len(lst)
    else:
        average = None

    return average


user_input = None
rolls_list = []
while True:
    user_input = input("Enter your roll: ")
    if user_input == "q":
        break

    elif user_input.isdigit():
        rolls_list.append(int(user_input))

    else:
        print("Invalid input!")


average = count_average(rolls_list)

print(f"All rolls: {rolls_list}")
print(f"Last 3 rolls: {rolls_list[-3:]}")
print(f"Reversed: {rolls_list[::-1]}")
print(f"Every second roll: {rolls_list[::2]}")
if average is None:
    print(f"Average: No data")
else:
    print(f"Average: {average}")
