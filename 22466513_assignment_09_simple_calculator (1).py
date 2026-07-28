def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Return a / b rounded to 2 decimal places, or None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return a % b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def exponent(a, b):
    return a ** b


def format_number(number):
    """Format a number without a trailing '.0' for whole values."""
    if number == int(number):
        return str(int(number))
    return str(number)


def get_two_numbers():
    """Prompt for two numbers and return them as floats, or None on bad input."""
    try:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None


def perform_operation(choice):
    """Ask for two numbers and print the result of the chosen operation."""
    numbers = get_two_numbers()
    if numbers is None:
        return
    a, b = numbers

    operations = {
        "1": (add, "+"),
        "2": (subtract, "-"),
        "3": (multiply, "*"),
        "4": (divide, "/"),
        "5": (modulus, "%"),
        "6": (exponent, "**"),
    }

    func, symbol = operations[choice]
    result = func(a, b)

    if result is None:
        if choice == "4":
            print("Error: Cannot divide by zero.")
        else:
            print("Error: Cannot perform modulus with zero.")
        return

    print(f"Result: {format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")


def print_menu():
    """Display the calculator menu."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        print_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in ("1", "2", "3", "4", "5", "6"):
            perform_operation(choice)
        else:
            print("Error: Please choose a number between 1 and 7.")

        print()


if __name__ == "__main__":
    main()
