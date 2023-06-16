from flask import Flask, render_template
from . import database

app = Flask(__name__)

@app.route("/css/<path:path>")
def css(path):
    return app.send_static_file("css/" + path)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/airports")
def airports():
    db_connection = database.DatabaseConnection()

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM airports")

    rows = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return render_template("index.html", airports=rows[:20])