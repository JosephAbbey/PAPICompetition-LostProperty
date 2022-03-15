import pkg_resources
import subprocess
import sqlite3

modules = [
    "flask",
    "flask_session"
]

installed = [i.key for i in pkg_resources.working_set]

install_lambda = lambda name: subprocess.run(f"pip3 install {name}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
[install_lambda(name) for name in modules if name not in installed]

from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from serverLib import serverLib

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True

Session(app)

@app.route("/")
def index():
    id: str = request.args.get("page", "1")
    categ: str = request.args.get("category", "1=1")

    lDB: serverLib.database.DB = serverLib.database.DB(sqlite3.connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)

    try: id: int = max(int(id), 1) # Lower bound and int
    except ValueError: id: int = 1 # If input is not int, set id to 1 (First page)
    except Exception as e: return f"{type(e)} : {e}", 500  # General error case

    # Sanitise and format input
    if not categ in serverLib.configs.CATEGORIES: categ: str = "1=1" # "All" condition
    else: categ: str = "category=" + str(serverLib.helpers.ignoredown(categ, "category", lDB)) # Convert user chosen category to database id

    # Ceiling round for the number of pages
    max_id: int = -1 * (-list(lDB.Execute(f"SELECT COUNT(1) FROM items WHERE {categ}")[0])[0] // serverLib.configs.PAGE_SIZE)

    id: int = min(id, max_id) # Upper bound

    handler.massPull(f"{categ} LIMIT {serverLib.configs.PAGE_SIZE} OFFSET {(id - 1) * serverLib.configs.PAGE_SIZE}")

    return render_template("index.html", json=handler.get(), categories=serverLib.configs.CATEGORIES, page=id, max=max_id)


@app.route("/item")
def item():
    if not (id := request.args.get("id")):
        return redirect("/")

    try: id: int = int(id)
    except ValueError: return redirect("/")
    except Exception as e: return f"{type(e)} : {e}", 500  # General error case

    lDB: serverLib.database.DB = serverLib.database.DB(sqlite3.connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)

    try: handler.pull(id)
    except serverLib.exceptions.InvalidInput: return redirect("/")

    i: serverLib.items.Item = handler.items()[0]

    return render_template("item.html", id=id, title=i.lookup("title"), json=i.json())

@app.route("/photo")
def photoAPI():
    if not (id := request.args.get("id")):
        return "Error 1 (No ID supplied)", 400

    try: id: int = int(id)
    except ValueError: return "Error 2 (Supplied ID was not a number)", 400
    except Exception as e: return f"{type(e)} : {e}", 500  # General error case

    lDB: serverLib.database.DB = serverLib.database.DB(sqlite3.connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)

    try: handler.pull(id)
    except serverLib.exceptions.InvalidInput: return "Error 3 (Supplied ID was not a valid Item)", 418

    return handler.items()[0].image()


@app.route("/login", methods=["GET", "POST"])
@serverLib.adminAuth.checkAdmin
def login():
    # GET request

    if request.method == "GET":
        return render_template("login.html")

    # POST request

    if not (pw := request.form.get("password")):
        return "Please enter a password", 401

    result: bool = serverLib.adminAuth.login(pw)

    if not result:
        return "Password was incorrect", 401

    session["admin"] = True

    return redirect("/admin")

@app.route("/admin", methods=["GET", "POST"])
@serverLib.adminAuth.checkLogin
def admin():
    lDB: serverLib.database.DB = serverLib.database.DB(sqlite3.connect(serverLib.configs.DATABASE))
    
    serverLib.helpers.checkExpire(lDB)
    
    # GET request
    if request.method == "GET":
        expired: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB) # Expired items
        requested: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB) # Requested items

        return render_template("admin.html", requested=requested.get(), expired=expired.get()) # Ben add requested and expired please

    config: serverLib.database.DBConfig = serverLib.database.DBConfig(lDB) # Database config object
    


if __name__ == "__main__":
    app.run()
