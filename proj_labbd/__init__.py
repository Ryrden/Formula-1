from flask import Flask, request, redirect, session, render_template
from flask_session import Session
from flask_login import LoginManager, login_required
from .models.user import User
from . import database

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def login():
    return render_template("index.html", action="login")

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["login"]
    password = request.form["password"]

    user = User.authenticate(username, password)

    if user is None:
        return render_template("index.html", action="invalid_login")

    session["user_object"] = user
    session["logged_in"] = True

    return redirect("/overview")


@app.route("/overview")
@login_required
def overview():
    if session.get("logged_in"):
        user_object = session["user_object"]

        print(user_object)
        
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