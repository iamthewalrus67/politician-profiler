"""
Contains example of usage of Article ADT and
Twitter ADT, Trends ADT classes
"""
import GoogleNews
import Pytrends
from flask import Flask
from article import Article
from twitter import Twitter
from trends import Trends
import request


def main():
    """
    Creates information for the site
    """

    # Get information from google about politician using GoogleNews
    politician_name = input("Enter politician's name: ")
    google = GoogleNews(lan="uk", encoding='utf-8')
    google_news = google.get_news(politician_name)
    google_search = google.search(politician_name)

    # Create instance of Article class
    info = [google_news, google_search]
    article = Article(info)
    article.set_date_time(info)
    article.set_description(info)
    article.set_link(info)
    article.set_title(info)
    article.set_media(info)
    article.set_image(info)

    # Get info from Twitter API and creates
    # instance of Twitter class
    url = ""  # twitter endpoint
    data = request.request(url)
    twitter = Twitter()
    twitter.set_name(data)
    twitter.set_screen_name(data)
    twitter.set_location(data)
    twitter.set_image(data)
    twitter.set_url(data)
    twitter.get_followers_size(data)

    #  Creates instance of Trends class
    pytrends = Pytrends(politician_name)
    trend = Trends()
    trend.get_related_topics()
    trend.draw_topics_graph()
    trend.get_historical_interest()
    trend.draw_countries()


if __name__ == "__main__":
    main()
