from typing import Any, List
import sqlite3

class DB:
    def __init__(self, database: sqlite3.Connection) -> None:
        self.db: sqlite3.Connection = database
        self.cursor: sqlite3.Cursor = self.db.cursor()
    
    def Execute(self, query: str, *args: List[Any]) -> sqlite3.Cursor:
        x = self.cursor.execute(query, args)
        self.db.commit()
        return x