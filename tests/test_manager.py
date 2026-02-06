import pytest
from datetime import datetime, timedelta

from domain.expense import Expense
from services.manager import ExpenseManager 
from exceptions.errors import StorageError


def valid_date():
    return (datetime.today().date() - timedelta(days=1)).strftime("%Y-%m-%d")


@pytest.fixture
def manager():
    return ExpenseManager()


@pytest.fixture
def expense_food():
    return Expense(50, "Food", valid_date())


@pytest.fixture
def expense_transport():
    return Expense(30, "Transport", valid_date())


# ---------- INITIAL STATE ----------

def test_initial_state(manager):
    assert manager.expense_list == []
    assert manager.category_total == {}
    assert manager.total_spent == 0


# ---------- ADD EXPENSE ----------

def test_add_valid_expense(manager, expense_food):
    manager.add_expense(expense_food)

    assert len(manager.expense_list) == 1
    assert manager.category_total["Food"] == 50
    assert manager.total_spent == 50


def test_add_multiple_expenses_same_category(manager, expense_food):
    manager.add_expense(expense_food)
    manager.add_expense(Expense(20, "Food", valid_date()))

    assert manager.category_total["Food"] == 70
    assert manager.total_spent == 70


def test_add_multiple_categories(manager, expense_food, expense_transport):
    manager.add_expense(expense_food)
    manager.add_expense(expense_transport)

    assert manager.category_total["Food"] == 50
    assert manager.category_total["Transport"] == 30
    assert manager.total_spent == 80


# ---------- ERROR HANDLING ----------

def test_add_invalid_expense_raises_error(manager):
    with pytest.raises(StorageError):
        manager.add_expense("not an expense")


# ---------- TOTAL EXPENSE ----------

def test_total_expense_calculation(manager):
    expense_dict = {"Food": 40, "Transport": 60}
    total = manager.total_expense(expense_dict)

    assert total == 100


# ---------- TOTAL SPENT SAFETY ----------

def test_total_spent_never_negative(manager):
    manager.total_spent = -100
    assert manager.total_spent >= 0
