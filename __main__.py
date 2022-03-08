import os
import sys
import pkg_resources

modules = [
    "flask",
    "flask_session"
]

installed = [i.key for i in pkg_resources.working_set]

[os.system("pip{}.{} install {}".format(sys.version_info.major, sys.version_info.minor, name)) for name in modules if name not in installed]

from flask import Flask, render_template, request, redirect, flash, session
from flask_session import Session
from serverLib import serverLib
from sqlite3 import connect
import adminAuth

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True

Session(app)

max = lambda x, y: x if x >= y else y

@app.route("/")
def index():
    id: str = request.args.get("page", "1")
    
    try:
        id: int = int(id) if int(id) >= 1 else 1
    except ValueError: id: int = 1
    except Exception as e: print(type(e), ":", e)
    
    lDB: serverLib.database.DB = serverLib.database.DB(connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)

    max: int = -1 * (-len(lDB.Execute("SELECT COUNT(1) FROM items").fetchall()) // serverLib.configs.PAGE_SIZE)
    
    handler.massPull(f"1=1 LIMIT {serverLib.configs.PAGE_SIZE} OFFSET {(id - 1) * serverLib.configs.PAGE_SIZE}")

    return render_template("index.html", json=handler.get(), categories=["Uniform", "Tech", "PE"], page=id, max=max)

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

    return render_template("item.html", id=id, title=i.dict()["title"], json=i.json())
        
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
    
    print(handler.items()[0].image().content_type)

    return handler.items()[0].image()

@app.route("/login", methods=["GET", "POST"])
def login():
    # GET request

    if request.method == "GET":
        return render_template("login.html")
    
    # POST request

    if not (pw := request.form.get("pw")):
        flash("Please enter a password")
        return redirect("/login")

    result: bool = adminAuth.login(pw)

    if not result:
        flash("Password was incorrect")
        return redirect("/login")

    session["admin"] = True

    return redirect("/admin")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    # GET request

    if request.method == "GET":
        return render_template("admin.html")

if __name__ == "__main__":
    app.run()