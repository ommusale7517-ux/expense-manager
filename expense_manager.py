import matplotlib.pyplot as plt

expenses = []

def add_expense():
    description = input("Enter Description: ")

    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Please enter a valid amount.")

    category = input("Enter Category (Food/Travel/Utilities): ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense Added Successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- Expense List -----")

    for expense in expenses:
        print(
            expense["description"],
            "| ₹", expense["amount"],
            "|", expense["category"]
        )


def show_summary():
    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense = ₹", total)


def show_graph():
    if len(expenses) == 0:
        print("No expenses available.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category not in summary:
            summary[category] = 0

        summary[category] += expense["amount"]

    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.bar(categories, amounts)

    plt.title("Expense Category Summary")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")

    plt.show()


while True:

    print("\n----- EXPENSE RECORDING SYSTEM ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Show Graph")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_summary()

    elif choice == "4":
        show_graph()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")