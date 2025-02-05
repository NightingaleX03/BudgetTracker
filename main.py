from expense import Expense
from budget import Budget
from file import File

word_art = r"""
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
                    $$/                                                                                                                          
"""

menu = r"""
┌───────────────────────────────────────────────────────┐
│ Please select from one of the following actions:      │
│     1. View Expenses                                  │
│     2. Filter Expenses                                │
│     3. Create Expense                                 │
│     4. Save to File                                   │
│     5. Load from File                                 │
│     6. Change Budget                                  │
│     7. Exit                                           │
└───────────────────────────────────────────────────────┘
"""

def main():
    print(word_art)
    # user sets budget
    Budget.set_budget()

    while True:
        choice = input(menu + "\nEnter choice: ")
        if not choice.isdigit() or int(choice) not in range(1, 8):
            print("Invalid choice, please try again.\n")
            continue

        choice = int(choice)

        #view expenses
        if choice == 1:
            Expense.view_expenses(Budget.check_budget)
        
        #filter expenses
        elif choice == 2:

            #filter by keyword or date range
            #print filter menu
            filter_choice = input("Select filter type:\n(k) By Keyword\n(d) By Date Range\n(c) By Category\nEnter choice: ").lower()
            if filter_choice in ['k', 'd', 'c']:
                #filter expenses function
                Expense.filter_expense(filter_choice, File.load_expense_file)
            else:
                print("Invalid filter choice.\n")

        #create expense
        elif choice == 3:
            Expense.add_expense()
            Budget.check_budget(Expense.expenses)
            print("Expense added successfully!\n")

        #save expenses to file
        elif choice == 4:
            File.save_expense_file()
            print("Expenses saved to file.\n")

        #load expenses from file
        elif choice == 5:
            File.load_expense_file()
            print("Expenses loaded from file.\n")

        #set budget
        elif choice == 6:
            Budget.set_budget()

        #exit bye bye <3
        elif choice == 7:
            print("Thank you for using Expense Tracker! Till next time! ❤️")
            break

        #invalid choice oh no!
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
