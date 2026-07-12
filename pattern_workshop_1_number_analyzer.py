# ANALYZE NUMBER 
# ask_positive_integer(prompt: str) -> int
def ask_positive_integer(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        if not user_input.isdigit():
            print("Invalid input: Input must be positive number!")

        else:
            positive_integer = int(user_input)
            
            if positive_integer <= 0:
                print("Invalid input: Input must be positive number!")

            else:                
                return positive_integer
            
# test ask_positive_integer()
'''print(ask_positive_integer("Positive integer: "))'''


# count_number_of_digits(num: int) -> int
def count_number_of_digits(num: int) -> int:
    number_of_digits = 0
    
    while num > 0:
        num //= 10
        number_of_digits += 1

    return number_of_digits

# test count_number_of_digits()
'''print(count_number_of_digits(1234))'''


# sum_digits(num: int) -> int
def sum_digits(num: int) -> int:
    digit_sum = 0

    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10

    return digit_sum

# test sum_digits()
'''print(sum_digits(1234))'''


# reverse_number(num: int) -> int
def reverse_number(num: int) -> int:
    reversed_number = 0
    while num > 0:
        reversed_number = reversed_number * 10 + num % 10
        num //= 10

    return reversed_number

# test reverse_number()
'''print(reverse_number(1234))'''


# is_palindrome(num: int) -> bool
def is_palindrome(num: int) -> bool:
    return num == reverse_number(num)
   
   
# analyze_number(num: int) -> dict
def analyze_number(num: int) -> dict:
    # validace <- ask_positive_integer()

    return {
        "number": num,
        "digit_count": count_number_of_digits(num),
        "digit_sum": sum_digits(num),
        "reversed_number": reverse_number(num),
        "is_palindrome": is_palindrome(num)
    }

# SHOW HISTORY
# show_history(analyzed_numbers: list[dict]) -> None
def show_history(analyzed_numbers: list[dict]) -> None:
    if not analyzed_numbers:
        print("History is empty.")
        return

    for analysis in analyzed_numbers:
        print("Number:", analysis["number"])
        print("Number of digits:", analysis["digit_count"])
        print("Sum of digits:", analysis["digit_sum"])
        print("Reversed number:", analysis["reversed_number"])
        print("Palindrome:", "Yes" if analysis["is_palindrome"] else "No")
        print()


# just for testing, TODO: comment or delete
analyzed_numbers = [
    analyze_number(1234),
    analyze_number(1221),
    analyze_number(567)
]

# STATISTICS
# count_number_of_analyzed_numbers(analyzed_numbers: list[dict]) -> int
def count_number_of_analyzed_numbers(
        analyzed_numbers: list[dict]
        ) -> int:
    
    return len(analyzed_numbers)

# test
'''print(count_number_of_analyzed_numbers(analyzed_numbers))'''


# find_largest_analyzed_number(analyzed_numbers: list[dict]) -> int | None
def find_largest_analyzed_number(
        analyzed_numbers: list[dict]
        ) -> int | None:
    
    if not analyzed_numbers:
        return None
    
    largest_analysis = max(
        analyzed_numbers,
        key=lambda analysis: analysis["number"]
        )

    largest_number = largest_analysis["number"]

    return largest_number


# find_smallest_analyzed_number(analyzed_numbers: list[dict]) -> int | None
def find_smallest_analyzed_number(
        analyzed_numbers: list[dict]
        ) -> int | None:
    
    if not analyzed_numbers:
        return None
    
    smallest_analysis = min(
        analyzed_numbers,
        key=lambda analysis: analysis["number"]
    )

    smallest_number = smallest_analysis["number"]

    return smallest_number


# calculate_average_value_of_analyzed_numbers(analyzed_numbers: list[dict]) -> float | None
def calculate_average_value_of_analyzed_numbers(
        analyzed_numbers: list[dict]
        ) -> float | None:
    
    if not analyzed_numbers:
        return None
    
    total_of_analyzed_numbers = sum(analysis["number"] for analysis in analyzed_numbers)

    average = total_of_analyzed_numbers / len(analyzed_numbers)

    return average


# count_numbers_with_even_digit_count(analyzed_numbers: list[dict]) -> int

# count_palindromes(analyzed_numbers: list[dict]) -> int

# show_statistics(analyzed_numbers: list[dict]) -> None
'''
Example Output:

Numbers analyzed: 7

Largest number:
Smallest number:

Average value:

Numbers with even digit count:
Palindrome count:
'''


'''
Pokud u něčeho při psaní zjistím,
že funkci ani nepotřebuji, tak ji samozřejmě psát nebudu.
'''






# 
'''
analyzed_numbers: list[dict] = [] # před menu

# pak při menu choice analyze number:
num = ask_positive_integer("Positive integer: ")
analysis = analyze_number(num)
analyzed_numbers.append(analysis)
'''


# menu
'''
=== Number Analyzer ===

1 - Analyze number
2 - Show history
3 - Statistics
4 - Exit
'''

'''
hlavní program provede:
analysis = analyze_number(number)
analyzed_numbers.append(analysis) # přidá do historie
'''

'''
analyze_number - Example Output:
Analyzing: 12321

Number of digits: 5
Sum of digits: 9
Reversed number: 12321
Palindrome: Yes
'''