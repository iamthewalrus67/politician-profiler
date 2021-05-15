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

    for i in range(5):
        text = ArticleADT(name, i)
        text.set_title()
        text.set_image()
        text.set_link()
        articles.append(text.article)

    return render_template("result.html", name_surname=name, description=wiki_object.wiki_desc, \
        desc_1=articles[0]["title"], link_1=articles[0]["url"], image_1=articles[0]["image"], \
            desc_2=articles[1]["title"], link_2=articles[1]["url"], image_2=articles[1]["image"], \
            desc_3=articles[2]["title"], link_3=articles[2]["url"], image_3=articles[2]["image"], \
            desc_4=articles[3]["title"], link_4=articles[3]["url"], image_4=articles[3]["image"], \
                desc_5=articles[4]["title"], link_5=articles[4]["url"], image_5=articles[4]["image"])


if __name__ == "__main__":
    app.run()