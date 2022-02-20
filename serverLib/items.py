from typing import Dict, List, Optional, Tuple, TypedDict, Union
import flask

from serverLib import configs, database, exceptions

class BaseItem(TypedDict): # DO NOT TOUCH
    title: int
    category: int
    photo: bytes
    location: int
    store: int

item_fields = Union[int, bytes]

"""
Promises:
    - fields will always be their hinted types
    - title, category, and location will be valid IDs in their respective tables
    - store will always be a valid store location

Not promised:
    - item will always exist in Items table
"""
class Item: # DO NOT CHANGE ITEM YOU WILL INSTANTLY REGRET IT
    def __init__(self, title: int, category: int, image: bytes, location: int, store: int, db: database.DB) -> None:
        # Promise 1
        if not isinstance(image, (bytes, type(None))):
            raise exceptions.BadItem("Promise 1 was broken")
        
        for v in [title, category, location, store]:
            if not isinstance(v, int):
                raise exceptions.BadItem("Promise 1 was broken")
        
        if not isinstance(db, database.DB):
            raise exceptions.BadItem("Promise 1 was broken")

        # Promises 2
        for (table, value) in {"title": title, "category": category, "location": location}.items():
            if len(db.Execute(f"SELECT id FROM {table} WHERE id = ?", value).fetchall()) != 1:
                raise exceptions.BadItem(f"Invalid {table} (Promise 2 was broken)")

        # Promise 3
        if store > configs.MAX_STORE:
            raise exceptions.BadItem("Invalid store (Promise 3 was broken)")

        self._db: database.DB = db
        self._item: BaseItem = { # DO NOT TOUCH, DON'T DO IT
            "title": title,
            "image": image,
            "category": category,
            "location": location,
            "store": store
        }
    
    def lookup(self, table: str) -> str:
        return self._db.Execute(f"SELECT name FROM {table} WHERE id = ?", self._item[table]).fetchall()[0][0]

    def __str__(self) -> str:
        inner: BaseItem = self._item
        
        category: str = self.lookup("category")
        title: str = self.lookup("title")
        location: str = self.lookup("location")
        
        return f"{category} {title} found in {location} currently stored in box {inner['store']}"
    
    def __repr__(self) -> str:
        return f"{self._item=}"
    
    def dict(self) -> Dict[str, item_fields]:
        return self._item
    
    def json(self) -> flask.Response:
        return flask.jsonify(self._item)
    
    def image(self) -> Optional[flask.Response]: # Generate a flask response containing the image
        if not (img := self._item.get("image")):
            return None
        
        response = flask.make_response(img)
        response.headers.set("Content-Type", "image/png")
        
        return response

class ItemHandler:
    def __init__(self, db: database.DB) -> None:
        if not isinstance(db, database.DB):
            raise exceptions.BadDB # Validate input

        self._db: database.DB = db
        self._items: List[BaseItem] = list()

    def pull(self, id: int) -> None: # Single Item pull by ID
        if not isinstance(id, int):
            raise exceptions.InvalidInput # Validate input

        query: str = "SELECT title, category, image, location, store FROM items WHERE id = ?"
        fields: List[item_fields] = self._db.Execute(query, id).fetchall()
        
        if not fields:
            raise exceptions.InvalidInput("Bad ID")
        
        i: Item = Item(*fields[0], self._db)

        self._items.append(i)

    def massPull(self, query: str, *args: List[any]) -> List[int]: # Multiple Item pull by condition
        if not isinstance(query, str):
            raise exceptions.InvalidInput # Validate input
        
        ids: List[Tuple(int, None)] = self._db.Execute(f"SELECT id FROM items WHERE {query}", *args) # Get IDs of rows which match the query
        ids = list(map(lambda x: x[0], ids)) # Get the IDs out of their tuples
        
        list(map(self.pull, ids)) # Get the full items and add them to the internal items list
        
        return ids
        
    def __str__(self) -> str:
        return ', '.join(list(map(str, self._items)))
       
    def __repr__(self) -> str:
        return f"{self._items=}"
    
    def items(self) -> List[Item]:
        return self._items
    
    def json(self) -> flask.Response:
        print(list(map(lambda x: x.dict(), self.items())))
        return flask.jsonify(list(map(lambda x: x.dict(), self.items()))) # Fix this!!!
