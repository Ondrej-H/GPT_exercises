def test(n):
    print(f"Začátek: {n}")

    if n > 0:
        test(n - 1)

    print(f"Konec: {n}") # nedokončené průchody (zastavené rekurzivním voláním test(n - 1) se dokončí když n == 0)
'''
takže se vypíše i:
Konec: 1
Konec: 2
'''
test(2)