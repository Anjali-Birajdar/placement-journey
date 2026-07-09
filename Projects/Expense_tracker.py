expenses = []
next_id = 1


def add_expense():
    global next_id
    category = input("Enter category: ")
    name = input("Enter expense name: ")

    while True:
        try:
            amount = float(input("Enter the amount spent: "))
            break
        except ValueError:
            print("Invalid amount.")
            print("Please enter a valid number.")

    expense = {
        "id": next_id,
        "category": category,
        "name": name,
        "amount": amount
    }
    expenses.append(expense)
    next_id += 1
    print(f"Expense added successfully! Expense ID: {expense['id']}")


def view_expenses():
    if len(expenses) == 0:
        print("No expense found.")
        return

    for expense in expenses:
        print("------------------------")
        print(f"ID: {expense['id']}")
        print(f"Category: {expense['category']}")
        print(f"Expense: {expense['name']}")
        print(f"Amount: ${expense['amount']}")


def total_expenses():
    if len(expenses) == 0:
        print("No expense found.")
        return

    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total expenses: ${total}")


def search_expense():
    while True:
        try:
            search_id = int(input("Enter Expense ID: "))
            break
        except ValueError:
            print("Please enter a valid ID.")
    found = False

    for expense in expenses:
        if expense["id"] == search_id:
            print(f"Expense: {expense['name']}")
            print(f"Amount: ${expense['amount']}")
            found = True
            break

    if not found:
        print("Expense not in database")


def remove_expense():
    while True:
        try:
            remove_id = int(input("Enter Expense ID to remove: "))
            break
        except ValueError:
            print("Please enter a valid ID.")
    found = False

    for expense in expenses:
        if expense["id"] == remove_id:
            expenses.remove(expense)
            print(f"Expense ID {remove_id} has been successfully removed!")
            found = True
            break

    if not found:
        print("Expense not found")


while True:
    print("---------- Expense Tracker ------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search Expense")
    print("5. Remove Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        remove_expense()
    elif choice == "6":
        print("Exited from the program")
        break
    else:
        print("Invalid choice")
