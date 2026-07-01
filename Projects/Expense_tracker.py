expenses = []


def add_expense():

    name = input("Enter expense name: ")
    amount = float(input("Enter the amount spent: "))

    expense = {"name": name, "amount": amount}

    print("Expense added!")

    expenses.append(expense)


def view_expenses():

    for expense in expenses:

        print("------------------------")
        print(f"Expense: {expense['name']}")
        print(f"Amount: ${expense['amount']}")

        if len(expenses) == 0:
            print("No expense found:")


def total_expenses():

    total = 0
    for expense in expenses:
        total += expense['amount']
        print(f"Total expenses: ${total}")

        if len(expenses) == 0:
            print("No expense found:")


def search_expense():

    search_name = input("Enter the name of the expense: ")
    found = False

    for expense in expenses:
        if expense['name'].lower() == search_name.lower():
            print(f"Expense: {expense['name']}")
            print(f"Amount: ${expense['amount']}")
            found = True
            break

        if not found:
            print("Expense not in database")


def remove_expense():

    expense_name = input("Enter the expense you wish to remove: ")
    found = False

    for expense in expenses:
        if expense['name'].lower() == expense_name.lower():
            expenses.remove(expense)
            print(f"{expense_name} has been successfully removed!")
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
