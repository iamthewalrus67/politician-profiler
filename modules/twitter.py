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
        return twitter_link


class Twitter:
    def __init__(self):
        self.base_url = 'https://api.twitter.com/1.1/'
        self.headers = {
            'Authorization': f'Bearer {self.get_bearer_token}'
        }

    def get_bearer_token(self):
        dir_path = os.path.dirname(__file__)
        bearer_token_path = os.path.join(dir_path, '../bearer_token')

        with open(bearer_token_path, 'r') as f:
            bearer_token = f.read()

        return bearer_token

    def search_user(self, screen_name):
        url = self.base_url + 'users/lookup.json'
        params = {
            'screen_name': screen_name
        }

        response = requests.get(
            url, headers=self.headers, params=params)

        return response.json()

    def get_latest_tweets(self, screen_name):
        url = self.base_url + 'statuses/user_timeline.json'
        params = {
            'screen_name': screen_name,
            'count': 2
        }

        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
