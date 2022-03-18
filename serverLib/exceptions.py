"""This module contains relevant exceptions for the serverLib library."""

class InvalidInput(Exception):
    """Indicates the input supplied to a class method or function was invalid."""
    
    def __init__(self, message: str = "Input was not valid") -> None:
        super().__init__(message)
        
class BadItem(Exception):
    """Similar to InvalidInput but specifically for cases where Item promises are broken by the supplied input."""
    
    def __init__(self, message: str = "One or more parameters broke the promises on Item") -> None:
        super().__init__(message)

class BadDB(Exception):
    """Similar to InvalidInput but specifically for cases where the serverLib.database.DB class was expected as input."""
    
    def __init__(self, message: str = "The database supplied is not of the class DB") -> None:
        super().__init__(message)