from model import Student

def menu():
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

while True: b 
    menu()

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")

        try:
            marks = float(input("Enter marks: "))
        except ValueError:
            print("Invalid marks.")
            continue

        s = Student(name, roll, marks)
        s.save()
        print("Student saved successfully.")

    elif choice == "2":
        Student.view_all()

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        Student.search(roll)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")