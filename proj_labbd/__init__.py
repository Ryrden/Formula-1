from flask import Flask, request, redirect, render_template
from . import database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/airports")
def airports():
    db_connection = database.DatabaseConnection()

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM airports")

    rows = cursor.fetchall()

    # TODO: Tratar close  do servidor

    return render_template("index.html", airports=rows[:20])

# how to create post route with flask 
@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["login"]
    password = request.form["password"]
    
    db_connection = database.DatabaseConnection()

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM users WHERE login = %s AND password = md5(%s)", (username, password))

    rows = cursor.fetchall()

    if (len(rows) > 0):
        return render_template("home.html", message="Login successful")
    else:
        return redirect("/")

        