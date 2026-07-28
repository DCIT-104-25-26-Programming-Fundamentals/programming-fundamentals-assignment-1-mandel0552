def calculate_sum(numbers):
    """Return the sum of all values in `numbers` without using sum()."""
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    """Return the average of all values in `numbers`."""
    # Reuse calculate_sum() rather than recalculating the total manually
    return calculate_sum(numbers) / len(numbers)


def calculate_max(numbers):
    """Return the largest value in `numbers` without using max()."""
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest


def calculate_min(numbers):
    """Return the smallest value in `numbers` without using min()."""
    smallest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
    return smallest


def get_numbers(count):
    """Prompt the user for `count` numbers and return them as a list."""
    numbers = []
    for i in range(1, count + 1):
        user_input = input(f"Enter number {i}: ")
        numbers.append(float(user_input))
    return numbers


def main():
    # Get how many numbers the user wants to enter
    count_input = input("How many numbers? ")

    try:
        count = int(count_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    # N must be a positive integer
    if count <= 0:
        print("Error: The number of values must be a positive integer.")
        return

    # Collect the numbers from the user
    numbers = get_numbers(count)

    # Compute each statistic using its own function
    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    highest = calculate_max(numbers)
    lowest = calculate_min(numbers)

    # Display the results
    print("\nResults:")
    print(f"Sum:     {total:g}")
    print(f"Average: {average:g}")
    print(f"Maximum: {highest:g}")
    print(f"Minimum: {lowest:g}")


if __name__ == "__main__":
    main()
