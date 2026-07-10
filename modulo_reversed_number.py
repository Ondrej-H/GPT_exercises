n = 1234
reversed_number = 0

while n > 0:
    print(f"n = {n}")
    print(f"Poslední číslice (n % 10): {n % 10}")
    print(f"reversed_number před: {reversed_number}")

    reversed_number = reversed_number * 10 + n % 10

    print(f"reversed_number po:  {reversed_number}")

    n //= 10

    print(f"n po //= 10: {n}")
    print("-" * 30)

print(f"Výsledek: {reversed_number}")