"""
DRY: do not repeat yourself


Student:
    name: str
    marks: list[int]


Features:
- fetch all students from the database
- add another yet student to the database
- retrieve the student by NAME. UI/UX issues...
"""
from typing import Optional

COMMANDS = ("quit", "show", "retrieve", "add")
next_id = 1

# Simulated database
students = [
    {
        "name": "John Doe",
        "marks": [4, 5, 1, 4, 5, 2, 5],
        "info": "John is 22 y.o. Hobbies: music",
    },
    {
        "name": "Marry Black",
        "marks": [4, 1, 3, 4, 5, 1, 2, 2],
        "info": "John is 23 y.o. Hobbies: football",
    },
]


# def find_student(name: str) -> dict | None:
#     for student in students:
#         if student["name"] == name:
#             return student
#
#     return None


def show_students() -> None:
    print("=" * 20)
    if not students:
        print("No students in the database.")
        print("=" * 20)
        return

    print("The list of students:\n")
    for student in students:
        print(f"{student['name']}. Marks: {student['marks']}")

    print("=" * 20)


def show_student(student_id: int) -> None:
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        print(f"There is no student with ID {student_id}.")
        return

    print("Detailed about student:\n")
    print(
        f"{student['name']}. Marks: {student['marks']}\n"
        f"Details: {student['info']}\n"
    )


def add_student(name: str, details: Optional[str] = None) -> None:
    global next_id
    new_student = {"id": next_id, "name": name, "marks": [], "info": details if details else ""}
    students.append(new_student)
    next_id += 1
    print(f"Student {name} added with ID {new_student['id']}.")


def main() -> None:
    print(f"Welcome to the Digital journal!\nAvailable commands: {COMMANDS}")
    while True:
        user_input = input("Enter the command: ").strip().lower()

        if user_input not in COMMANDS:
            print(f"Command {user_input} is not available.\n")
            continue

        if user_input == "quit":
            print("See you next time.")
            break

        try:
            if user_input == "show":
                show_students()
            elif user_input == "retrieve":
                try:
                    student_id = int(input("Enter student ID: "))
                    show_student(student_id)
                except ValueError:
                    print("Invalid ID. Please enter a number.")

            elif user_input == "add":
                name = input("Enter student's name: ").strip()
                details = input("Enter additional details (optional): ").strip()
                add_student(name, details)

        except NotImplementedError as error:
            print(f"Feature '{error}' is not ready for live.")
        except Exception as error:
            print(error)


if __name__ == "__main__":
    main()