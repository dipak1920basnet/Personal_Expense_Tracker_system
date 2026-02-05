from dateutil.parser import parse
from datetime import datetime, timedelta

class Expense:
    def __init__(self, amount, category, date, note=None):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Amount cannot be less than 0")

        self._amount = value

    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not value:
            raise ValueError("Category cannot be empty")
        
        self._category = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        try: 
            expense_date = datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Please enter a date")
        
        
        today = datetime.today().date()
        start_date = today - timedelta(days=10)
        end_date = today
            
        if not (start_date <= expense_date <= end_date):
            raise ValueError(f"Date must be between {start_date} and {end_date}")
        
        self._date = expense_date
    
    @property 
    def note(self):
        return self._note
    
    @note.setter
    def note(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError("The note must be in string")
            if len(value) > 300:
                    raise ValueError("Note limit is of 300 char")
        self._note = value

