# Import of Flask and Flask Session
from flask import session, render_template, Blueprint
from flask_login import login_required

# Import Models
from ..interactor.user import User
from ..interactor.admin import Admin
from ..interactor.driver import Driver
from ..interactor.racing_team import RacingTeam

overview_bp = Blueprint("overview", __name__)


@overview_bp.route("/overview")
@login_required
def overview():
    """Render the Overview Page with the Overview Cards and Actions for the User"""
    user_object = session["user_object"]

    if user_object["type"] == "DRIVER":
        overview_cards = _get_overview_driver(session["user_object"]["source_id"])
        actions = []

    elif user_object["type"] == "RACING_TEAM":
        overview_cards = _get_overview_racing_team(session["user_object"]["source_id"])
        actions = _get_actions_racing_team()

    elif user_object["type"] == "ADMIN":
        overview_cards = _get_overview_admin()
        actions = _get_actions_admin()

    return render_template(
        "overview.html.jinja",
        user=user_object,
        overview_cards=overview_cards,
        actions=actions,
    )


def _get_actions_admin():
    """Return the Actions for the Admin User"""
    register_racing_team = {
        "id": 0,
        "title": "Register Racing Team",
        "description": "Register a new Racing Team in the Database",
        "operation": "Register",
        "fields": [
            {
                "name": "constructor_id",
                "label": "Constructor Id *",
                "type": "number",
                "placeholder": "Racing Team Identifier",
                "required": "required",
            },
            {
                "name": "constructor_ref",
                "label": "Constructor Ref *",
                "type": "text",
                "placeholder": "Racing Team Reference",
                "required": "required",
            },
            {
                "name": "name",
                "label": "Constructor Name *",
                "type": "text",
                "placeholder": "Racing Team Name",
                "required": "required",
            },
            {
                "name": "nationality",
                "label": "Constructor Nationality *",
                "type": "text",
                "placeholder": "Racing Team Nationality",
                "required": "required",
            },
            {
                "name": "url",
                "label": "Constructor Url",
                "type": "text",
                "placeholder": "Racing Team Website",
                "required": "",
            },
        ],
        "action": "register/racing-team",
    }

    register_driver = {
        "id": 1,
        "title": "Register Driver",
        "description": "Register a new Driver in the Database",
        "operation": "Register",
        "fields": [
            {
                "name": "driver_id",
                "label": "Driver Id *",
                "type": "number",
                "placeholder": "Driver ID",
                "required": "required",
            },
            {
                "name": "driver_ref",
                "label": "Driver Ref *",
                "type": "text",
                "placeholder": "Driver Reference",
                "required": "required",
            },
            {
                "name": "number",
                "label": "Driver Number",
                "type": "number",
                "placeholder": "Driver Number",
                "required": "",
            },
            {
                "name": "code",
                "label": "Code",
                "type": "text",
                "placeholder": "Driver Code",
                "required": "",
            },
            {
                "name": "forename",
                "label": "Forename *",
                "type": "text",
                "placeholder": "Driver Forename",
                "required": "required",
            },
            {
                "name": "surname",
                "label": "Surname *",
                "type": "text",
                "placeholder": "Driver Surname",
                "required": "required",
            },
            {
                "name": "dob",
                "label": "Date of Birth *",
                "type": "date",
                "placeholder": "Driver Date of Birth",
                "required": "required",
            },
            {
                "name": "nationality",
                "label": "Nationality *",
                "type": "text",
                "placeholder": "Driver Nationality",
                "required": "required",
            },
            {
                "name": "url",
                "label": "url",
                "type": "text",
                "placeholder": "Driver URL",
                "required": "",
            },
        ],
        "action": "register/driver",
    }

    return [register_racing_team, register_driver]


def _get_actions_racing_team():
    """Return the Actions for the Racing Team User"""
    fetch_driver = {
        "id": 0,
        "title": "Fetch Driver",
        "description": "Fetch a Driver from the Database",
        "operation": "Fetch",
        "fields": [
            {
                "name": "driver_name",
                "label": "Driver Name",
                "type": "text",
                "placeholder": "Driver Name",
                "required": "required",
            }
        ],
        "action": "fetch/driver",
    }

    return [fetch_driver]


def _get_overview_admin():
    """Return the Overview Cards for the Admin User"""
    amount_drivers = {
        "image": "driver.png",
        "title": "Amount of Drivers",
        "type_card": "default",
        "description": "Total Drivers registered in the Database",
        "value": Admin.get_amount_drivers(),
    }

    amount_racing_team = {
        "image": "racing_team.png",
        "title": "Amount of Racing Teams",
        "type_card": "default",
        "description": "Total Racing Teams registered in the Database",
        "value": Admin.get_amount_racing_team(),
    }

    amount_races = {
        "image": "races.png",
        "title": "Amount of Races",
        "type_card": "default",
        "description": "Total of Races registered in the Database",
        "value": Admin.get_amount_races(),
    }

    amount_seasons = {
        "image": "formula1.png",
        "title": "Amount of Seasons",
        "type_card": "default",
        "description": "Total of Seasons registered in the Database",
        "value": Admin.get_amount_seasons(),
    }

    return [amount_drivers, amount_racing_team, amount_races, amount_seasons]


def _get_overview_racing_team(source_id):
    """Return the Overview Cards for the Racing Team User"""
    amount_wins = {
        "image": "winner.png",
        "title": "Amount of Wins",
        "type_card": "default",
        "description": "Total Wins of the Racing Team",
        "value": RacingTeam.get_amount_wins(source_id),
    }

    amount_different_drivers = {
        "image": "team.png",
        "title": "Amount of Different Drivers",
        "type_card": "default",
        "description": "Number of different drivers who have already raced for the team;",
        "value": RacingTeam.get_diff_drivers(source_id),
    }

    occurrence_of_existence = {
        "image": "formula1.png",
        "title": "Occurrences",
        "type_card": "date",
        "description": "First and Last year in which there is team data in the base",
        "value": RacingTeam.get_first_and_last_ocurrences(source_id),
    }

    return [amount_wins, amount_different_drivers, occurrence_of_existence]


def _get_overview_driver(source_id):
    """Return the Overview Cards for the Driver User"""
    amount_wins = {
        "image": "winner.png",
        "title": "Amount of Wins",
        "type_card": "default",
        "description": "Total Wins of the Driver",
        "value": Driver.get_amount_wins(source_id),
    }

    occurrence_of_existence = {
        "image": "formula1.png",
        "title": "Occurrences",
        "type_card": "date",
        "description": "First and last year in which there is pilot data in the base",
        "value": Driver.get_first_and_last_ocurrences(source_id),
    }

    return [amount_wins, occurrence_of_existence]
