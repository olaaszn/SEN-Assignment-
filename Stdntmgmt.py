import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def add_student(students):
    name = input("Enter student name: ")
    try:
        marks = float(input("Enter marks (0-100): "))
        grade = calculate_grade(marks)
        student = {
            "name": name,
            "marks": marks,
            "grade": grade
        }
        students.append(student)
        save_students(students)
        print("Student record added successfully!")
    except ValueError:
        print("Invalid marks input.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- STUDENT RECORDS ---")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Marks: {student['marks']}, Grade: {student['grade']}")


def main():
    students = load_students()

    while True:
        print("\n--- STUDENT GRADE MANAGEMENT ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
