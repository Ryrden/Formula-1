# Import of Flask and Flask Session
from flask import Flask, request, redirect, session, render_template
from flask_login import LoginManager, login_required
from flask_session import Session
from flask import Blueprint

# Import Models
from .models.user import User
from .models.admin import Admin

from . import database

overview_bp = Blueprint("overview", __name__)

@overview_bp.route("/overview")
@login_required
def overview():
    user_object = session["user_object"]

    overview_cards = _get_overview_admin()

    return render_template("overview.html.jinja", user=user_object, overview_cards=overview_cards)


def _get_overview_admin():
    amount_drivers = {
        "title": "Amount of Drivers",
        "type_card": "default",
        "description": "Description here",
        "value": Admin.get_amount_drivers()
    }

    amount_racing_team = {
        "title": "Amount of Racing Teams",
        "type_card": "default",
        "description": "Description here",
        "value": 20
        # "value": Admin.get_amount_racing_team()
    }

    amount_races = {
        "title": "Amount of Races",
        "type_card": "default",
        "description": "Description here",
        "value": 20
        # "value": Admin.get_amount_races()
    }

    amount_seasons = {
        "title": "Amount of Seasons",
        "type_card": "default",
        "description": "Description here",
        "value": 20
        # "value": Admin.get_amount_seasons()
    }

    return [
        amount_drivers,
        amount_racing_team,
        amount_races,
        amount_seasons
    ]

