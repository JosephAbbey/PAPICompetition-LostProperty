"""This module contains a number of helpful functions for the serverLib library."""

from typing import Dict, List, Optional, Set
import datetime, json, os

from serverLib import configs, database, exceptions, items

class Notify:
    """
    The class for dealing with items leaving the system.
    
    Attributes:
        file (str): The file to save data to.
        data (Dict[str, Set[int]]): A dictionary holding two sets of ids (one for expired items, one for requested items).
    """
    
    def __init__(self, savefile: str = configs.NOTIFY_FILE) -> None:
        """
        The constructor for the Notify class.

        Parameters:
            savefile (str): The file to saved data to.
        """

        if not isinstance(savefile, str): # Verify that the savefile is a string
            raise exceptions.InvalidInput
        
        self.file: str = savefile
        
        # Create the savefile if it does not exist
        if not os.path.isfile(savefile): open(savefile, "w").close()
        
        # Read data from savefile
        with open(self.file, "r") as f:
            try: self.data: Dict[str, List[int]] = dict(json.load(f))
            except json.decoder.JSONDecodeError: self.data: Dict[str, Set[int]] = {"exp": [], "req": []}

        self.__save()
    
    def __save(self) -> None:
        # The internal save method, not part of the public API

        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=4)
    
    def expired(self) -> List[int]:
        """
        The method for getting the list of expired ids from a Notify instance.

        Returns:
            List[int]: The list of ids.
        """

        return self.data["exp"]

    def requested(self) -> List[int]:
        """
        The method for getting the list of requested ids from a Notify instance.

        Returns:
            List[int]: The list of ids.
        """

        return self.data["req"]

    def expire(self, ids: List[int]) -> None:
        """
        The method for adding a list of ids to the expired ids list.
        This method does not add the id if it exists in the requested ids list or it already exists in the expired ids list.

        Parameters:
            ids (List[int]): The list of ids to add.
        """

        # Remove ids that already exists or are in the requested list
        valid_ids: List[int] = [id for id in ids if (id not in self.requested() and id not in self.expired())]

        # Add remaining ids to expired list
        list(map(self.expired().append, valid_ids))

        # Save
        self.__save()

    def request(self, id: int) -> None:
        """
        The method for adding an ids to the requested ids list.
        This method does not add the id if it already exists in the requested ids list and removes it from the expired ids list if it is there.

        Parameters:
            ids (int): The id to add.
        """

        # Return if already in requested ids list
        if id in self.requested(): return

        # Remove from expired ids list if it is there
        if id in self.expired(): expired.remove(id)

        # Add id to requested
        self.requested().append(id)

        # Save
        self.__save()

def ignoredown(value: str, table: str, db: database.DB) -> Optional[int]:
    """
    The opposite of the serverLib.items.Item.lookup method.

    Parameters:
        value (str): The value to get the id for
        table (str): The table to search in
        db (serverLib.database.DB): The database to search in

    Returns:
        int: The corresponding id
    """

    if not value: return None

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

def checkExpire(db: database.DB, notif: Notify = Notify()) -> None:
    current: datetime.datetime = datetime.datetime.now(datetime.timezone.utc) # Current time (UTC)
    barrier: datetime.timedelta = current - configs.EXPIRY_TIME # Get lower bound on times
    
    handler: items.ItemHandler = items.ItemHandler(db)
    
    ids: List[int] = handler.massPull("inTime < ?", barrier) # Get all items that satisfy query
    
    if not ids:
        return # If there are no expired items, return early
    
    notif.expire(ids) # Notify about items to remove
