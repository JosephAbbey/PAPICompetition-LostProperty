"""
This module contains a number of helpful functions for the serverLib library.
"""

from typing import List
import datetime, json

from serverLib import configs, database, exceptions, items

class Notify:
    def __init__(self) -> None:
        self.data = list()
    
    def __save(self) -> None:
        with open(configs.NOTIFY, "w") as f:
            json.dump(self.data, f, indent=4)
    
    def notify(self, l: List[items.Item]) -> None:
        pass

def push(item: items.Item, db: database.DB) -> None:
    i = item.dict()
    keys: List[str] = list(i.keys()) # Column names
    values: List[items.item_fields] = list(i.values()) # Values for those columns

    query: str = f"INSERT INTO items ({', '.join(keys)}) VALUES (?, ?, ?, ?, ?)" # Insert values query
    return db.Execute(query, *values).fetchall()

def addItem(item: items.Item, db: database.DB) -> None:
    if not isinstance(item, items.Item):
        raise exceptions.InvalidInput # Validate input
    
    push(item, db)
   
def removeItem(id: int, db: database.DB) -> None:
    if not isinstance(id, int):
        raise exceptions.InvalidInput # Validate input
    
    db.Execute("DELETE FROM items WHERE id = ?", id) # Delete item
    
def checkExpire(db: database.DB, notif: Notify) -> None: # THREAD
    current: datetime.datetime = datetime.datetime.now(datetime.timezone.utc) # Current time (UTC)
    barrier: datetime.timedelta = current - configs.EXPIRY_TIME # Get lower bound on times
    
    handler: items.ItemHandler = items.ItemHandler(db)
    
    ids: List[int] = handler.massPull("inTime < ?", barrier) # Get all items that satisfy query
    
    if not ids:
        return # If there are no expired items, return early
    
    list(map(removeItem, ids)) # Delete items
    
    notif.notify(handler.items()) # Notify about removed items