def read_matrix(rows, cols, label=""):
    """
    Prompt the user to enter `rows` lines, each containing `cols`
    space-separated numbers, and return the result as a 2D list.
    """
    matrix = []
    for r in range(1, rows + 1):
        while True:
            prompt = f"Enter row {r}{' of ' + label if label else ''}: "
            values = input(prompt).split()

            if len(values) != cols:
                print(f"Error: Expected {cols} values, got {len(values)}. Try again.")
                continue

            try:
                row = [float(v) for v in values]
            except ValueError:
                print("Error: Please enter valid numbers only. Try again.")
                continue

            matrix.append(row)
            break
    return matrix


def print_matrix(matrix, title=""):
    """Display `matrix` in a neat, aligned grid using nested loops."""
    if title:
        print(title)

    # Format every value first so we can find the widest one for alignment
    formatted = []
    for row in matrix:
        formatted_row = []
        for value in row:
            # Show whole numbers without a trailing ".0"
            if value == int(value):
                formatted_row.append(str(int(value)))
            else:
                formatted_row.append(f"{value:g}")
        formatted.append(formatted_row)

    width = 0
    for row in formatted:
        for value in row:
            if len(value) > width:
                width = len(value)

    for row in formatted:
        line = "  ".join(value.rjust(width) for value in row)
        print(line)


def transpose_matrix(matrix):
    """Return the transpose of `matrix` (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Build an empty cols x rows matrix, then fill it in
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """
    Return the matrix product of matrix_a (M x N) and matrix_b (N x P).
    Result is an M x P matrix.
    """
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])

    result = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def get_dimensions(label=""):
    """Prompt for and return (rows, cols) as positive integers."""
    while True:
        try:
            rows = int(input(f"Enter number of rows{' for ' + label if label else ''}: "))
            cols = int(input(f"Enter number of columns{' for ' + label if label else ''}: "))
        except ValueError:
            print("Error: Please enter valid whole numbers.")
            continue

        if rows <= 0 or cols <= 0:
            print("Error: Rows and columns must be positive integers.")
            continue

        return rows, cols


def run_transpose():
    rows, cols = get_dimensions()
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    result = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(result)


def run_addition():
    rows, cols = get_dimensions("Matrix A")
    print("\nMatrix A")
    matrix_a = read_matrix(rows, cols, "Matrix A")

    print("\nMatrix B must be the same size as Matrix A "
          f"({rows} x {cols}).")
    matrix_b = read_matrix(rows, cols, "Matrix B")

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)

    result = add_matrices(matrix_a, matrix_b)
    print("\nSum (A + B):")
    print_matrix(result)


def run_multiplication():
    print("Matrix A (M x N):")
    m, n = get_dimensions("Matrix A")
    matrix_a = read_matrix(m, n, "Matrix A")

    print(f"\nMatrix B must have {n} rows (to match Matrix A's columns).")
    p = int(input("Enter number of columns for Matrix B: "))
    matrix_b = read_matrix(n, p, "Matrix B")

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)

    result = multiply_matrices(matrix_a, matrix_b)
    print("\nProduct (A x B):")
    print_matrix(result)


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")

    choice = input("Choose an operation (1-3): ").strip()

    if choice == "1":
        run_transpose()
    elif choice == "2":
        run_addition()
    elif choice == "3":
        run_multiplication()
    else:
        print("Error: Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
