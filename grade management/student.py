student_grade = {}


# add a new student
def add_student(name,grade):
    student_grade[name] = grade
    print(f"{name} has been added with grade {grade}")


# update a student
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name}'s grade has been updated to {grade}")
    else:
        print(f"{name} is not in the student list")

# delete student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been deleted from the student list")
    else:
        print(f"{name} is not in the student list")


# view all students
def view_all_students():
    if not student_grade:
        print("No students in the list")
    else:
        for name, grade in student_grade.items():
            print(f"{name}: {grade}")


def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)

        elif choice == "2":
            name = input("Enter student name: ")
            grade = input("Enter new grade: ")
            update_student(name, grade)

        elif choice == "3":
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == "4":
            view_all_students()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

    
