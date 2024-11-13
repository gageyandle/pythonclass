#imports locale library to format currency values
import locale
#sets the locale to US english currency
locale.setlocale(locale.LC_ALL, 'en_US')

# def main, collects inputs and adds expenses the subtracts from budget
# all using locale en_US

def main():
    print("A small program to calculate your monthly budget!")
    income = obtain_income()
    expenses = obtain_expenses()
    total_expenses = sum(expenses)
    remaining_budget = income - total_expenses
    print(f"Total Income: {locale.currency(income)}")
    print(f"Total Expenses: {locale.currency(total_expenses)}")
    print(f"Remaining Budget: {locale.currency(remaining_budget)}")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {locale.currency(expense)}")
    print("Completed by, Gage Yandle")

# collects the income and raises an error if value is below 0

def obtain_income():
    while True:
        try:
            income = float(input("Enter your monthly income: "))
            if income < 0:
                raise ValueError("Income cannot be a number above 0!")
            return income
        except ValueError as e:
            print(e)

# collects the expense and raises an error if value is below 0

def obtain_expenses():
    expenses = []
    while True:
        try:
            expense = float(input("Enter an expense amount (or 'stop' to finish): "))
            if expense < 0:
                raise ValueError("Expense cannot be negative.")
            expenses.append(expense)
        except ValueError as e:
            print(e)
        if input("Continue entering expenses? (y/n): ").lower() != 'y':
            break
    return expenses

if __name__ == "__main__":
    main()