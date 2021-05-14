from flask import Flask, render_template, request
from pytrend_ex import polit_trends

app = Flask(__name__)

@app.route("/")
def page():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def form_post():
    name = request.form["Ім'я Прізвище"]
    if name:
        return render_template("success.html")
    # info = polit_trends(name)
    # return info
