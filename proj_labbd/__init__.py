from flask import Flask, request, redirect, session, render_template
from flask_session import Session
from flask_login import LoginManager, login_required
from .models.user import User
from . import database

app = Flask(__name__)

# Session Config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def login():
    return render_template("index.html.jinja", action="valid_credentials")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["login"]
    password = request.form["password"]

    user = User.authenticate(username, password)

    if user is None:
        return render_template("index.html.jinja", action="invalid_credentials")

    session["user_object"] = user

    return redirect("/overview")


@app.route("/overview")
@login_required
def overview():
    user_object = session["user_object"]

    db_connection = database.DatabaseConnection()
    cursor = db_connection.cursor()

    switcher = {
        "driver": "SELECT CONCAT(D.forename, ' ' , D.surname) AS name FROM Driver D WHERE D.driverid = %s",
        "constructor": "SELECT C.name FROM Constructors C WHERE C.constructorid = %s",
    }

    source_id = (str(user_object["source_id"]),)

    match user_object["type"]:
        case "DRIVER":
            cursor.execute(switcher.get("driver"), source_id)
            name = cursor.fetchone()[0]
        case "RACING_TEAM":
            cursor.execute(switcher.get("constructor"), source_id)
            name = cursor.fetchone()[0]
        case "ADMIN":
            name = "Administrator"

    user_object["name"] = name

    return render_template("overview.html.jinja", user=user_object)

# TODO: Pegar qual tipo de relatório é por query Params
@app.route("/report1")
@login_required
def reports():
    user_object = session["user_object"]

    switcher = {
        "admin_report1": "SELECT * FROM report1()",
        # TODO: Add other reports
    }

    db_connection = database.DatabaseConnection()
    cursor = db_connection.cursor()
    
    match user_object["type"]:
        case "ADMIN":
            cursor.execute(switcher.get("admin_report1"))
            report = cursor.fetchall()
        case "DRIVER":
            # TODO: Add driver report
            report = None
        case "RACING_TEAM":
            # TODO: Add racing team report
            report = None

    return render_template("./reports/report1.html.jinja", user=user_object, report=report)


@app.context_processor
def context_processor():
    def get_username():
        if session.get("user_object") is None:
            return None

        return session["user_object"]["name"]

    return dict(get_username=get_username)
