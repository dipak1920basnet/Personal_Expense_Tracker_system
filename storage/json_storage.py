from pathlib import Path
import json
from services.manager import ExpenseManager
from domain.expense import Expense
import os 

file_path = "expense_storage.json"

def check_json(file_path):
    if file_path.exists():
        return True
    else:
        return False
    
def open_data(i:Expense):
    expense_info = {
            "amount":i.amount,
            "category":i.category,
            "date":i.date,
            "note":i.note}
    return expense_info

def parse_data(Expense:list):
    expenses = []
    for i in Expense:
        expenses.append(open_data(i))
    return expenses

class JsonStorage:

    @staticmethod
    def load():
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return {
                "expense": [],
                "category_total": {},
                "in_total_expense": 0
            }

        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {
                "expense": [],
                "category_total": {},
                "in_total_expense": 0
            }

    @staticmethod
    def save(expense_manager:ExpenseManager):
        stored_data = JsonStorage.load()

        # Append expenses:
        stored_data["expense"].extend(
            parse_data(expense_manager.expense_list)
        )
        
        stored_data["category_total"] = {}
        stored_data["in_total_expense"] = 0

    # RECOMPUTE totals from expense list
        for exp in stored_data["expense"]:
            category = exp["category"]
            amount = exp["amount"]
            stored_data["category_total"][category] = (
                stored_data["category_total"].get(category, 0) + amount
            )

        stored_data["in_total_expense"] = sum(stored_data["category_total"].values())

        with open("expense_storage.json","w") as f:
            json.dump(stored_data,f, indent=4)
        

