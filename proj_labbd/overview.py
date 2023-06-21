# Import of Flask and Flask Session
from flask import Flask, request, redirect, session, render_template
from flask_login import LoginManager, login_required
from flask_session import Session
from flask import Blueprint

# Import Models
from .models.user import User
from .models.admin import Admin
from .models.driver import Driver
from .models.racing_team import RacingTeam

from . import database

overview_bp = Blueprint("overview", __name__)

@overview_bp.route("/overview")
@login_required
def overview():
    user_object = session["user_object"]

    if user_object["type"] == "DRIVER":
        overview_cards = _get_overview_driver(session["user_object"]["source_id"])

    elif user_object["type"] == "RACING_TEAM":
        overview_cards = _get_overview_racing_team(session["user_object"]["source_id"])

    elif user_object["type"] == "ADMIN":
        overview_cards = _get_overview_admin()

    return render_template("overview.html.jinja", user=user_object, overview_cards=overview_cards)

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