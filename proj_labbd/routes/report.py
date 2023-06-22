from flask import session, request, render_template, Blueprint
from flask_login import login_required

from ..interactor.admin import Admin
from ..interactor.driver import Driver
from ..interactor.racing_team import RacingTeam

report_bp = Blueprint("report", __name__)


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
            report["rows"] = Admin.get_report(report_id, request.form["value"])
        elif user_object["type"] == "DRIVER":
            pass
        elif user_object["type"] == "RACING_TEAM":
            pass

    return render_template("./report.html.jinja", report=report)


def _get_report_admin():
    report_1 = {
        "id": 1,
        "title": "Report 1",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Status", "Count"],
        "rows": Admin.get_report(1),
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
        "headers": ["City", "IATA", "Airport Name", "Distance", "Airport Type"],
        "rows": None,
    }

    return {1: report_1, 2: report_2}


def _get_report_racing_team(source_id):
    report_1 = {
        "id": 3,
        "title": "Report 1",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Name", "Wins"],
        "rows": RacingTeam.get_report(3, source_id),
    }

    report_2 = {
        "id": 4,
        "title": "Report 2",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Status", "Count"],
        "rows": RacingTeam.get_report(4, source_id),
    }

    return {1: report_1, 2: report_2}


def _get_report_driver(source_id):
    report_1 = {
        "id": 5,
        "title": "Report 1",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Wins", "Year", "Race"],
        "rows": Driver.get_report(5, source_id),
    }

    report_2 = {
        "id": 6,
        "title": "Report 2",
        "description": "Number of results, by status",
        "has_input": False,
        "headers": ["Status", "Count"],
        "rows": Driver.get_report(6, source_id),
    }

    return {1: report_1, 2: report_2}
