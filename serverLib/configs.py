"""
This file contains the details for the customizable aspects of the serverLib library.
"""

import datetime

MAX_STORE: int = 5 # Number of store boxes
PAGE_SIZE: int = 10 # Items per catalogue page

DATA_FOLDER: str = "data"
DATABASE: str = f"{DATA_FOLDER}/lostProperty.db" # Database file
NOTIFY: str = f"{DATA_FOLDER}/notifSave.json" # Savefile (JSON)

EXPIRY_TIME: datetime.timedelta = datetime.timedelta(hours=3) # Time until item expires
NOTIFY_TIME: datetime.timedelta = datetime.timedelta(weeks=3) # How often to notify