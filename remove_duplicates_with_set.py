def remove_duplicates(numbers: list):
    # Write code here
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


numbers = [1, 2, 2, 3, 4, 4, 5]

print(remove_duplicates(numbers))