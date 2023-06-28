# Import of Flask and Flask Session
from flask import session, request, redirect, render_template, Blueprint
from flask_login import login_required

# Import Models
from ..interactor.user import User
from ..interactor.admin import Admin
from ..interactor.driver import Driver
from ..interactor.racing_team import RacingTeam

actions_bp = Blueprint("actions", __name__)

@actions_bp.route("/register/driver", methods=["POST"])
@login_required
def register_driver():
    """Register a new driver"""
    driver_id = request.form["driver_id"]
    driver_ref = request.form["driver_ref"] or ""
    number = request.form["number"] or 0
    code = request.form["code"]
    forename = request.form["forename"]
    surname = request.form["surname"]
    dob = request.form["dob"]
    nationality = request.form["nationality"]
    url = request.form["url"] or ""

    Admin.insert_driver(
        driver_id, driver_ref, number, code, forename, surname, dob, nationality, url
    )

    return redirect("/overview")

@actions_bp.route("/register/racing-team", methods=["POST"])
@login_required
def register_racing_team():
    """Register a new racing team"""
    constructor_id = request.form["constructor_id"]
    constructor_ref = request.form["constructor_ref"]
    name = request.form["name"]
    nationality = request.form["nationality"]
    url = request.form["url"] or ""

    Admin.insert_racing_team(constructor_id, constructor_ref, name, nationality, url)

    return redirect("/overview")


@actions_bp.route("/fetch/driver", methods=["POST"])
@login_required
def fetch_driver():
    """Fetch a driver by name"""
    constructor_id = session["user_object"]["source_id"]
    driver_name = request.form["driver_name"]

    report = {
        "id": 0,
        "title": "Report 0",
        "description": "Fetch a Drivers by Forename",
        "has_input": False,
        "headers": ["Driver Id", "Driver Ref", "Code", "Name", "Nationality"],
        "rows": Driver.get_related_drivers_by_forename(driver_name, constructor_id),
    }

    return render_template("./report.html.jinja", report=report)