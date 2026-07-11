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

# sum_digits(num: int) -> int

# reverse_number(num: int) -> int

# is_palindrome(num: int) -> bool

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