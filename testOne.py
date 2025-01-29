#Command to Run Test File: python -m unittest testOne.py
import unittest
from unittest.mock import patch
from expense import Expense

class TestExpenseTracker(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[
        'Laptop my life is one mine', '500', '2021-01-01', 
        'Food cause food good', '100', '2021-01-01', 
        'Rent (why is it so expensive)', '2000', '2021-01-01', 
        '1'
    ])
    @patch('builtins.print')
    def test_expenses(self, mock_print, mock_input):

        Expense.expenses = []

        Expense.add_expense()
        Expense.add_expense()
        Expense.add_expense()

        Expense.view_expenses()

        mock_print.assert_any_call('ID: 1, Description: Laptop my life is one mine, Amount: 500, Date: 2021-01-01')
        mock_print.assert_any_call('ID: 2, Description: Food cause food good, Amount: 100, Date: 2021-01-01')
        mock_print.assert_any_call('ID: 3, Description: Rent (why is it so expensive), Amount: 2000, Date: 2021-01-01')

        Expense.save_expense_file()

        Expense.expenses = []
        Expense.load_expense_file()
        Expense.view_expenses()

if __name__ == '__main__':
    unittest.main()
