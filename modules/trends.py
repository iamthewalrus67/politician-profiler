'''
Module for working with Google Trends.
'''

from pytrends.request import TrendReq
import pandas as pd


class Trends:
    '''
    Wrapper class for pytrends library.
    '''

    def __init__(self, keywords):
        '''
        Initialize trends object.
        '''
        self.pytrends = TrendReq(hl='uk', tz=360)
        self.pytrends.build_payload(keywords)

    def interest_over_time(self):
        '''
        Get interest overt time.
        '''
        return self.pytrends.interest_over_time()

    def interest_by_region(self, resolution='COUNTRY', inc_low_vol=False):
        '''
        Get interest by region.
        '''
        return self.pytrends.interest_by_region(resolution=resolution, inc_low_vol=inc_low_vol)

    def related_topics(self):
        '''
        Get related topics.
        '''
        return self.pytrends.related_topics()

    def related_querries(self):
        '''
        Get related search querries.
        '''
        return self.pytrends.related_queries()

    def trending_searches(self, pn='ukraine'):
        '''
        Get trending searhes by country.
        '''
        return self.pytrends.trending_searches(pn=pn)

    def top_charts(self, date, hl='uk', tz=360, geo='GLOBAL'):
        '''
        Get top charts by date.
        '''
        return self.pytrends.top_charts(date, hl=hl, tz=tz, geo=geo)

    def suggestions(self, keyword):
        '''
        Get suggestions for keyword.
        '''
        return self.pytrends.suggestions(keyword)
