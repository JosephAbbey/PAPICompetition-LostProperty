"""
This module contains a number of helpful functions for the serverLib library.
"""

from typing import Dict, List, Set
import datetime, json, os

from serverLib import configs, database, exceptions, items

class Notify:
    """
    The class for dealing with items leaving the system.
    
    Attributes:
        file (str): The file to save ids to.
        data (Dict[str, Set[int]]): A dictionary holding two sets of ids (one for expired items, one for requested items).
    """
    
    def __init__(self, savefile: str) -> None:
        if not isinstance(savefile, str):
            raise exceptions.InvalidInput
        
        self.file: str = savefile
        
        if not os.path.isfile(savefile): open(savefile, "w").close()
        
        with open(self.file, "r") as f:
            try: self.data: Dict[str, Set[int]] = dict(json.load(f))
            except json.decoder.JSONDecodeError: self.data: Dict[str, Set[int]] = dict()
    
    def __save(self) -> None:
        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=4)
    
    def expire(self, ids: List[int]) -> None:
        pass
    
    def request(self, ids: List[int]) -> None:
        pass

def ignoredown(value: str, table: str, db: database.DB) -> int:
    """
    The opposite of the serverLib.items.Item.lookup method.

    Parameters:
        value (str): The value to get the id for
        table (str): The table to search in
        db (serverLib.database.DB): The database to search in

    Returns:
        int: The corresponding id
    """

    return list(db.Execute(f"SELECT id FROM {table} WHERE name = ?", value)[0])[0]

def addItem(item: items.Item) -> None: 
    """
    The method for adding an item to the database.
    This method consumes the Item!
    
    Parameters:
        item (serverLib.items.Item): The item to add to the database.
    """
    
    if not isinstance(item, items.Item):
        raise exceptions.InvalidInput # Validate input
    
    item.push() # Push the item
   
def removeItem(id: int, db: database.DB) -> None:
    """
    The method for removing an item from the database.
    
    Parameters:
        id (int): The id of the item to remove from the database.
        db (serverLib.database.DB): The database to remove the item from.
    """
    
    if not isinstance(id, int):
        raise exceptions.InvalidInput # Validate input
    
    db.Execute("DELETE FROM items WHERE id = ?", id) # Delete item
    
def checkExpire(db: database.DB, notif: Notify = Notify(configs.NOTIFY_FILE)) -> None:
    current: datetime.datetime = datetime.datetime.now(datetime.timezone.utc) # Current time (UTC)
    barrier: datetime.timedelta = current - configs.EXPIRY_TIME # Get lower bound on times
    
    handler: items.ItemHandler = items.ItemHandler(db)
    
    ids: List[int] = handler.massPull("inTime < ?", barrier) # Get all items that satisfy query
    
    if not ids:
        return # If there are no expired items, return early
    
    notif.notify(handler.items()) # Notify about items to remove