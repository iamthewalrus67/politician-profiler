'''
Module for working with Twitter API.
'''
import requests
import os
from googlesearch import search


def get_twitter_id(politician_name):
    """Returns politician`s Twitter screen name or None if a politician
    does not have a Twitter sccount."""
    query = politician_name + " твіттер"
    for result in search(query, tld="co.in", num=3, stop=1, pause=2):
        twitter_link = result
    if "twitter.com" not in twitter_link:
        return None
    else:
        twitter_link = twitter_link[20:]
        screen_name = twitter_link.split("?")[0]
        return screen_name


class Twitter:
    def __init__(self):
        self.base_url = 'https://api.twitter.com/1.1/'
        self.headers = {
            'Authorization': f'Bearer {self.get_bearer_token()}'
        }
        self.latest_tweets = []

    def get_bearer_token(self):
        bearer_token = os.environ['TWITTER_KEY']
        return bearer_token

    def search_user(self, screen_name):
        url = self.base_url + 'users/lookup.json'
        params = {
            'screen_name': screen_name
        }
        response = requests.get(
            url, headers=self.headers, params=params)
        return response.json()

    def get_latest_tweets(self, screen_name, number=5):
        if screen_name is None:
            self.latest_tweets = None  # [None, None, None, None, None]
        else:
            url = self.base_url + 'statuses/user_timeline.json'
            params = {
                'screen_name': screen_name,
                'count': number
            }
            response = requests.get(url, headers=self.headers, params=params)
            text = response.json()
            # print(self.latest_tweets[0]["entities"]["urls"][0]["url"])
            for tweet in text:
                try:
                    link = tweet["entities"]["urls"][0]["url"]
                    content = tweet["text"].split("https")
                    if content[0]:
                        self.latest_tweets.append([content[0], link])
                except IndexError:
                    continue


# tw = Twitter()
# screen_name = get_twitter_id('Кива Ілля')
# print(screen_name)
# print(tw.get_latest_tweets(screen_name, number=10))
# print(tw.latest_tweets)
# print(len(tw.latest_tweets))
