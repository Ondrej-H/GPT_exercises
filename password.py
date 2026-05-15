"""
Zadání:

Program se ptá na heslo.
Správné heslo je:

python123

Dokud uživatel nezadá správné heslo, ptej se znovu.
Po 3 špatných pokusech napiš:
Access denied
a program skonči.

Pokud zadá správně:
Welcome
Bonus (volitelně):
Po každém špatném pokusu vypiš, kolik pokusů zbývá.
"""

# my solution
password = None
attempts_left = 3
while password != "python123" and attempts_left > 0:
    password = input("Password: ")
    attempts_left -= 1
    if password == "python123":
        print("Welcome!")
        break
    print(f"Attempts left: {attempts_left}")
    if attempts_left == 0:
        print("Access denied")


# GPT solution
password = ""
attempts_left = 3

while password != "python123" and attempts_left > 0:
    password = input("Password: ")

    if password == "python123":
        print("Welcome!")
        break

    attempts_left -= 1
    print(f"Attempts left: {attempts_left}")

if password != "python123":
    print("Access denied")