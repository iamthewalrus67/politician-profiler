"""Abstract data type for representing an article."""


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
        for i in range(5):
            text = info[i]
            info_list = [text["title"], text["link"]]
            self.articles.append(info_list)
