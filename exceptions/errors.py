class InvalidexpenseError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error with value: {value}")
        # super() lets you call methods from the parent class without hardcoding the parent’s name

class StorageError(Exception):
    def __init__(self, value):
        self.args = value
        super().__init__(f"Error with value: {value}")



