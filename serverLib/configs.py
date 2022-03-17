"""
This file contains the details for the customizable aspects of the serverLib library.
"""

from io import TextIOWrapper
from typing import Dict, List, Union
import datetime
import json

# Reading config file

CONFIG_FILE: TextIOWrapper = open("mainConfig.json")
CONFIG_JSON: Dict[str, Union[str, int]] = json.load(CONFIG_FILE)

# Database details

MAX_STORE: int = CONFIG_JSON["max_store"]  # Number of store boxes
PAGE_SIZE: int = CONFIG_JSON["page_size"]  # Items per catalogue page

# External data files

DATA_FOLDER: str = CONFIG_JSON["data_folder"]
DATABASE: str = f"{DATA_FOLDER}/lostProperty.db"  # Database file
NOTIFY_FILE: str = f"{DATA_FOLDER}/notifSave.json"  # Savefile (JSON)

BASE_IMAGE_FILE: str = f"{DATA_FOLDER}/defImage.png"  # Default image file
with open(BASE_IMAGE_FILE, "rb") as img:
    BASE_IMAGE: bytes = img.read()  # Default image bytes

# Timedeltas

EXPIRY_TIME: datetime.timedelta = datetime.timedelta(milliseconds=CONFIG_JSON["expiry_time_ms"])  # Time until item expires (milliseconds)