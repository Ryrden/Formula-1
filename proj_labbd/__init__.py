# Import of Flask and Flask Session
from flask import Flask, request, redirect, session, render_template
from flask_login import LoginManager, login_required
from flask_session import Session

# Imports of Routes Files
from .overview import overview_bp

# Import Models
from .interactor.user import User
from .interactor.admin import Admin
from .interactor.racing_team import RacingTeam
from .interactor.driver import Driver

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


@app.route("/report/<int:report_id>", methods=["GET"])
@login_required
def reports_get(report_id):
    MAX_NUMBER_OF_REPORTS = 6
    RANGE_OF_REPORTS = range(1, MAX_NUMBER_OF_REPORTS + 1)
    if report_id not in RANGE_OF_REPORTS:
        return redirect("/overview")
    
    REPORT_ID_WITHOUT_INPUT = 1

    if report_id is REPORT_ID_WITHOUT_INPUT:
        report = {
            "id": 1,
            "title": "Report 1",
            "has_input": False,
            "description": "Number of results, by status",
            "headers": ["Status", "Count"],
            "rows": Admin.get_report(report_id)
        }
    else:
        report = {
            "id": 2,
            "title": "Report 2",
            "has_input": True,
            "input": {
                "label": "City",
                "placeholder": "Enter a city name",
                "type": "text",
                "name": "city",
            },
            "description": "Brazilian airports within a 100km radius distance from the given city",
            "headers": ["City", "IATA", "Airport Name", "Distance", "Airport Type"],
            "rows": None
        }
    return render_template(f"./report.html.jinja", report=report)


# Essa lógica ta uma Bosta e só funciona pro Report 1 do ADMIN,
# algumas reports tem input, n sei como faremos (acho q o melhor é um template pra cada report)
@app.route("/report/<int:report_id>", methods=["POST"])
@login_required
def reports(report_id):
    user_object = session["user_object"]
    user_type = user_object["type"]

    value = request.form["value"]

    report = None
    if user_type == "ADMIN":
        report = {
            "id": 2,
            "title": "Report 2",
            "has_input": True,
            "input": {
                "label": "City",
                "placeholder": "Enter a city name",
                "type": "text",
                "name": "city",
            },
            "description": "Brazilian airports within a 100km radius distance from the given city",
            "headers": ["City", "IATA", "Airport Name", "Distance", "Airport Type"],
            "rows": Admin.get_report(report_id, value)
        }
    elif user_type == "RACINGS_TEAM":
        report = RacingTeam.get_report(report_id + 2)
    elif user_type == "DRIVER":
        report = Driver.get_report(report_id + 4)
    else:
        return redirect("/overview")

    return render_template(
        f"./report.html.jinja", report=report
    )


@app.context_processor
def context_processor():
    def get_username():
        if session.get("user_object") is None:
            return None

        return session["user_object"]["name"]

    return dict(get_username=get_username)
