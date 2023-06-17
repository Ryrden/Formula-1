from flask import Flask, request, redirect, session, render_template
from flask_session import Session
from . import database

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["login"]
    password = request.form["password"]

    db_connection = database.DatabaseConnection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Users U WHERE login = %s AND password = md5(%s)", (username, password))
    rows = cursor.fetchall()

    if len(rows) == 1:
        user_id, login, _, user_type, source_id = rows[0]
        user_object = { "user_id": user_id, "username": login, "user_type": user_type, "source_id": source_id }
        session["logged_in"] = True
        session["user_object"] = user_object
        return redirect("/overview")
    else:
        return redirect("/")

@app.route("/overview")
def overview():
    if session.get("logged_in"):
        user_object = session["user_object"]
        
        db_connection = database.DatabaseConnection()
        cursor = db_connection.cursor()
        
        switcher = {
            "driver": "SELECT CONCAT(D.forename, ' ' , D.surname) AS name FROM Driver D WHERE D.driverid = %s",
            "constructor": "SELECT C.name FROM Constructors C WHERE C.constructorid = %s"
        }
        
        source_id = (
            str(user_object["source_id"]),
        )

        match user_object["user_type"]:
            case "DRIVER":
                cursor.execute(switcher.get("driver"), source_id)
                name = cursor.fetchone()[0]
            case "RACING_TEAM":
                cursor.execute(switcher.get("constructor"), source_id)
                name = cursor.fetchone()[0]
            case "ADMIN":
                name = "Administrator"

        user_object["name"] = name

        return render_template("overview.html", user=user_object)
    else:
        return redirect("/")