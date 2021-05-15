from flask import Flask, render_template, request, redirect
from ArticleADT import ArticleADT

app = Flask(__name__)

articles = []

@app.route("/")
def page():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    name = request.form["name_surname"]

    for i in range(4):
        text = ArticleADT(name, i)
        text.set_date_time()
        text.set_title()
        text.set_description()
        text.set_media()
        articles.append(str(text))

    return render_template("success.html", politician_name=name, articles=articles)

if __name__ == "__main__":
    app.run()