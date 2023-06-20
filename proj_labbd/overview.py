# Import of Flask and Flask Session
from flask import Flask, request, redirect, session, render_template
from flask_login import LoginManager, login_required
from flask_session import Session
from flask import Blueprint

# Import Models
from .models.user import User

from . import database

overview_bp = Blueprint("overview", __name__)

@overview_bp.route("/overview")
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

    return render_template("overview.html.jinja", user=user_object, title="Overview")