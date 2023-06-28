from flask import session, request, render_template, Blueprint
from flask_login import login_required

from ..interactor.admin import Admin
from ..interactor.driver import Driver
from ..interactor.racing_team import RacingTeam

report_bp = Blueprint("report", __name__)

REPORT_1_ADMIN = 1
REPORT_2_ADMIN = 2
REPORT_1_RACING_TEAM = 3
REPORT_2_RACING_TEAM = 4
REPORT_1_DRIVER = 5
REPORT_2_DRIVER = 6


@report_bp.route("/report/<int:report_id>", methods=["GET", "POST"])
@login_required
def reports_get(report_id):
    """Returns the report page for the given report_id."""
    user_object = session["user_object"]
    source_id = int(user_object["source_id"])

    if request.method == "GET":
        if user_object["type"] == "DRIVER":
            report = _get_report_driver(source_id)[report_id]

        elif user_object["type"] == "RACING_TEAM":
            report = _get_report_racing_team(source_id)[report_id]

        elif user_object["type"] == "ADMIN":
            report = _get_report_admin()[report_id]
    elif request.method == "POST":
        if user_object["type"] == "ADMIN":
            report = _get_report_admin()[report_id]
            report["rows"] = Admin.get_report(REPORT_2_ADMIN, request.form["value"])
        elif user_object["type"] == "DRIVER":
            pass
        elif user_object["type"] == "RACING_TEAM":
            pass

    return render_template("./report.html.jinja", report=report)


def _get_report_admin():
    """Returns the report for the admin user."""
    report_1 = {
        "id": 1,
        "title": "Report 1",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Status", "Count"],
        "rows": Admin.get_report(REPORT_1_ADMIN),
    }

    report_2 = {
        "id": 2,
        "title": "Report 2",
        "description": "Brazilian airports within a 100km radius distance from the given city",
        "has_input": True,
        "input": {
            "label": "City",
            "placeholder": "Enter a city name",
            "type": "text",
            "name": "city",
        },
        "headers": [
            "City",
            "IATA",
            "Airport Name",
            "Airport City",
            "Distance",
            "Airport Type",
        ],
        "rows": None,
    }

    return {1: report_1, 2: report_2}


def _get_report_racing_team(source_id):
    """Returns the report for the racing team user."""
    report_1 = {
        "id": 3,
        "title": "Report 1",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Name", "Wins"],
        "rows": RacingTeam.get_report(REPORT_1_RACING_TEAM, source_id),
    }

    report_2 = {
        "id": 4,
        "title": "Report 2",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Status", "Count"],
        "rows": RacingTeam.get_report(REPORT_2_RACING_TEAM, source_id),
    }

    return {1: report_1, 2: report_2}


def _get_report_driver(source_id):
    """Returns the report for the driver user."""
    report_1 = {
        "id": 5,
        "title": "Report 1",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Wins", "Year", "Race"],
        "rows": Driver.get_report(REPORT_1_DRIVER, source_id),
    }

    report_2 = {
        "id": 6,
        "title": "Report 2",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Status", "Count"],
        "rows": Driver.get_report(REPORT_2_DRIVER, source_id),
    }

    return {1: report_1, 2: report_2}
