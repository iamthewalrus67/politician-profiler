from WikiADT import WikiADT
from flask import Flask, render_template, request, redirect
from ArticleADT import ArticleADT
from WikiADT import WikiADT
from modules.trends import Trends
from modules import check_database
from modules.declaration import Declaration

app = Flask(__name__)

articles = []


@app.route("/")
def page():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    name = request.form["name_surname"]

    check_if_politicain_exists = check_database.check_all_politicians(name)
    if check_if_politicain_exists is False:
        return render_template('error.html')

    vorishki, progulshiki, knopkodavu = check_database.check_politician(name)
    thief, absentee, cheater = "", "", ""
    if vorishki:
        thief = "❌"
    if progulshiki:
        absentee = "❌"
    if knopkodavu:
        cheater = "❌"

    wiki_object = WikiADT(name)

    articles = ArticleADT(name).articles

    trends = Trends([name.lower()])
    interest = trends.interest_over_time()
    dates = [str(i).split('T')[0]
             for i in list(interest.index.values)][-20:]
    popularity_level = interest[name.lower()].tolist()[-20:]

    declaration = Declaration(name)

    return render_template("result.html", image=wiki_object.links[1], name=name, politician_description=wiki_object.wiki_desc,
                           desc_1=articles[0][0], link_1=articles[0][1], image_1=articles[0][2],
                           desc_2=articles[1][0], link_2=articles[1][1], image_2=articles[1][2],
                           desc_3=articles[2][0], link_3=articles[2][1], image_3=articles[2][2],
                           desc_4=articles[3][0], link_4=articles[3][1], image_4=articles[3][2],
                           desc_5=articles[4][0], link_5=articles[4][1], image_5=articles[4][2], popularity_level=popularity_level, dates=dates,
                           absentee=absentee, cheater=cheater, thief=thief, declaration_link=declaration.link,
                           salary='{:,}'.format(declaration.salary).replace(',', ' '))



if __name__ == "__main__":
    app.run(debug=True)
