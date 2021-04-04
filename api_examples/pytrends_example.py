'''
Example of pytrends usage.
'''

from pytrends.request import TrendReq
from pprint import pprint


pytrends = TrendReq(hl='en-US', tz=360)

key_words = ['Programming']

pytrends.build_payload(key_words)

data_frame1 = pytrends.interest_over_time()
print(data_frame1.head())
print('---------------')

data_frame2 = pytrends.interest_by_region(resolution='COUNTRY')
print(data_frame2.head())
print('---------------')

data_frame3 = pytrends.related_topics()
print(data_frame3)
print('---------------')

data_frame4 = pytrends.trending_searches(pn='ukraine')
print(data_frame4.head())
print('---------------')

data_frame5 = pytrends.top_charts(date='2020')
print(data_frame5.head())
print('---------------')

data_frame6 = pytrends.suggestions('UCU')
print(data_frame6)
