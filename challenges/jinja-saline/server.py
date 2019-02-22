import os
from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

here = os.path.dirname(os.path.abspath(__file__))
flag_path = os.path.join(here, "flag")

@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("login.html")
    else:
        page = """<!DOCTYPE html>
<html>
  <head>
    <title>Welcome</title>
  </head>
  <body>
    <h1>Welcome, """ + request.form["username"] + """.</h1>
  </body>
</html>
"""
        return render_template_string(page, dir=dir)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5007)
