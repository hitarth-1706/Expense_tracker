print("Expense Tracker Starting...")
expenses = []
budget = 0

def add_expense():
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Invalid Amount")
        else:
            expenses.append((category, amount))
            print("Expense Added Successfully")

    except:
        print("Invalid Input")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses found")
    else:
        for item in expenses:
            print(item[0], item[1])

def category_total():
    totals = {}

    for item in expenses:
        cat = item[0]
        amt = item[1]

        if cat in totals:
            totals[cat] += amt
        else:
            totals[cat] = amt

    for key in totals:
        print(key, totals[key])

def show_menu():
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Category-wise Total")
    print("4. Set Monthly Budget")
    print("5. Check Budget Alert")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    if choice == "2":
        view_expenses()
    if choice == "3":
        category_total()

    if choice == "6":
        print("Thank You")
        break