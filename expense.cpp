#include <iostream>
#include <string>
#include <ctime>    



class Expense{
private:

    struct ExpenseObject{
        std::time_t result = std::time(nullptr);
        char* dt = ctime(&result);
        //std::cout << std::ctime(&result);

        int id;
        std::string description;
        double amount;
        std::string date = dt;
    } expense_obj;
    
    
    

    public:
        Expense(){
            
        }
        void addExpense();
        void filterExpense(char filterExpenseType);

        void viewExpense();
        void loadExpenseFile();
        void saveExpenseFile();

        void budgetAlerts();

};

void Expense::addExpense(){
    ExpenseObject expense;
    std::cout << "Enter the description of the expense: ";
    std::cin >> expense.description;
    std::cout << "Enter the amount of the expense: ";
    std::cin >> expense.amount;
    std::cout << "Enter the date of the expense: ";
    std::cin >> expense.date;

    
}

void Expense::filterExpense(char filterExpenseType){
    int start_date;
    int end_date;
    char try_again = 'y';
    
    do{
        if(filterExpenseType == 'k'){ // filter by keyword
            std::cout << "Enter the keyword to filter by:" << std::endl;

            
            try_again = 'n'; // exit loop
        }
        else if(filterExpenseType == 'd'){ // filter by date range
            std::cout << "Enter the start date: to filter by:" << std::endl;
            std::cin >> start_date; // get start date
            std::cout << "Enter the end date to filter by:" << std::endl;
            std::cin >> end_date; // get end date


            try_again = 'n'; // exit loop
        }
        else{ // error message ask user to retry again
            std::cout << "Invalid filter type: Please try again :D!" << std::endl;
            try_again = 'y';
        }
    }while(try_again == 'y');
} // end of filterExpense function


/*
void Expense::viewExpense(){
    std::cout<<"TOTAL EXPENSES"<<endl;
    for (){
    
    }
    
}
*/
void Expense::loadExpenseFile(){}
void Expense::saveExpenseFile(){}
void Expense::budgetAlerts(){}
















