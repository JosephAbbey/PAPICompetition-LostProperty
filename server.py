from flask import Flask, jsonify, Response, request
from sqlite3 import Connection, connect, Cursor
from threading import Lock
from typing import Any, Callable, Dict, Tuple, TypedDict, Union, List
import configs

# Base classes and exceptions
class BaseItem(TypedDict):
    title: str
    photo: bytes
    category: int
    location: int
    store: int

class InvalidInput(Exception):
    def __init__(self, message: str = "Input was not valid") -> None:
        super().__init__(message)
        
class BadItem(Exception):
    def __init__(self, message: str = "One or more parameters broke the promises on Item") -> None:
        super().__init__(message)

# Classes
"""
Promises:
    - ExecuteAS and ExecuteIterAS will block any other execution on the database by threads using the same lock

Not promised:
    - ExecuteAS and ExecuteIterAS will block all other execution on the database
"""
class AtomSafeDB:
    def __init__(self, database: Connection) -> None:
        self.db = database
        self.cursor: Cursor = self.db.cursor()
        
    def generateLock(self) -> Lock:
        return Lock()
    
    def Execute(self, command: str) -> Any:
        return self.cursor.execute(command)
    
    def ExecuteAS(self, commands: List[str], lock: Lock) -> List[Any]:
        lock.acquire()
        results = []
        
        for command in commands:
            results.append(self.cursor.execute(command))
            
        lock.release()
        return results
    
    def ExecuteIterAS(self, function: Callable[[int, List[Any]], Union[Tuple[None, Any], str]], lock: Lock) -> Any:
        lock.acquire()
        step, results = 0, []
        
        while (x := function(step, results))[0] is not None:
            results.append(self.cursor.execute(x))
            step += 1
            
        lock.release()
        return x[1]
    
"""
Promises:
    - fields will always be their hinted types
    - category will always be a valid ID in Categories table
    - location will always be a valid ID in Locations table
    - store will always be a valid store location

Not promised:
    - title will always exist in Names table
    - item will always exist in Items table
"""
class Item:
    def __init__(self, title: str, photo: bytes, category: int, location: int, store: int, db: AtomSafeDB) -> None:
        # Promise 1
        if not isinstance(title, str): raise BadItem
        if not isinstance(photo, bytes): raise BadItem
        
        for v in [category, location, store]:
            if not isinstance(v, int): raise BadItem
            
        if not isinstance(db, AtomSafeDB): raise BadItem("db is not AtomSafeDB")
        
        # Promises 2 and 3
        for (table, value) in {"categories": category, "locations": location}.items():
            if len(db.Execute(f"SELECT id FROM {table} WHERE id = {value}")) != 1: raise BadItem(f"Invalid {table}")
        
        # Promise 4
        if store > configs.MAX_STORE: raise BadItem("Invalid store")
        
        self._item: BaseItem = {
            title: title,
            photo: photo,
            category: category,
            location: location,
            store: store
        }
    
    def __str__(self) -> str:
        inner: BaseItem = self._item
        return f"{inner.category} {inner.title} found in {inner.where} currently stored in box {inner.store}" # Change for category + location lookup
    
    def __repr__(self) -> str:
        return f"Item({self._item=})"
    
    def dict(self) -> Dict:
        return self._item
    
    def json(self) -> Response:
        return jsonify(self._item)

# Globals

database = connect("lostProperty.db")
ASDB = AtomSafeDB(database)
NamesLock = ASDB.generateLock()
ERowsLock = ASDB.generateLock()

"""
# Helper functions

def notify(message: str) -> None:
    msg = f"{message}" # Formatting here
    
    # Send message

def addItem(item: Item) -> None:
    if item is None: raise InvalidInput
    
# Flask

app = Flask(__name__)

@app.route("/photo")
def photoAPI():
    id = request.args.get("id")
"""

if __name__ == "__main__":
    i = Item("Gloves", bytes.fromhex("50"), 1, 1, 1, ASDB)
    print(i)