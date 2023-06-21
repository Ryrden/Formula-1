# Import of Flask and Flask Session
from flask import Flask, request, redirect, session, render_template
from flask_login import LoginManager, login_required
from flask_session import Session

# Imports of Routes Files
from .overview import overview_bp

# Import Models
from .models.user import User
from .models.admin import Admin
from .models.racing_team import RacingTeam
from .models.driver import Driver

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


@app.route("/report/<int:report_id>", methods=["GET"])
@login_required
def reports_get(report_id):
    return render_template(
        f"./reports/report{report_id}.html.jinja", user=session["user_object"]
    )


# Essa lógica ta uma Bosta e só funciona pro Report 1 do ADMIN,
# algumas reports tem input, n sei como faremos (acho q o melhor é um template pra cada report)
@app.route("/report/<int:report_id>", methods=["POST"])
@login_required
def reports(report_id, params=None):
    if report_id not in (1, 2):
        return redirect("/overview")

    user_object = session["user_object"]
    user_type = user_object["type"]

    print(user_type, report_id)

    report = None
    if user_type == "ADMIN":
        report = Admin.get_report(report_id)
    elif user_type == "RACINGS_TEAM":
        report = RacingTeam.get_report(report_id + 2)
    elif user_type == "DRIVER":
        report = Driver.get_report(report_id + 4)
    else:
        return redirect("/overview")

    return render_template(
        f"./reports/report{report_id}.html.jinja", user=user_object, report=report
    )


@app.context_processor
def context_processor():
    def get_username():
        if session.get("user_object") is None:
            return None

        return session["user_object"]["name"]

    return dict(get_username=get_username)
