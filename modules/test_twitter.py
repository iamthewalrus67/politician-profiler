from unittest import TestCase
import unittest
import twitter


class TestTwitter(TestCase):
    def setUp(self):
        self.tw = twitter.Twitter()

    def test_get_twitter_id(self):
        self.assertEqual(twitter.get_twitter_id(
            'Володимир Зеленський'), 'ZelenskyyUa')

    def test_search_user(self):
        self.assertEqual(type(self.tw.search_user('ZelenskyyUa')), list)
