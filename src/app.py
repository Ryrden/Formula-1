from flask import Flask, render_template
from database import DatabaseConnection

app = Flask(__name__)

@app.route("/")
def index():
    db_connection = DatabaseConnection()

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM airports")

    rows = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return render_template("index.html", airports=rows[:20])

if __name__ == "__main__":
    app.run()