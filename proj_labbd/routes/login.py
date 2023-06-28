# Import of Flask and Flask Session
from flask import  request, redirect, session, render_template, Blueprint

# Import Models
from ..interactor.user import User


login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login_post():
    """Login user"""
    username = request.form["login"]
    password = request.form["password"]

    user = User.authenticate(username, password)

    if user is None:
        return render_template("index.html.jinja", response="invalid_credentials")

    session["user_object"] = user

    return redirect("/overview")