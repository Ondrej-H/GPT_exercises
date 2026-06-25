def ask_positive_int(subject: str) -> int:
    while True:
        print()
        user_input = input(f"{subject} (positive whole number, Enter = 1): ")
        if user_input == "":
            user_input = 1
            print(f"{subject} was set to 1")
            return user_input

        if user_input.isdigit():
            user_input = int(user_input)

            if user_input >= 1:
                print(f"{subject} was successfully set to {user_input}.")
                return user_input

            else:
                print("Invalid input! Input must be positive whole number!")

        else:
            print("Invalid input! Input must be positive whole number!")


# test ask_positive_int
print(ask_positive_int("HP"))
