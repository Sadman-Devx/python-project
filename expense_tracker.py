# Expense Tracker: A program that allows users to track their expenses and generate reports.
import json
import os 

DATA_FILE = 'expenses.json'
def load_expenses():
    """Load expenses from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []
def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)
def add_expense(expenses):
    """Add a new expense."""
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")
def view_expenses(expenses):
    """View all expenses."""
    if not expenses:
        print("No expenses recorded.")
        return
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['date']} - {expense['category']} - ${expense['amount']:.2f} - {expense['description']}")

def generate_report(expenses):
    """Generate a simple expense report."""
    if not expenses:
        print("No expenses to report.")
        return
    total_expense = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total_expense:.2f}")
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        category_totals[category] = category_totals.get(category, 0) + expense['amount']
    print("Expenses by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

def main(): 
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            generate_report(expenses)
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
if __name__ == "__main__":
    main()
