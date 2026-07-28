def print_table(number):
    """Print the multiplication table for `number` from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        product = number * i
        print(f"{number}  x  {i:<2} =  {product}")


def print_tables_up_to(n):
    """Print the multiplication table for every number from 1 to n,
    separated by a dashed line between each table."""
    for number in range(1, n + 1):
        print_table(number)
        if number != n:
            print("-" * 30)


def run_single_table():
    """Part A: ask for a number and print its multiplication table."""
    number_input = input("Enter a number: ")

    try:
        number = int(number_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    print_table(number)


def run_range_of_tables():
    """Part B: ask for N and print tables for every number from 1 to N."""
    n_input = input("Enter a number (N): ")

    try:
        n = int(n_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print_tables_up_to(n)


def main():
    # Part A
    run_single_table()

    print()

    # Part B
    run_range_of_tables()


if __name__ == "__main__":
    main()
