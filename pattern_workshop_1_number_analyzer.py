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
'''
Jak zajistíš validaci?

Co když zadá:
text?
záporné číslo?
nulu?


Example Output:
Analyzing: 12321

Number of digits: 5
Sum of digits: 9
Reversed number: 12321
Palindrome: Yes
'''

# show_history(analyzed_numbers: list[dict]) -> None

# count_number_of_analyzed_numbers(analyzed_numbers: list[dict]) -> int

# find_largest_analyzed_number(analyzed_numbers: list[dict]) -> int | None

# find_smallest_analyzed_number(analyzed_numbers: list[dict]) -> int | None

# calculate_average_value_of_analyzed_numbers(analyzed_numbers: list[dict]) -> float | None

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