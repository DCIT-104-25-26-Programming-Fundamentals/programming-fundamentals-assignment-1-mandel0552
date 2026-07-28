def is_prime(number):
    """
    Return True if `number` is a prime number, False otherwise.

    A prime number is a whole number greater than 1 that has no
    divisors other than 1 and itself.
    """
    # Numbers less than 2 are never prime
    if number < 2:
        return False

    # 2 is the only even prime number
    if number == 2:
        return True

    # Eliminate other even numbers quickly
    if number % 2 == 0:
        return False

    # Check odd divisors up to the square root of the number.
    # If no divisor is found, the number is prime.
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


def main():
    # Get input from the user and convert it to an integer
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid whole number.")
        return

    # Call the function and print the appropriate result
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")


if __name__ == "__main__":
    main()
