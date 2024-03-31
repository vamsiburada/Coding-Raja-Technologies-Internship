import os

# Function to record an expense
def record_expense(expenses):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"category": category, "amount": amount})

# Function to record income
def record_income(incomes):
    source = input("Enter income source: ")
    amount = float(input("Enter income amount: "))
    incomes.append({"source": source, "amount": amount})

# Function to calculate remaining budget
def calculate_budget(incomes, expenses):
    total_income = sum(income["amount"] for income in incomes)
    total_expenses = sum(expense["amount"] for expense in expenses)
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function to display expense analysis
def expense_analysis(expenses):
    categories = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        categories[category] = categories.get(category, 0) + amount

    print("Expense Analysis:")
    for category, amount in categories.items():
        print(f"{category}: {amount}")

# Function to save transactions to a file
def save_transactions(incomes, expenses):
    with open("transactions.txt", "w") as file:
        file.write("Incomes:\n")
        for income in incomes:
            file.write(f"{income['source']},{income['amount']}\n")
        file.write("\nExpenses:\n")
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")

# Function to load transactions from a file
def load_transactions():
    incomes = []
    expenses = []
    if os.path.exists("transactions.txt"):
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
            current_section = None
            for line in lines:
                if line.strip() == "Incomes:":
                    current_section = "Incomes"
                elif line.strip() == "Expenses:":
                    current_section = "Expenses"
                elif current_section == "Incomes":
                    source, amount = line.strip().split(",")
                    incomes.append({"source": source, "amount": float(amount)})
                elif current_section == "Expenses":
                    category, amount = line.strip().split(",")
                    expenses.append({"category": category, "amount": float(amount)})
    return incomes, expenses

# Main function
def main():
    incomes, expenses = load_transactions()

    while True:
        print("\n1. Record Expense")
        print("2. Record Income")
        print("3. Calculate Remaining Budget")
        print("4. Expense Analysis")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            record_expense(expenses)
        elif choice == "2":
            record_income(incomes)
        elif choice == "3":
            remaining_budget = calculate_budget(incomes, expenses)
            print(f"Remaining Budget: {remaining_budget}")
        elif choice == "4":
            expense_analysis(expenses)
        elif choice == "5":
            save_transactions(incomes, expenses)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
