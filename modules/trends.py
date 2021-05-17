'''
Module for working with Google Trends.
'''

from pytrends.request import TrendReq
import pandas as pd


class Trends:
    def __init__(self, keywords):
        self.pytrends = TrendReq(hl='uk', tz=360)
        self.pytrends.build_payload(keywords)

    def interest_over_time(self):
        return self.pytrends.interest_over_time()

    def interest_by_region(self, resolution='COUNTRY', inc_low_vol=False):
        return self.pytrends.interest_by_region(resolution=resolution, inc_low_vol=inc_low_vol)

    def related_topics(self):
        return self.pytrends.related_topics()

    def related_querries(self):
        return self.pytrends.related_queries()

    def trending_searches(self, pn='ukraine'):
        return self.pytrends.trending_searches(pn=pn)

    def top_charts(self, date, hl='uk', tz=360, geo='GLOBAL'):
        return self.pytrends.top_charts(date, hl=hl, tz=tz, geo=geo)

    def suggestions(self, keyword):
        return self.pytrends.suggestions(keyword)
