students = []

while True:
    print("\nChoose: (a)dd, (d)elete, (s)earch, (t)op, (v)iew, (q)uit")
    choice = input("Your choice: ")

    if choice == "a":
        name = input("Name: ")
        age = int(input("Age: "))
        grade = float(input("Grade: "))
        students.append({"name": name, "age": age, "grade": grade})
        print("Student added!")

    elif choice == "d":
        name = input("Enter name to delete: ")
        found = False
        for s in students:
            if s["name"].lower() == name.lower():
                students.remove(s)
                print("Student deleted!")
                found = True
                break
        if not found:
            print("Student not found!")

    elif choice == "s":
        name = input("Enter name to search: ")
        found = False
        for s in students:
            if s["name"].lower() == name.lower():
                print("Found:", s)
                found = True
                break
        if not found:
            print("Student not found!")

    elif choice == "t":
        if students:
            top = max(students, key=lambda x: x["grade"])
            print("Top student:", top)
        else:
            print("No students yet!")

    elif choice == "v":
        print("\nAll Students:")
        for s in students:
            print(s)

    elif choice == "q":
        break
