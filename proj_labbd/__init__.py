# Import of Flask and Flask Session
from flask import Flask, request, redirect, session, render_template
from flask_login import LoginManager, login_required
from flask_session import Session

# Imports of Routes Files
from .overview import overview_bp

# Import Models
from .models.user import User

app = Flask(__name__)
app.register_blueprint(overview_bp)

# Session Config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def login():
    return render_template("index.html.jinja", action="valid_credentials")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["login"]
    password = request.form["password"]

    user = User.authenticate(username, password)

    if user is None:
        return render_template("index.html.jinja", action="invalid_credentials")

    session["user_object"] = user

    return redirect("/overview")


@app.context_processor
def context_processor():
    def get_username():
        if session.get("user_object") is None:
            return None

        return session["user_object"]["name"]

    return dict(get_username=get_username)
