class InvalidInput(Exception):
    def __init__(self, message: str = "Input was not valid") -> None:
        super().__init__(message)
        
class BadItem(Exception):
    def __init__(self, message: str = "One or more parameters broke the promises on Item") -> None:
        super().__init__(message)

class BadDB(Exception):
    def __init__(self, message: str = "The database supplied is not of the class DB") -> None:
        super().__init__(message)