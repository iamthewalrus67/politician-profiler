from pytrends.request import TrendReq


class Trends:
    def __init__(self, name: str):
        self.name = name
        self.trends = TrendReq(hl='uk', tz=360)
        self.trends.build_payload([name])

    # def get_related_topics(self):
    #     topics = self.trends.related_topics()
    #     return topics

    def get_interest_over_time(self):
        dataframe = self.trends.interest_over_time()
        return dataframe[dataframe[self.name] > 0][self.name].to_dict()

    def get_countries(self):
        dataframe = self.trends.interest_by_region()
        return dataframe[dataframe[self.name] > 0][self.name].to_dict()

    # def get_suggestions(self):
    #     return self.trends.suggestions(self.name)
