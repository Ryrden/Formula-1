# Import of Flask and Flask Session
from flask import Flask, request, redirect, session, render_template
from flask_login import LoginManager, login_required
from flask_session import Session

# Imports of Routes Files
from .routes.overview import overview_bp
from .routes.report import report_bp

# Import Models
from .interactor.user import User
from .interactor.admin import Admin
from .interactor.racing_team import RacingTeam
from .interactor.driver import Driver

app = Flask(__name__)
app.register_blueprint(overview_bp)
app.register_blueprint(report_bp)

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
    session.clear()
    return render_template("index.html.jinja", response="valid_credentials")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["login"]
    password = request.form["password"]

    user = User.authenticate(username, password)

    if user is None:
        return render_template("index.html.jinja", response="invalid_credentials")

    session["user_object"] = user

    return redirect("/overview")


@app.route("/register/driver", methods=["POST"])
def register_driver():
    driver_id = request.form["driver_id"]
    driver_ref = request.form["driver_ref"] or ""
    number = request.form["number"] or 0
    code = request.form["code"]
    forename = request.form["forename"]
    surname = request.form["surname"]
    dob = request.form["dob"]
    nationality = request.form["nationality"]
    url = request.form["url"] or ""

    Admin.insert_driver(
        driver_id, driver_ref, number, code, forename, surname, dob, nationality, url
    )

    return redirect("/overview")


@app.route("/register/racing-team", methods=["POST"])
def register_racing_team():
    constructor_id = request.form["constructor_id"]
    constructor_ref = request.form["constructor_ref"]
    name = request.form["name"]
    nationality = request.form["nationality"]
    url = request.form["url"] or ""

    Admin.insert_racing_team(constructor_id, constructor_ref, name, nationality, url)

    return redirect("/overview")


@app.route("/fetch/driver", methods=["POST"])
@login_required
def fetch_driver():
    constructor_id = session["user_object"]["source_id"]
    driver_name = request.form["driver_name"]

    report = {
        "id": 0,
        "title": "Report 0",
        "description": "Coisa alguma",
        "has_input": False,
        "headers": ["Driver Id", "Driver Ref", "Code", "Name", "Nationality"],
        "rows": Driver.get_related_drivers_by_forename(driver_name, constructor_id),
    }

    return render_template("./report.html.jinja", report=report)


@app.context_processor
def context_processor():
    def get_username():
        if session.get("user_object") is None:
            return None

        return session["user_object"]["name"]

    return dict(get_username=get_username)
