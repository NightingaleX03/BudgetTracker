import json
from datetime import datetime

class Expense:

    #list to store all expenses
    expenses = []

    #constructor
    def __init__(self, expense_id, description, amount, date=None):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount

        #if date is not provided, set it to current date
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    #method to add expense
    @staticmethod
    def add_expense():
        expense_id = len(Expense.expenses) + 1

        #get description, amount, date from user
        description = input("Enter description: ")
        amount = input("Enter amount: ")
        date = input("Enter date (YYYY-MM-DD): ")

        #create an instance of Expense
        expense = Expense(len(Expense.expenses) + 1, description, amount, date)

        #append the expense to expenses list
        Expense.expenses.append(expense)

    #method to save expenses to file
    @staticmethod
    def view_expenses():

        #no expenses available
        if not Expense.expenses:
            print("No expenses available")

        #display all expenses
        else:
            for expense in Expense.expenses:
                print(f"ID: {expense.expense_id}, Description: {expense.description}, Amount: {expense.amount}, Date: {expense.date}")

    #method to save expenses to file
    @staticmethod
    def filter_expense(filter_choice):
        
        #load expenses from file
        Expense.load_expense_file()

        # Filter by keyword
        if filter_choice == 'k':
            keyword = input("Enter keyword: ")
            
            #filter expenses based on keyword
            filtered_expenses = [expense for expense in Expense.expenses if keyword.lower() in expense.description.lower()]

            #no expenses found
            if not filtered_expenses:
                print("No expenses found.")

            else:
                #display filtered expenses
                for expense in filtered_expenses:
                    print(f"ID: {expense.expense_id}, Description: {expense.description}, Amount: {expense.amount}, Date: {expense.date}")

        # Filter by date range
        elif filter_choice == 'd':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")

            #filter expenses based on date range
            filtered_expenses = [expense for expense in Expense.expenses if start_date <= expense.date <= end_date]

            #no expenses found
            if not filtered_expenses:
                print("No expenses found.")
            else:
                #display filtered expenses
                for expense in filtered_expenses:
                    print(f"ID: {expense.expense_id}, Description: {expense.description}, Amount: {expense.amount}, Date: {expense.date}")

    #method to save expenses to file
    @staticmethod
    def save_expense_file():
        try:
            #load existing expensesS
            with open("expenseList.json", "r") as file:
                exist_expenses = json.load(file)
        
        #if file not found or empty
        except (FileNotFoundError, json.JSONDecodeError):
            exist_expenses = []

        #save all expenses to file
        with open("expenseList.json", "w") as file:
            all_expenses = exist_expenses + [expense.__dict__ for expense in Expense.expenses]
            #write expenses to file
            json.dump(all_expenses, file)

    #method to load expenses from file
    @staticmethod
    def load_expense_file():
        try:
            #try to load expenses from file
            with open("expenseList.json", "r") as file:
                anything = file.read().strip();

                #if file is empty
                if not anything:
                    print("No expenses available")
                    return
                
                #load expenses from file
                Expense.expenses = [Expense(**expense) for expense in json.loads(anything)]
        
        #if file not found
        except FileNotFoundError:
            pass
