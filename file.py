import json
from expense import Expense

class File:

    # method to save expenses to file
    @staticmethod
    def save_expense_file():
        try:
            with open("expenseList.json", "r") as file:
                exist_expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            exist_expenses = []

        new_expenses = [expense.dict for expense in Expense.expenses if expense.dict not in exist_expenses]
        if new_expenses:
            with open("expenseList.json", "w") as file:
                json.dump(exist_expenses + new_expenses, file)
                print("Expenses saved successfully.")
        else:
            print("No new expenses to save.")

    # method to load expenses from file
    @staticmethod

     # load expenses from file
    def load_expense_file():
        try:

            # load expenses from file
            with open("expenseList.json", "r") as file:
                anything = file.read().strip()
                if not anything:
                    print("No expenses available")
                    return

                # convert json string to list of dictionaries
                Expense.expenses = [Expense(**expense) for expense in json.loads(anything)]

        # file not found
        except FileNotFoundError:
            print("No expense file found.")
