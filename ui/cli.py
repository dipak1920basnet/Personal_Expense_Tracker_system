from services.manager import ExpenseManager
from domain.expense import Expense
def main():
    get_expense()

def get_expense():
    Apple_manager = ExpenseManager()
    continous_info(company_manager=Apple_manager)
    return Apple_manager

def add_data(data:list):
    return Expense(*data)

def info():
    data_info = []
    category = input("Enter Category:")
    amount = float(input("Enter amount: "))
    date = input("Enter a spent date: ")
    note = input("""
                Note Limit: 300
                Enter a Note (Optional): 
                """)
    data_info.append(amount)
    data_info.append(category)
    data_info.append(date)
    data_info.append(note)
    return data_info


def continous_info(company_manager):
    while True:
        datas = info()
        company_manager.add_expense(add_data(datas))
        print()
        print()
        print("Want to add more: ")
        more_info = input("""Enter: Y for yes
                                    N for No: """)
        
        if more_info.lower() == "y":
            continue
        else:
            break

if __name__ == "__main__":
    main()