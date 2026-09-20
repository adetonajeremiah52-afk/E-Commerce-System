def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number")


def get_int_range(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Please enter a number between {min_value} and {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")


def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")