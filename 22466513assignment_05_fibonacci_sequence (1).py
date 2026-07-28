def generate_fibonacci(n):
    """
    Return a list containing the first `n` numbers of the Fibonacci
    sequence, generated using a loop (no recursion).
    """
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def is_fibonacci(number):
    """
    Return True if `number` appears in the Fibonacci sequence,
    False otherwise. Uses a loop to generate terms up to `number`.
    """
    if number < 0:
        return False

    a, b = 0, 1
    while a < number:
        a, b = b, a + b

    return a == number


def print_first_n_terms():
    """Part A: ask for N and print the first N Fibonacci terms."""
    n_input = input("How many terms? ")

    try:
        n = int(n_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    sequence = generate_fibonacci(n)
    print("Fibonacci sequence: " + " ".join(str(term) for term in sequence))


def check_fibonacci_membership():
    """Part B: ask for a number and report whether it's a Fibonacci number."""
    number_input = input("Enter a number to check: ")

    try:
        number = int(number_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


def main():
    # Part A
    print_first_n_terms()

    print()

    # Part B
    check_fibonacci_membership()


if __name__ == "__main__":
    main()
