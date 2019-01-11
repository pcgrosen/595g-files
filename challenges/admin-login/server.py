import os
import random
import string
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

admin = "admin"
here = os.path.dirname(os.path.abspath(__file__))
flag_path = os.path.join(here, "flag")
db_path = os.path.join(here, "users.db")

def fix_database(db):
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    db.commit()

    c.execute("SELECT * FROM users WHERE username=?", (admin,))
    if not c.fetchone():
        password = "".join(random.choice(string.ascii_letters) for _ in xrange(64))
        c.execute("INSERT INTO users VALUES (?, ?)", (admin, password))
        db.commit()
    c.close()

def get_flag():
    with open(flag_path, "rb") as f:
        return f.read().strip()

@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("login.html")
    else:
        db = sqlite3.connect(db_path)
        fix_database(db)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username='%s' AND password='%s'" %
                       (request.form["username"], request.form["password"]))
        if cursor.fetchone():
            if request.form["username"] == admin:
                return render_template("flag.html", flag=get_flag())
            else:
                return "Well, you logged in, but you aren't an admin."
        else:
            return "Hey! You're not an admin!", 403

if __name__ == "__main__":
    app.run(port=5001)
