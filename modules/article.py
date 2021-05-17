"""Abstract data type for representing an article."""


from bs4 import BeautifulSoup
import requests
from GoogleNews import GoogleNews


class ArticleADT:
    """A class for representing a news article."""

    def __init__(self, politician_name):
        """Initialize an object representing an article."""
        news = GoogleNews()
        news.setlang("uk")
        news.setencode("utf-8")
        news.setperiod("3d")
        news.search(politician_name)
        info = news.result()
        self.articles = []
        
        name, surname = politician_name.split()[0], politician_name.split()[1] 
        self.link= f"https://www.google.com/search?q=+{name}+{surname}+новини&source=lnms&tbm=isch"
    
        def get_data(self):
            r = requests.get(self.link)
            return r.text

        html_data = get_data(self)
        soup = BeautifulSoup(html_data, "html.parser")
        image_links, num = [], 0
        for item in soup.find_all("img"):
            image_links.append(item["src"])
            num += 1
            if num == 6:
                break
        
        for i in range(5):
            text = info[i]
            info_list = [text["title"], text["link"], image_links[i+1]]
            self.articles.append(info_list)
