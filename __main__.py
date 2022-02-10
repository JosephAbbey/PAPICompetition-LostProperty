from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/static/")
@app.route("/<a>")
def index(a = None):
    return redirect("/static/" + (a or "index.html"))

app.run()