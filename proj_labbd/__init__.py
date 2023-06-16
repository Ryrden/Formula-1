from flask import Flask, render_template
from . import database

app = Flask(__name__)

@app.route("/")
def index():
    db_connection = database.DatabaseConnection()

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM airports")

    rows = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return render_template("index.html", airports=rows[:20])
