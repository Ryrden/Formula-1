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

    return render_template("overview.html.jinja", user=user_object, overview_cards=overview_cards, actions=actions)

def _get_actions_admin():
    register_racing_team = {
        "id": 0,
        "title": "Register Racing Team",
        "description": "Register a new Racing Team in the Database",
        "operation": "register",
        "fields": [
            {
                "name": "Constructor Id",
                "type": "number",
                "placeholder": "Racing Team Identifier",
                "required": True
            },
            {
                "name": "Constructor Ref",
                "type": "text",
                "placeholder": "Racing Team Reference",
                "required": True
            },
            {
                "name": "Constructor Name",
                "type": "text",
                "placeholder": "Racing Team Name",
                "required": True
            },
            {
                "name": "Constructor Nationality",
                "type": "text",
                "placeholder": "Racing Team Nationality",
                "required": True
            },
            {
                "name": "Constructor Url",
                "type": "text",
                "placeholder": "Racing Team Website",
                "required": True
            }
        ],
        "action": "register/racing-team"
    }

    register_driver = {
        "id": 1,
        "title": "Register Driver",
        "description": "Register a new Driver in the Database",
        "operation": "register",
        "fields": [
            {
                "name": "DriverId",
                "type": "number",
                "placeholder": "Driver ID",
                "required": True
            },
            {
                "name": "DriverRef",
                "type": "text",
                "placeholder": "Driver Reference",
                "required": True
            },
            {
                "name": "DriverNumber",
                "type": "number",
                "placeholder": "Driver Number",
                "required": False
            },
            {
                "name": "Code",
                "type": "text",
                "placeholder": "Driver Code",
                "required": False
            },
            {
                "name": "Forename",
                "type": "text",
                "placeholder": "Driver Forename",
                "required": True
            },
            {
                "name": "Surname",
                "type": "text",
                "placeholder": "Driver Surname",
                "required": True
            },
            {
                "name": "dob",
                "type": "date",
                "placeholder": "Driver Date of Birth",
                "required": True
            },
            {
                "name": "nationality",
                "type": "text",
                "placeholder": "Driver Nationality",
                "required": True
            },
            {
                "name": "url",
                "type": "text",
                "placeholder": "Driver URL",
                "required": True
            }
        ],
        "action": "register/driver"
    }

    return [
        register_racing_team,
        register_driver
    ]

def _get_actions_racing_team():
    fetch_driver = {
        "id": 0,
        "title": "Fetch Driver",
        "description": "Fetch a Driver from the Database",
        "operation": "fetch",
        "fields": [
            {
                "name": "DriverName",
                "type": "text",
                "placeholder": "Driver Name",
                "required": True
            }
        ],
        "action": "fetch/driver"
    }

    return [
        fetch_driver
    ]


def _get_overview_admin():
    amount_drivers = {
        "image": "driver.png",
        "title": "Amount of Drivers",
        "type_card": "default",
        "description": "Total Drivers registered in the Database",
        "value": Admin.get_amount_drivers()
    }

    amount_racing_team = {
        "image": "racing_team.png",
        "title": "Amount of Racing Teams",
        "type_card": "default",
        "description": "Total Racing Teams registered in the Database",
        "value": Admin.get_amount_racing_team()
    }

    amount_races = {
        "image": "races.png",
        "title": "Amount of Races",
        "type_card": "default",
        "description": "Total of Races registered in the Database",
        "value": Admin.get_amount_races()
    }

    amount_seasons = {
        "image": "formula1.png",
        "title": "Amount of Seasons",
        "type_card": "default",
        "description": "Total of Seasons registered in the Database",
        "value": Admin.get_amount_seasons()
    }

    return [
        amount_drivers,
        amount_racing_team,
        amount_races,
        amount_seasons
    ]

def _get_overview_racing_team(source_id):
    amount_wins = {
        "image": "winner.png",
        "title": "Amount of Wins",
        "type_card": "default",
        "description": "Total Wins of the Racing Team",
        "value": RacingTeam.get_amount_wins(source_id)
    }

    amount_different_drivers = {
        "image": "team.png",
        "title": "Amount of Different Drivers",
        "type_card": "default",
        "description": "Number of different drivers who have already raced for the team;",
        "value": RacingTeam.get_diff_drivers(source_id)
    }

    occurrence_of_existence = {
        "image": "formula1.png",
        "title": "Occurrences",
        "type_card": "date",
        "description": "First and Last year in which there is team data in the base",
        "value": RacingTeam.get_first_and_last_ocurrences(source_id)
    }

    return [
        amount_wins,
        amount_different_drivers,
        occurrence_of_existence
    ]


def _get_overview_driver(source_id):
    amount_wins = {
        "image": "winner.png",
        "title": "Amount of Wins",
        "type_card": "default",
        "description": "Total Wins of the Driver",
        "value": Driver.get_amount_wins(source_id)
    }

    occurrence_of_existence = {
        "image": "formula1.png",
        "title": "Occurrences",
        "type_card": "date",
        "description": "First and last year in which there is pilot data in the base",
        "value": Driver.get_first_and_last_ocurrences(source_id)
    }

    return [
        amount_wins,
        occurrence_of_existence
    ]