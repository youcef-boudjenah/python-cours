expenses = []

while True:
    choice = input("\nChoose: (a)dd, (d)elete, (v)iew, (q)uit: ")

    if choice == "a":
        exp = input("Enter expense: ")
        expenses.append(exp)
        print("Added!")

    elif choice == "d":
        for e in enumerate(expenses):
            print(e)
        index = int(input("Enter index to delete: "))
        expenses.pop(index)
        print("Deleted!")

    elif choice == "v":
        print("\nExpenses:")
        for e in expenses:
            print("-", e)

    elif choice == "q":
        break
