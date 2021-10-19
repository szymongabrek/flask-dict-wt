from os import close
import sqlite3

from flask import Flask, request, render_template, g
from data.dbHandler import query_db, close_db

app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    close_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dict")
def dict():
    q = request.args.get('q')

    res = query_db("SELECT * FROM ajt WHERE ang LIKE ?", [q])

    return render_template("result.html", query=q, owca=res)
