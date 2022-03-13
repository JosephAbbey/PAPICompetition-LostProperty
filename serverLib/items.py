"""
This module handles the storage of Items as well as methods relating to singular Items.
"""

from typing import Dict, List, Optional, Tuple, TypedDict, Union
import flask, copy, json

from serverLib import configs, database, exceptions

# Types

class BaseItem(TypedDict):
    title: int
    category: int
    colour: int
    image: Optional[bytes]
    location: int
    store: int

item_fields = Union[int, bytes]

# Classes

class Item:
    """
    The class for storing the information of a singular item.
    
    Guarantees:
        - Fields will always be their hinted types.
        - The `title`, `category`, and `location` attributes will be valid IDs in their respective tables.
        - The `store` attribute will always be a valid store location.

    Not guaranteed:
        - Item will always exist in Items table of the database.
        
    Attributes:
        _db (serverLib.database.DB): The database the `title`, `category`, and `location` IDs reference.
        _item (serverLib.items.BaseItem): The dictionary holding all necessary details about the Item.
    """
    
    def __init__(self, fields: BaseItem, db: database.DB) -> None:
        """
        The constructor for the Item class.

        Parameters:
            title (int): The ID of the item's title in the `title` table.
            category (int): The ID of the item's category in the `category` table.
            image (bytes | None): The bytes of the item's image.
            location (int): The ID of the item's location in the `locations` table.
            store (int): The item's store number
            db (serverLib.database.DB): The database containing the `title`, `category`, and `location` tables.
        """

        # Promise 1
        if not isinstance(fields["image"], (bytes, type(None))):
            raise exceptions.BadItem("Promise 1 was broken")
        
        for v in [fields[x] for x in ["title", "category", "location", "store"]]:
            if not isinstance(v, int):
                raise exceptions.BadItem("Promise 1 was broken")
        
        if not isinstance(db, database.DB):
            raise exceptions.BadItem("Promise 1 was broken")

        # Promises 2
        for (table, value) in {"title": fields["title"], "category": fields["category"], "location": fields["location"]}.items():
            if len(db.Execute(f"SELECT id FROM {table} WHERE id = ?", value)) != 1:
                raise exceptions.BadItem(f"Invalid {table} (Promise 2 was broken)")

        # Promise 3
        if fields["store"] > configs.MAX_STORE:
            raise exceptions.BadItem("Invalid store (Promise 3 was broken)")

        self._db: database.DB = db
        self._item: BaseItem = fields
    
    # Internal methods

    def lookup(self, table: str) -> str:
        """
        The function for converting an ID to its corresponding value.

        Parameters:
            table (str): The name of the table to search.

        Returns:
            str: The corresponding value.
        """
        
        return self._db.Execute(f"SELECT name FROM {table} WHERE id = ?", self._item[table])[0][0]

    def rawdict(self) -> BaseItem:
        """
        The method for getting a copy of an item's interal BaseItem dict.

        Returns:
            serverLib.items.BaseItem: The item's BaseItem
        """

        return copy.deepcopy(self._item)

    def dict(self) -> Dict[str, item_fields]:
        """
        The method for getting a formatted copy of an item's internal BaseDict dict.

        Returns:
            Dict[str, serverLib.items.item_fields]: The formatted dictionary.
        """

        inner: BaseItem = self.rawdict()
        inner.pop("image", None)
        
        inner["title"] = self.lookup("title")
        inner["category"] = self.lookup("category")
        inner["colour"] = self.lookup("colour")
        inner["location"] = self.lookup("location")
        
        return inner
    
    # Output methods

    def push(self) -> None:
        """
        The method for pushing an item to it's stored database.
        This method consumes the class instance!
        """

        i = self.rawdict()
        keys: List[str] = list(i.keys()) # Column names
        values: List[item_fields] = list(i.values()) # Values for those columns

        query: str = f"INSERT INTO items ({', '.join(keys)}) VALUES (?{', ?' * (len(keys) - 1)})" # Insert values query
        self._db.Execute(query, *values)

        del self

    def json(self) -> str:
        """
        The method for getting an item formatted as JSON.

        Returns:
            str: The item's JSON.
        """

        return json.dumps(self.dict())

    def image(self, default: bytes = configs.BASE_IMAGE) -> flask.Response:
        """
        The method for getting an item's image or a default image.

        Parameters:
            default (bytes) = serverLib.configs.BASE_IMAGE: The image to return on a None value for image.

        Returns:
            flask.Response: The formatted flask image response.
        """

        if not (img := self._item.get("image")):
            img: bytes = default

        response: flask.Response = flask.make_response(img)
        response.headers.set("Content-Type", "image/*")

        return response
    
    def __str__(self) -> str:
        inner: BaseItem = self.dict()
        
        return f"{inner['category']} {inner['title']} of colour {inner['colour']} found in {inner['location']} currently stored in box {inner['store']}"
    
    def __repr__(self) -> str:
        return f"{self._item=}"

class ItemHandler:
    """
    The class for storing the information of a multiple item.
    
    Guarantees:
        - Cannot break Item's guarantees
        
    Attributes:
        _db (serverLib.database.DB): The database contianing all the Items.
        _items (List[serverLib.items.BaseItem]): The list holding all the handler's Item instances.
    """

    def __init__(self, db: database.DB) -> None:
        """
        The constructor for the ItemHanlder class.

        Parameters:
            db (serverLib.database.DB): The database containing all the Items.
        """

        if not isinstance(db, database.DB):
            raise exceptions.BadDB # Validate input

        self._db: database.DB = db
        self._items: Dict[int, BaseItem] = dict()

    # Input methods

    def pull(self, id: int) -> None: # Single Item pull by ID
        if not isinstance(id, int):
            raise exceptions.InvalidInput # Validate input

        query: str = "SELECT title, category, colour, image, location, store FROM items WHERE id = ?"
        fields: BaseItem = dict(self._db.Execute(query, id)[0])
        
        if not fields:
            raise exceptions.InvalidInput("Bad ID")
        
        i: Item = Item(fields, self._db)

        self._items[int(id)] = i

    def massPull(self, query: str, *args: List[any]) -> List[int]: # Multiple Item pull by condition
        if not isinstance(query, str):
            raise exceptions.InvalidInput # Validate input
        
        ids: List[Tuple(int, None)] = self._db.Execute(f"SELECT id FROM items WHERE {query}", *args) # Get IDs of rows which match the query
        ids = list(map(lambda x: x[0], ids)) # Get the IDs out of their tuples
        
        list(map(self.pull, ids)) # Get the full items and add them to the internal items list
        
        return ids
    
    # Output methods

    def items(self) -> List[Item]:
        return list(self._items.values())
    
    def get(self) -> Dict[int, Dict[str, item_fields]]:
        return {i: x.json() for (i, x) in self._items.items()}
    
    def __str__(self) -> str:
        return ', '.join(list(map(str, self.items())))
       
    def __repr__(self) -> str:
        return f"{self._items=}"
    
    def json(self) -> str:
        return json.dumps(self.get())
