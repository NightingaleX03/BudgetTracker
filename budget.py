class Budget:
    budget = 0

    # method to set budget
    @staticmethod
    def set_budget():

         # get budget from user
        budget_temp = input("Enter budget: ")
        while not budget_temp.isdigit():
            budget_temp = input("Invalid input. Please enter a numeric budget: ")
        Budget.budget = int(budget_temp)
        print(f"Budget set to {Budget.budget}")

     # method to check budget
    @staticmethod
    def check_budget(expenses):

        # calculate total expenses
        total = sum([int(expense.amount) for expense in expenses])
        print(f"Total expenses so far: {total}")

         # check if total expenses go over budget
        if total > Budget.budget:
            print("Please stop spending money! You have exceeded your budget!")
        
        # check if total expenses is below budget
        else:
            print("You are within your budget! Spend away!")

    # method to check total expenses from file
    @staticmethod
    def check_total_expenses(file_loader):

        # load expenses from file
        file_loader()
        from expense import Expense
        total_expenses = sum([int(expense.amount) for expense in Expense.expenses])
        print(f"Total expenses from file: {total_expenses}")
