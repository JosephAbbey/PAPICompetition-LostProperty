from serverLib import serverLib

open(serverLib.configs.DATABASE, "w").close()

db: serverLib.database.DB = serverLib.database.DB(serverLib.configs.DATABASE)