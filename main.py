from ui.cli import get_expense
from storage.json_storage import JsonStorage

JsonStorage.save(get_expense())

