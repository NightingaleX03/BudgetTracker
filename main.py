from expense import Expense
wordArt = r""" 
 ________                                                                    ________                                __                           
/        |                                                                  /        |                              /  |                          
$$$$$$$$/  __    __   ______    ______   _______    _______   ______        $$$$$$$$/   ______    ______    _______ $$ |   __   ______    ______  
$$ |__    /  \  /  | /      \  /      \ /       \  /       | /      \          $$ |    /      \  /      \  /       |$$ |  /  | /      \  /      \ 
$$    |   $$  \/$$/ /$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$$/ /$$$$$$  |         $$ |   /$$$$$$  | $$$$$$  |/$$$$$$$/ $$ |_/$$/ /$$$$$$  |/$$$$$$  |
$$$$$/     $$  $$<  $$ |  $$ |$$    $$ |$$ |  $$ |$$      \ $$    $$ |         $$ |   $$ |  $$/  /    $$ |$$ |      $$   $$<  $$    $$ |$$ |  $$/ 
$$ |_____  /$$$$  \ $$ |__$$ |$$$$$$$$/ $$ |  $$ | $$$$$$  |$$$$$$$$/          $$ |   $$ |      /$$$$$$$ |$$ \_____ $$$$$$  \ $$$$$$$$/ $$ |      
$$       |/$$/ $$  |$$    $$/ $$       |$$ |  $$ |/     $$/ $$       |         $$ |   $$ |      $$    $$ |$$       |$$ | $$  |$$       |$$ |      
$$$$$$$$/ $$/   $$/ $$$$$$$/   $$$$$$$/ $$/   $$/ $$$$$$$/   $$$$$$$/          $$/    $$/        $$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       
                    $$ |                                                                                                                          
                    $$ |                                                                                                                          
                    $$/                                                                                                                           """

menu = r"""
┌───────────────────────────────────────────────────────┐
│ Please select from one of the following actions:      │
│     1. View Expenses                                  │
│     2. Filter Expenses                                │
│     3. Create Expense                                 │
│     4. Save to File                                   │
│     5. Load from File                                 │
│     6. Exit                                           │
└───────────────────────────────────────────────────────┘
"""
def main():
    print(wordArt)

    while True:
        choice = ""
        while choice.isdigit() == False and choice not in ["1","2","3","4","5","6"]:
            #print menu
            print(menu)
            choice = input("Enter choice: ")

        choice = int(choice)

        #view expenses
        if (choice == 1):
            Expense.view_expenses()

        #filter expenses
        elif (choice == 2):
            filterChoice = ""

            #filter by keyword or date range
            choices = ['k', 'd']
            validChoice = False
            while not validChoice:
                #print filter menu
                print("Please select a filter type:\n\t(k) By Keyword\n\t(d) By Date Range\n")
                filterChoice = input("Enter choice: ")
                if filterChoice in choices:
                    validChoice = True
            #filter expenses function
            Expense.filter_expense(filterChoice);
            print("\n")
        
        #create expense
        elif (choice == 3):
            Expense.add_expense()
            print("Expense added successfully\n")

        #save to file
        elif (choice == 4):
            Expense.save_expense_file()
            print("Expenses saved to file\n")

        #load from file
        elif (choice == 5):
            Expense.load_expense_file()
            print("Expenses loaded from file\n")
        
        elif (choice == 6):
            print("Thank you for using Expense Tracker, Till next time! <3")
            break
        
        #invalid choice
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
