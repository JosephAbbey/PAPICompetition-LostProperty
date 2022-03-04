"""
This file contains the details for the customizable aspects of the serverLib library.
"""

import datetime
import json

MAX_STORE: int = 5 # Number of store boxes
PAGE_SIZE: int = 10 # Items per catalogue page

DATA_FOLDER: str = "data"
DATABASE: str = f"{DATA_FOLDER}/lostProperty.db" # Database file
NOTIFY: str = f"{DATA_FOLDER}/notifSave.json" # Savefile (JSON)

BASE_IMAGE_FILE: str = f"{DATA_FOLDER}/defImage.png"
with open(BASE_IMAGE_FILE, "rb") as img:
    BASE_IMAGE: bytes = img.read()

EXPIRY_TIME: datetime.timedelta = datetime.timedelta(hours=3) # Time until item expires
NOTIFY_TIME: datetime.timedelta = datetime.timedelta(weeks=3) # How often to notify