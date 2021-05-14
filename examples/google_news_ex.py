'''
Example of GoogleNews usage.
'''

from GoogleNews import GoogleNews
from pprint import pprint

news = GoogleNews()

news.setlang('en')
news.setencode('utf-8')
news.setperiod('3d')

news.search('Programming')

info = news.result()

print(news.total_count())
print(len(info))

news.get_page(2)

info = news.result()

print(len(info))

pprint(info)