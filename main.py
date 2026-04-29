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
    if choice == "6":
        print("Thank You")
        break