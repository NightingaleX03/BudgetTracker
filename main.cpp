#include <iostream>
#include "expenseOptions.cpp"
#include "fileOptions.cpp"

int main() {
    std::string wordArt = R"(
________                                                                    ________                             __                           
|        \                                                                  |        \                           |  \                          
| $$$$$$$$ __    __   ______    ______   _______    _______   ______         \$$$$$$$$______   ______    _______ | $$   __   ______    ______  
| $$__    |  \  /  \ /      \  /      \ |       \  /       \ /      \          | $$  /      \ |      \  /       \| $$  /  \ /      \  /      \ 
| $$  \    \$$\/  $$|  $$$$$$\|  $$$$$$\| $$$$$$$\|  $$$$$$$|  $$$$$$\         | $$ |  $$$$$$\ \$$$$$$\|  $$$$$$$| $$_/  $$|  $$$$$$\|  $$$$$$\
| $$$$$     >$$  $$ | $$  | $$| $$    $$| $$  | $$ \$$    \ | $$    $$         | $$ | $$   \$$/      $$| $$      | $$   $$ | $$    $$| $$   \$$
| $$_____  /  $$$$\ | $$__/ $$| $$$$$$$$| $$  | $$ _\$$$$$$\| $$$$$$$$         | $$ | $$     |  $$$$$$$| $$_____ | $$$$$$\ | $$$$$$$$| $$      
| $$     \|  $$ \$$\| $$    $$ \$$     \| $$  | $$|       $$ \$$     \         | $$ | $$      \$$    $$ \$$     \| $$  \$$\ \$$     \| $$      
 \$$$$$$$$ \$$   \$$| $$$$$$$   \$$$$$$$ \$$   \$$ \$$$$$$$   \$$$$$$$          \$$  \$$       \$$$$$$$  \$$$$$$$ \$$   \$$  \$$$$$$$ \$$      
                    | $$                                                                                                                       
                    | $$                                                                                                                       
                     \$$                                                                                                                       
    )";
    std::cout << wordArt << std::endl;

    int choice;
    std::cout << "Please select from one of the following actions:\n1. View Expenses\n2.Filter Expenses\n3. Create Expense\n4.Create Budget" << std::endl;
    std::cin >> choice;

    if (choice == 1) {
        Expense::viewExpense();
    } else if (choice == 2) {
        char filterChoice;
        char choices[2] = {'k', 'd'};
        bool validChoice = false;
        while (!validChoice) {
            std::cout << "Please select a filter type:\n(k) By Keyword\n(d) By Date Range" << std::endl;
            std::cin >> filterChoice;
            for (char c : choices) {
                if (filterChoice == c) {
                    validChoice = true;
                    break;
                }
            }
        }
        Expense::filterExpense(filterChoice);
    } else if (choice == 3) {
        Expense::addExpense();
    } else if (choice == 4) {
        Expense::addBudget(); 
    }
    
}
