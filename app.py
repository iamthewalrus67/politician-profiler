from WikiADT import WikiADT
from flask import Flask, render_template, request, redirect
from ArticleADT import ArticleADT
from WikiADT import WikiADT
from modules.trends import Trends

app = Flask(__name__)

articles = []


@app.route("/")
def page():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    name = request.form["name_surname"]

    wiki_object = WikiADT(name)

    articles = ArticleADT(name).articles

    trends = Trends([name.lower()])
    interest = trends.interest_over_time()
    dates = [str(i).split('T')[0]
             for i in list(interest.index.values)][-20:]
    popularity_level = interest[name.lower()].tolist()[-20:]

    return render_template("result.html", image=wiki_object.links, name=name, politician_description=wiki_object.wiki_desc,
                           desc_1=articles[0][0], link_1=articles[0][1], image_1=articles[0][2],
                           desc_2=articles[1][0], link_2=articles[1][1], image_2=articles[1][2],
                           desc_3=articles[2][0], link_3=articles[2][1], image_3=articles[2][2],
                           desc_4=articles[3][0], link_4=articles[3][1], image_4=articles[3][2],
                           desc_5=articles[4][0], link_5=articles[4][1], image_5=articles[4][2],
                           popularity_level=popularity_level, dates=dates)


if __name__ == "__main__":
    app.run(debug=True)
