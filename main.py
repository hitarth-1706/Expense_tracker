print("Expense Tracker Starting...")
expenses = []
budget = 0

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

    if choice == "6":
        print("Thank You")
        break