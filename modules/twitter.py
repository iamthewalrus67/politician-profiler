'''
Module for working with Twitter API.
'''

import requests
import os


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
