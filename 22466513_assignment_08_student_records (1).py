def calculate_average(scores):
    """Return the average of `scores`, rounded to 2 decimal places."""
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)


def format_score(score):
    """Format a score without a trailing '.0' for whole numbers."""
    if score == int(score):
        return str(int(score))
    return str(score)


def add_student(students):
    """Ask for a student's name, ID, and scores, then save the record."""
    name = input("Student name: ")
    id_input = input("Student ID: ")

    try:
        student_id = int(id_input)
    except ValueError:
        print("Error: Student ID must be a valid whole number.")
        return

    count_input = input("How many scores? ")
    try:
        count = int(count_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if count <= 0:
        print("Error: Number of scores must be a positive integer.")
        return

    scores = []
    for i in range(1, count + 1):
        score_input = input(f"Enter score {i}: ")
        try:
            score = float(score_input)
        except ValueError:
            print("Error: Scores must be valid numbers. Student not added.")
            return
        scores.append(score)

    student = {"name": name, "id": student_id, "scores": scores}
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Print a formatted table of every student's name, ID, scores, and average."""
    if not students:
        print("No students have been added yet.")
        return

    separator = "-" * 50
    print(separator)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print(separator)

    for student in students:
        scores_str = ", ".join(format_score(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{average}")

    print(separator)


def find_student_average(students):
    """Look up a student by ID and print their average score."""
    id_input = input("Enter student ID: ")

    try:
        student_id = int(id_input)
    except ValueError:
        print("Error: Please enter a valid ID number.")
        return

    for student in students:
        if student["id"] == student_id:
            average = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average}")
            return

    print("Error: No student found with that ID.")


def print_menu():
    """Display the student record system menu."""
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            find_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose a number between 1 and 4.")

        print()


if __name__ == "__main__":
    main()
