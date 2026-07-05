# 1. Z listu slov vytvoř list jejich prvních písmen.
words = ["bla", "polo", "bubu"]
initials = [word[0] for word in words]
print(initials)


# 2. Z listu čísel vytvoř list jejich druhých mocnin, ale jen lichých čísel.
numbers = [1, 2, 3, 4, 5, 6]

odd_squares = [num ** 2 for num in numbers if num % 2] # if num % 2 is same as if num % 2 != 0
print(odd_squares)


# 3. Z věty vytvoř list slov delších než 4 znaky (pomocí .split()).
sentence = "Takže i tohle je platné a dost pythonic."

words_longer_than_4 = [word for word in sentence.split() if len(word) > 4]
print(words_longer_than_4)


# next
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numbers = []

'''for row in matrix:
    for num in row:
        numbers.append(num)'''
    
numbers = [num for row in matrix for num in row]

print(numbers)