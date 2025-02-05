from typing_extensions import Self


from typing import Any


from datetime import datetime

class Expense:

    # list to store all expenses
    expenses = []

    # constructor
    def __init__(self, description, amount, category="other", date=None):
        self.description = description
        self.amount = amount
        self.category = category

        # if date is not provided, set it to current date
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    @property
    def dict(self) -> dict[str, Any | str]:
        # Convert the expense object to a dictionary
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    # method to add expense
    @staticmethod
    def add_expense():

         # get description, amount, date from user
        description = input("Enter description: ")
        amount = input("Enter amount: ")

        # validate amount
        while not amount.isdigit():
            amount = input("Invalid amount. Please enter a valid number: ")

        date = input("Enter date (YYYY-MM-DD) or leave blank for today's date: ")
        
        # date not selected use current date
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")

         # get category from user
        print("Please select a category:\n\t(f) Food\n\t(t) Transport\n\t(u) Utilities\n\t(r) Rent\n\t(o) Other\n")
        category = input("Enter choice: ").lower()
        category_mapping = {'f': 'food', 't': 'transport', 'u': 'utilities', 'r': 'rent', 'o': 'other'}
        category = category_mapping.get(category, 'other')

        # create an instance of Expense
        expense = Expense(description, amount, category, date)
        
        # append the expense to expenses list
        Expense.expenses.append(expense)

    # method to view expenses
    @staticmethod
    def view_expenses(budget_checker):
        if not Expense.expenses:
            print("No expenses available")
        else:
            for expense in Expense.expenses:
                print(f"Description: {expense.description}, Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}")

        budget_checker(Expense.expenses)

    # method to filter expenses
    @staticmethod
    def filter_expense(filter_choice, file_loader):
        file_loader()

        #  filter by keyword
        if filter_choice == 'k':
            keyword = input("Enter keyword: ")
            filtered_expenses = [expense for expense in Expense.expenses if keyword.lower() in expense.description.lower()]

         # filter by date range
        elif filter_choice == 'd':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            filtered_expenses = [expense for expense in Expense.expenses if start_date <= expense.date <= end_date]

        # filter by category
        elif filter_choice == 'c':
            category = input("Enter category (food, transport, utilities, rent, other): ").lower()
            filtered_expenses = [expense for expense in Expense.expenses if expense.category == category]

        # invalid filter choice
        else:
            print("Invalid filter choice.")
            return

        # error checking 
        if not filtered_expenses:
            print("No expenses found.")
        else:
            for expense in filtered_expenses:
                print(f"Description: {expense.description}, Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}")
