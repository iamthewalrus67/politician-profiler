"""Abstract data type for representing an article."""


from GoogleNews import GoogleNews

class ArticleADT:
    """A class for representing a news article."""
    def __init__(self, politician_name, number):
        """Initialize an object representing an article."""
        news = GoogleNews()
        news.setlang("uk")
        news.setencode("utf-8")
        news.setperiod("3d")

        news.search(politician_name)

        self.info = news.result()[number]

        self.article = {}

    def set_date_time(self):
        self.article["date_time"] = self.info["date"]

    def set_description(self):
        self.article["description"] = self.info["desc"]

    def set_link(self):
        self.article["url"] = self.info["link"]

    def set_title(self):
        self.article["title"] = self.info["title"]

    def set_media(self):
        self.article["media"] = self.info["media"]

    def set_image(self):
        self.article["image"] = self.info["img"]

    def __str__(self):
        """Return information about an article as a string of key-value pairs."""
        string = ""
        if self.article.keys:
            for key in self.article.keys():
                string += key + ": " + self.article[key] + "\n"
        
        return string
