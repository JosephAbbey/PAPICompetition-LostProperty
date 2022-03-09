from serverLib.configs import PAGE_SIZE
import sqlite3
import adminAuth
from serverLib import serverLib
from flask_session import Session
from flask import Flask, render_template, request, redirect, flash, session
import os
import sys
import pkg_resources

modules = [
    "flask",
    "flask_session"
]

installed = [i.key for i in pkg_resources.working_set]
[
    os.system(
        "pip{}.{} install {}".format(
            sys.version_info.major,
            sys.version_info.minor, name
        )
    ) for name in modules if name not in installed
]


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True

Session(app)


@app.route("/")
def index():
    id: str = request.args.get("page", "1")
    categ: str = request.args.get("category", "1=1")

    lDB: serverLib.database.DB = serverLib.database.DB(
        sqlite3.connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)

    try:
        # Verify user input is valid, set to max if not
        id: int = max(int(id), 1)
    # except ValueError: id: int = 1 # If input is not int, set id to 1 (First page)
    except Exception as e:
        return f"{type(e)} : {e}", 500  # General error case

    if not categ in [*serverLib.configs.CATEGORIES]:
        categ = "1=1"  # Sanitise user input
    else:
        categ = f"category={serverLib.configs.CATEGORIES.index(categ) + 1}"

    max_id: int = -1 * \
        (-list(lDB.Execute(f"SELECT COUNT(1) FROM items WHERE {categ}").fetchall()[0])[
         0] // serverLib.configs.PAGE_SIZE)

    if id > max_id:
        id = max_id  # If id is greater than max_id, set id to max_id

    handler.massPull(
        f"{categ} LIMIT {PAGE_SIZE} OFFSET {(id - 1) * PAGE_SIZE}")

    return render_template("index.html", json=handler.get(), categories=serverLib.configs.CATEGORIES, page=id, max=max_id)


@app.route("/item")
def item():
    if not (id := request.args.get("id")):
        return redirect("/")

    try:
        id: int = int(id)
    except ValueError:
        return redirect("/")
    except Exception as e:
        print(type(e), ":", e)

    lDB: serverLib.database.DB = serverLib.database.DB(
        sqlite3.connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)

    try:
        handler.pull(id)
    except serverLib.exceptions.InvalidInput:
        return redirect("/")

    i: serverLib.items.Item = handler.items()[0]

    return render_template("item.html", id=id, title=i.lookup("title"), json=i.json())


@app.route("/photo")
def photoAPI():
    if not (id := request.args.get("id")):
        return "Error 1 (No ID supplied)", 400

    try:
        id: int = int(id)
    except ValueError:
        return "Error 2 (Supplied ID was not a number)", 400
    except Exception as e:
        print(type(e), ":", e)

    lDB: serverLib.database.DB = serverLib.database.DB(
        sqlite3.connect(serverLib.configs.DATABASE))
    handler: serverLib.items.ItemHandler = serverLib.items.ItemHandler(lDB)

    try:
        handler.pull(id)
    except serverLib.exceptions.InvalidInput:
        return "Error 3 (Supplied ID was not a valid Item)", 418

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
