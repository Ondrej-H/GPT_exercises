numbers = []

# 1) add_number()
def add_number(nums):
    num = input("Enter a number: ")
    if num.isdigit() or (len(num) > 1 and num[0] == "-" and num[1:].isdigit()):
        nums.append(float(num))
    else:
        print("Invalid input!")


# 2) Show basic statistics

# 2.1) Total numbers
#total_numbers = len(numbers)

# 2.2) Sum
def count_sum(nums):
    sum_of_nums = 0
    for num in nums:
        sum_of_nums += float(num)
    
    return sum_of_nums


# 2.3) Average
def count_average(nums):
    if len(nums) >= 1:
        average = count_sum(nums) / len(nums)
        return average
    
    


# 2.4) Highest
#highest = max(numbers)

# 2.5) Lowest
#lowest = min(numbers)

# 2.6) Sorted ascending
#ascending = sorted(numbers)

# 2.7) Sorted descending
#descending = sorted(numbers, reverse=True)


# 3) Show sequence analysis

# 3.1) First 3 nums
#first_3_nums = numbers[:3]

# 3.2) Last 3 nums
#last_3_nums = numbers[-3:]

# 3.3) Middle numbers               #[1, 5, 4, 3]
def extract_middle_nums(nums):
    if len(nums) % 2 == 1:
        middle_nums = nums[(len(nums) // 2) - 1 : (len(nums) // 2) + 2]

    elif len(nums) % 2 == 0:
        middle_nums = nums[(len(nums) // 2) - 1 : (len(nums) // 2) +1]

    return middle_nums


# 3.4) Reversed list
#reversed_list = numbers[::-1]

# 3.5) Every second
#every_second = numbers[::2]

# 3.6) Every third number from index 1
#every_third_from_index_1 = numbers[1::3]

# 3.7) Without first and last
#without_fist_and_last = numbers[1:-1]


# 4) Show special groups
# 4.1) Even nums
def extract_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)

    return evens


# 4.2) Odd nums
def extract_odds(nums):
    odds = []
    for num in nums:
        if num % 2 == 1:
            odds.append(num)

    return odds


# 4.3) Positive nums
def extract_positives(nums):
    positives = []
    for num in nums:
        if num > 0:
            positives.append(num)

    return positives



# 4.4) Negative nums
def extract_negatives(nums):
    negatives = []
    for num in nums:
        if num < 0:
            negatives.append(num)

    return negatives


# 4.5) Nums bigger than average
def extract_biggers_than_average(nums):
    average = count_average(nums)
    biggers_than_average = []
    for num in nums:
        if num > average:
            biggers_than_average.append(num)

    return biggers_than_average



# 5) Remove duplicates
def remove_duplicates(nums):
    no_duplicates = []
    for num in nums:
        if num not in no_duplicates:
            no_duplicates.append(num)

    return no_duplicates


# 6) Clear list
#numbers.clear()


# 7) Exit
"""if choice == 7:
    print("Goodbye!")
    break"""



print()
print("Welcome to Number Sequence Analyzer")
print()

menu_choice = None

while True:
    print("""
1 - Add number
2 - Show basic statistics
3 - Show sequence analysis
4 - Show special groups
5 - Remove duplicates
6 - Clear list
7 - Exit""")
    menu_choice = input("Choose: ")

    if menu_choice == "1":
        add_number(numbers)

    elif menu_choice == "2":
        print()
        print("BASIC STATISTICS:")
        if not numbers:
            print("The list of numbers is empty!")
        else:
            print(f"All numbers: {numbers}")
            print(f"Total numbers: {len(numbers)}")
            print(f"Sum: {count_sum(numbers)}")
            print(f"Average: {count_average(numbers)}")
            print(f"Highest: {max(numbers)}")
            print(f"Lowest: {min(numbers)}")
            print(f"Sorted ascending: {sorted(numbers)}")
            print(f"Sorted descending: {sorted(numbers, reverse=True)}")

    elif menu_choice == "3":
        print()
        print("SEQUENCE ANALYSIS:")
        print(f"First 3 numbers: {numbers[:3]}")
        print(f"Last 3 numbers: {numbers[-3:]}")
        print(f"Middle numbers: {extract_middle_nums(numbers)}")
        print(f"Reversed list: {numbers[::-1]}")
        print(f"Every second number: {numbers[::2]}")
        print(f"Every third number from index 1: {numbers[1::3]}")
        print(f"Without first and last: {numbers[1:-1]}")
    
    elif menu_choice == "4":
        print()
        print("SPECIAL GROUPS:")
        print(f"Even numbers: {extract_evens(numbers)}")
        print(f"Odd numbers: {extract_odds(numbers)}")
        print(f"Positive numbers: {extract_positives(numbers)}")
        print(f"Negative numbers: {extract_negatives(numbers)}")
        print(f"Numbers bigger than average: {extract_biggers_than_average(numbers)}")
        
    elif menu_choice == "5":
        print()
        print("LIST WITHOUT DUPLICATES:")
        print(remove_duplicates(numbers))

    elif menu_choice == "6":
        want_delete = input("""
              Are you sure you want to delete all the numbers from the list?
              If so, just press enter. If not, type "n" and then press enter.
              """)
        if want_delete == "":
            numbers.clear()
            print("All numbers were deleted.")
        else:
            print("Nothing was deleted.")
            pass
        
    elif menu_choice == "7":
        print("Goodbye!")
        break


    else:
        print("Invalid input!")



