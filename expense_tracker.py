print("💰 Expense Tracker")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append((item, amount))
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added.")
        else:
            print("\nYour Expenses:")
            for item, amount in expenses:
                print(item, "-", amount)

    elif choice == "3":
        total = sum(amount for item, amount in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")