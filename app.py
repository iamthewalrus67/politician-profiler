from WikiADT import WikiADT
from flask import Flask, render_template, request, redirect
from ArticleADT import ArticleADT
from WikiADT import WikiADT

app = Flask(__name__)

articles = []


@app.route("/")
def page():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    name = request.form["name_surname"]
    print(name)

    wiki_object = WikiADT(name)

    articles = ArticleADT(name)

    return render_template("result.html", image=wiki_object.links[1], name=name, politician_description=wiki_object.wiki_desc,
                           desc_1=articles[0][0], link_1=articles[0][1],
                           desc_2=articles[1][0], link_2=articles[1][1],
                           desc_3=articles[2][0], link_3=articles[2][1],
                           desc_4=articles[3][0], link_4=articles[3][1],
                           desc_5=articles[4][0], link_5=articles[4][1])



if __name__ == "__main__":
    app.run()