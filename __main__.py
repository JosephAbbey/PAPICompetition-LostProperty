import os
import sys
import pkg_resources

modules = [
    "flask"
]

installed = [i.key for i in pkg_resources.working_set]

for name in modules:
    if name in installed: print(name, "already in pkg_resources.working_set")
    else: os.system("pip{}.{} install {}".format(sys.version_info.major, sys.version_info.minor, name))

from flask import Flask, render_template, request, redirect, flash, session
from serverLib import serverLib
from sqlite3 import connect
import adminAuth

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
    
    i: serverLib.items.Item = handler.items()[0]

    return render_template("item.html", title=i.dict()["title"], json=i.json())
        
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

@app.route("/login", methods=["GET", "POST"])
def loginAPI():
    if request.method == "GET": # GET request
        return render_template("login.html")
    
    # POST request

    if not (pw := request.form.get("pw")):
        flash("Please enter a password")
        return redirect("/login")

    result: bool = adminAuth.login(pw)

    if not result:
        flash("Password was incorrect")
        return redirect("/login")

    


if __name__ == "__main__":
    app.run()