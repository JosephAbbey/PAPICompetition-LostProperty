"""
This module handles interactions with any sqlite3 databases.
"""

from typing import Any, List
import sqlite3
import io

from serverLib import exceptions

class DB:
    """
    The built-in database class for serverLib.
    
    Attributes:
        db (sqlite3.Connection): The raw sqlite3 database connection, used to commit changes.
        cursor (sqlite3.Cursor): A cursor generated from the sqlite3 connection.
    """
    
    def __init__(self, database: sqlite3.Connection) -> None:
        """
        The constructor for the DB class.
        
        Parameters:
            database (sqlite3.Connection): The raw sqlite3 database connection to be used.
        """
        
        self.db: sqlite3.Connection = database
        self.db.row_factory = sqlite3.Row
        self.cursor: sqlite3.Cursor = self.db.cursor()
    
    def Execute(self, query: str, *args: List[Any]) -> sqlite3.Cursor:
        """
        The method to execute queries, which may contain placeholders, on the stored database. 
        
        Parameters:
            query (str): The query to be executed.
            *args (List[Any]): The values to be substituted in for any ? placeholder characters in the query.
        
        Returns:
            sqlite3.Cursor: The results wrapped in a sqlite3 cursor object.
        """
        
        x = self.cursor.execute(query, args)
        self.db.commit()
        return map(list, x.fetchall())

    def ExecuteScript(self, script: io.TextIOWrapper) -> None:
        """
        The method to execute a script file on the stored database.
        
        Parameters:
            script (io.TextIoWrapper): The file to be ran.
        """
        
        self.db.executescript(script.read())
        self.db.commit()
    
class DBConfig:
    """
    A class for adding categories, locations, and titles to their respective tables.
    
    Attributes:
        _db (serverLib.database.DB): The internal database object.
    """

    def __init__(self, database: DB) -> None:
        """
        The constructor for the DBConfig class.
        
        Parameters:
            database (serverLib.database.DB): The database to configure.
        """
        
        if not isinstance(database, DB): raise exceptions.BadDB
        self._db: DB = database
        
    def __internalAdd(self, table: str, value: str) -> None:
        # The internal add method, not part of the public API
        
        if not (isinstance(table, str) and isinstance(value, str)): raise exceptions.InvalidInput
        self._db.Execute(f"INSERT OR IGNORE INTO {table} VALUES (?)", value)
        
    def addLocation(self, location: str) -> None:
        """
        The method to add a location to the database's `location` table.
        
        Parameters:
            location (str): The location to add.
        """
        
        self.__internalAdd("location", location)
        
    def addTitle(self, title: str) -> None:
        """
        The method to add a title to the database's `title` table.
        
        Parameters:
            title (str): The title to add.
        """
        
        self.__internalAdd("title", title)