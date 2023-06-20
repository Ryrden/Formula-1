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

    overview_cards = _get_overview_driver()

    return render_template("overview.html.jinja", user=user_object, overview_cards=overview_cards)


def _get_overview_driver():
    amount_drivers = {
        "title": "Amount of Drivers Registered",
        "type_card": "default",
        "description": "Description here",
        "value": 20
    }

    amount_racing_team = {
        "title": "Amount of Racing Teams Registered",
        "type_card": "default",
        "description": "Description here",
        "value": 20
    }

    amount_races = {
        "title": "Amount of Races Registered",
        "type_card": "default",
        "description": "Description here",
        "value": 20
    }

    amount_seasons = {
        "title": "Amount of Seasons Registered",
        "type_card": "default",
        "description": "Description here",
        "value": 20
    }

    return [
        amount_drivers,
        amount_racing_team,
        amount_races,
        amount_seasons
    ]

