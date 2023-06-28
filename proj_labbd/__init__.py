# Import of Flask and Flask Session
from flask import Flask, request, redirect, session, render_template
from flask_login import LoginManager, login_required
from flask_session import Session

# Imports of Routes Files
from .routes.overview import overview_bp
from .routes.report import report_bp
from .routes.actions import actions_bp
from .routes.login import login_bp

# Import Models
from .interactor.user import User

app = Flask(__name__)
app.register_blueprint(overview_bp)
app.register_blueprint(report_bp)
app.register_blueprint(actions_bp)
app.register_blueprint(login_bp)

# Session Config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    """Load user from database."""
    return User.get(user_id)


@app.route("/")
def login():
    """Login page."""
    session.clear()
    return render_template("index.html.jinja", response="valid_credentials")


@app.context_processor
def context_processor():
    """Context processor for Jinja2 templates."""

    def get_username():
        if session.get("user_object") is None:
            return None

        return session["user_object"]["name"]

    return dict(get_username=get_username)
