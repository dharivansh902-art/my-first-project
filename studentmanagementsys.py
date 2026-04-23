import json
import os

FILE_NAME = "students.json"

# Load data from file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "course": course
    }

    data.append(student)
    save_data(data)
    print("✅ Student added successfully!")

# View all students
def view_students():
    data = load_data()
    if not data:
        print("❌ No records found.")
        return
    
    print("\n--- Student Records ---")
    for student in data:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Course: {student['course']}")

# Search student
def search_student():
    data = load_data()
    roll = input("Enter Roll Number to search: ")

    for student in data:
        if student["roll"] == roll:
            print("✅ Found:", student)
            return
    print("❌ Student not found.")

# Update student
def update_student():
    data = load_data()
    roll = input("Enter Roll Number to update: ")

    for student in data:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")
            save_data(data)
            print("✅ Updated successfully!")
            return
    print("❌ Student not found.")

# Delete student
def delete_student():
    data = load_data()
    roll = input("Enter Roll Number to delete: ")

    for student in data:
        if student["roll"] == roll:
            data.remove(student)
            save_data(data)
            print("✅ Deleted successfully!")
            return
    print("❌ Student not found.")

# Main menu
def main():
    while True:
        print("\n==== Student Data Management System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

# Run program
if __name__ == "__main__":
    main()