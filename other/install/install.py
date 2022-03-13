from typing import Dict, Optional, Union
import subprocess
import sqlite3
import zipfile
import json
import os

# Unzip data
    
with zipfile.ZipFile("data.zip", mode="r") as archive:
    archive.extractall()
    
os.remove("data.zip")

# Generate mainConfig.json (Required for serverLib)

while True:
    try: maxstore: int = int(input("How many numbered boxes will be used to organise lost property: "))
    except ValueError: print("Input must be a number.") # Input was not a number
    except Exception as e: print(f"An error occured ({type(e).__name__})") # Some other issue occured (Allows for KeyboardInterrupt)
    finally: break
    
defConfig: Dict[str, Union[str, int]] = {
    "max_store": maxstore, # User set
    "page_size": 16, # Reasonable number
    "data_folder": "data", # Self-explanatory
    "expiry_time_ms": 15724800000 # 6 months default
}

json.dump(defConfig, open("mainConfig.json", "w"), indent=4)

library_wheel: str = "serverLib-0.1.0-py3-none-any.whl"
subprocess.run(f"pip3 install {library_wheel}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
os.remove(library_wheel)

from serverLib import serverLib # serverLib can now be imported

open(serverLib.configs.DATABASE, "w").close() # Create database file

conn: sqlite3.Connection = sqlite3.connect(serverLib.configs.DATABASE) # Open database connection
db: serverLib.database.DB = serverLib.database.DB(conn) # Wrap database connection

db.ExecuteScript(open(f"{serverLib.configs.DATA_FOLDER}/Template.sql")) # Apply template to new database

# Get an admin password

while True:
    password: str = input("Create an admin password: ")
    
    details: Optional[str] = serverLib.adminAuth.update(password)
    
    if details is None: break
    
    print(details)