# This test case is generated with AI: 
import pytest
from datetime import datetime, timedelta

from domain.expense import Expense  
# ⬆️ replace `your_module_name` with the file name where Expense is defined


def valid_date():
    """Returns a valid date string within the allowed range."""
    return (datetime.today().date() - timedelta(days=1)).strftime("%Y-%m-%d")


# ---------- VALID CASE ----------

def test_expense_creation_success():
    expense = Expense(
        amount=100,
        category="Food",
        date=valid_date(),
        note="Lunch"
    )

    assert expense.amount == 100.0
    assert expense.category == "Food"
    assert expense.note == "Lunch"


# ---------- AMOUNT TESTS ----------

def test_amount_cannot_be_negative():
    with pytest.raises(ValueError):
        Expense(
            amount=-50,
            category="Food",
            date=valid_date()
        )


def test_amount_must_be_number():
    with pytest.raises(TypeError):
        Expense(
            amount="abc",
            category="Food",
            date=valid_date()
        )


# ---------- CATEGORY TESTS ----------

def test_category_cannot_be_empty():
    with pytest.raises(ValueError):
        Expense(
            amount=20,
            category="",
            date=valid_date()
        )


# ---------- DATE TESTS ----------

def test_invalid_date_format():
    with pytest.raises(ValueError):
        Expense(
            amount=20,
            category="Food",
            date="2024/01/01"
        )


def test_date_out_of_range():
    old_date = (datetime.today().date() - timedelta(days=20)).strftime("%Y-%m-%d")
    with pytest.raises(ValueError):
        Expense(
            amount=20,
            category="Food",
            date=old_date
        )


# ---------- NOTE TESTS ----------

def test_note_must_be_string():
    with pytest.raises(TypeError):
        Expense(
            amount=20,
            category="Food",
            date=valid_date(),
            note=123
        )


def test_note_length_limit():
    long_note = "a" * 301
    with pytest.raises(ValueError):
        Expense(
            amount=20,
            category="Food",
            date=valid_date(),
            note=long_note
        )


def test_note_optional():
    expense = Expense(
        amount=20,
        category="Food",
        date=valid_date()
    )
    assert expense.note is None
