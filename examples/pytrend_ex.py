from pytrends.request import TrendReq
from pprint import pprint

pytrends = TrendReq(hl='uk', tz=360)

key_words = ['Зеленський']

pytrends.build_payload(key_words)

# data_frame1 = pytrends.interest_over_time()
# print(data_frame1.head())
# print('---------------')

# data_frame2 = pytrends.get_historical_interest(key_words, year_start = 2021, month_start=1, day_start=1, year_end=2021, month_end=1, day_end=10, sleep=1)
# print(data_frame2.head())
# print('---------------')

# data_frame3 = pytrends.related_topics()
# print(data_frame3)
# print('---------------')

# data_frame4 = pytrends.interest_by_region(resolution='COUNTRY')
# print(data_frame4)
# print('---------------')

# data_frame6 = pytrends.suggestions('володимир зеленський')
# print(data_frame6)
