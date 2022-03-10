from serverLib import serverLib
import sqlite3

open(serverLib.configs.DATABASE, "w").close()

conn: sqlite3.Connection = sqlite3.connect(serverLib.configs.DATABASE)
db: serverLib.database.DB = serverLib.database.DB(conn)

db.ExecuteScript(open(f"{serverLib.configs.DATA_FOLDER}/Template.sql"))