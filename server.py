from typing import Any, Callable, Dict, ForwardRef, Tuple, TypedDict, Union, List
from flask import Flask, jsonify, Response, request
from sqlite3 import Connection, connect, Cursor
from threading import Lock
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

class BadDB(Exception):
    def __init__(self, message: str = "The database supplied is not of the class DB") -> None:
        super().__init__(message)

# Classes
class DB:
    def __init__(self, database: Connection) -> None:
        self.db: Connection = database
        self.cursor: Cursor = self.db.cursor()
    
    def Execute(self, command: str, iter: List[Any] = ()) -> Cursor:
        x = self.cursor.execute(command, iter)
        self.db.commit()
        return x

"""
Promises:
    - fields will always be their hinted types
    - title will always be a valid ID in Names table
    - category will always be a valid ID in Categories table
    - location will always be a valid ID in Locations table
    - store will always be a valid store location

Not promised:
    - item will always exist in Items table
"""
class Item:
    def __init__(self, title: str, image: bytes, category: int, location: int, store: int, db: DB) -> None:
        # Promise 1
        if not isinstance(image, bytes): raise BadItem
        
        for v in [title, category, location, store]:
            if not isinstance(v, int): raise BadItem
        
        if not isinstance(db, DB): raise BadItem

        # Promises 2 and 3
        for (table, value) in {"title": title, "category": category, "location": location}.items():
            if len(db.Execute(f"SELECT id FROM {table} WHERE id = {value}").fetchall()) != 1: raise BadItem(f"Invalid {table}")

        # Promise 4
        if store > configs.MAX_STORE: raise BadItem("Invalid store")

        self._db: DB = db
        self._item: BaseItem = {
            "title": title,
            "image": image,
            "category": category,
            "location": location,
            "store": store
        }
    
    def lookup(self, table: str) -> str:
        return self._db.Execute(f"SELECT name FROM {table} WHERE id = {self._item[table]}").fetchall()[0][0]

    def __str__(self) -> str:
        inner: BaseItem = self._item
        category: str = self.lookup("category")
        title: str = self.lookup("title")
        location: str = self.lookup("location")
        return f"{category} {title} found in {location} currently stored in box {inner['store']}" # Change for category + location lookup
    
    def __repr__(self) -> str:
        return f"{self._item=}"
    
    def dict(self) -> Dict:
        return self._item
    
    def json(self) -> Response:
        return jsonify(self._item)

    def push(self) -> str:
        items: List[Tuple[str, Union[int, bytes]]] = [t for t in self._item.items()]

        tables: List[str] = [t[0] for t in items]
        values: List[Any] = [t[1] for t in items]

        query: str = f"INSERT INTO items ({', '.join(tables)}) VALUES ({', '.join(['?' for _ in enumerate(items)])})"
        self._db.Execute(query, values)

class ItemHandler:
    def __init__(self, db: DB) -> None:
        if not isinstance(db, DB): raise BadDB

        self._db = db
        self._items: List[BaseItem] = list()

    def pull(self, id: int) -> None:
        if not isinstance(id, int): raise InvalidInput

        # Not yet checked
        self._items.append(Item(self._db.Execute("SELECT * FROM items WHERE id = ?", id).fetchall()[0][1:]))


# Globals

conn: Connection = connect("lostProperty.db")
database: DB = DB(conn)

# Helper functions

def notify(message: str) -> None:
    msg = f"{message}" # Formatting here
    
    # Send message

def addItem(item: Item) -> None:
    if item is None: raise InvalidInput


# Routes

app = Flask(__name__)

@app.route("/photo")
def photoAPI():
    id = request.args.get("id")

if __name__ == "__main__":
    i = Item(1, bytes.fromhex("41"), 1, 1, 2, database)
    print(i)
    print(repr(i))
    print(i.dict())
    #print(i.push())

    print(database.Execute("SELECT * FROM items;").fetchall())