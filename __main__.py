from flask import Flask, render_template, request, redirect
from serverLib import serverLib
from sqlite3 import connect

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    id: str = request.args.get("page", "0")
    
    try: id: int = int(id)
    except ValueError: id: int = 0
    except Exception as e: print(type(e), ":", e)
    
    lDB: serverLib.database.DB = serverLib.database.DB(connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)
    
    handler.massPull(f"1=1 LIMIT {serverLib.configs.PAGE_SIZE} OFFSET {id * serverLib.configs.PAGE_SIZE}")
    
    return render_template("index.html", json=handler.get())

@app.route("/item")
def item():
    if not (id := request.args.get("id")): return redirect("/")
    
    try: id: int = int(id)
    except ValueError: return redirect("/")
    except Exception as e: print(type(e), ":", e)
    
    lDB: serverLib.database.DB = serverLib.database.DB(connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)
    
    try: handler.pull(id)
    except serverLib.exceptions.InvalidInput: return redirect("/")
    
    return render_template("item.html", json=handler.items()[0].dict())
        
@app.route("/photo")
def photoAPI():
    if not (id := request.args.get("id")): return "Error 1 (No ID supplied)"
    
    try: id: int = int(id)
    except ValueError: return "Error 2 (Supplied ID was not a number)"
    except Exception as e: print(type(e), ":", e)
    
    lDB: serverLib.database.DB = serverLib.database.DB(connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)
    
    try: handler.pull(id)
    except serverLib.exceptions.InvalidInput: return "Error 3 (Supplied ID was not a valid Item)"
    
    if not (r := handler.items()[0].image()): return "No image"
    
    return r

if __name__ == "__main__":
    app.run()