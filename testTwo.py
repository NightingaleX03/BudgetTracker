# Command to Run Test File: python -m unittest testTwo.py

import unittest
from unittest.mock import patch
from expense import Expense

class TestExpenseTracker(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[
        'Telescope to see the stars <3', '750', '2025-01-01', 
    ])
    @patch('builtins.print')
    def test_expenses(self, mock_print, mock_input):

        Expense.expenses = []
        Expense.view_expenses()
        mock_print.assert_any_call('No expenses available')

        Expense.add_expense()
        Expense.view_expenses()
        mock_print.assert_any_call('ID: 1, Description: Telescope to see the stars <3, Amount: 750, Date: 2025-01-01')

        Expense.save_expense_file()
        Expense.load_expense_file()

        Expense.view_expenses()

if __name__ == '__main__':
    unittest.main()
