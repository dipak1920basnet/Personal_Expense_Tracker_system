from domain.expense import Expense
from exceptions.errors import InvalidexpenseError, StorageError

class ExpenseManager:
    def __init__(self):
        self.expense_list = []
        self.category_total = {} 
        self._total_spent = 0

    @property
    def total_spent(self):
        return self._total_spent
    
    @total_spent.setter
    def total_spent(self, value):
        if self._total_spent < 0:
            self._total_spent = 0
        else:
            self._total_spent = value
    
    def category_total_expense(self,expense_lists):
        for expense in expense_lists:
            try:
                self.category_total[expense.category] += expense.amount
            except KeyError:
                self.category_total[expense.category] = expense.amount

    def total_expense(self, expense_dict:dict):
        return sum(expense_dict.values())

    def add_expense(self, expense):
        if not isinstance(expense, Expense):
            raise StorageError
        else:
            self.expense_list.append(expense)
            self.category_total_expense(self.expense_list)
            self.total_spent = self.total_expense(self.category_total)
            