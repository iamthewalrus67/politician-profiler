from unittest import TestCase
from trends import Trends
from pandas import DataFrame


class TestTrends(TestCase):
    def setUp(self):
        self.trends = Trends(['кива'])

    def test_interest_over_time(self):
        self.assertEqual(type(self.trends.interest_over_time()), DataFrame)

    def test_interest_by_region(self):
        self.assertEqual(type(self.trends.interest_by_region()), DataFrame)

    def test_related_topics(self):
        self.assertEqual(type(self.trends.related_topics()), dict)

    def test_related_querries(self):
        self.assertEqual(type(self.trends.related_querries()), dict)

    def test_trending_searches(self):
        self.assertEqual(type(self.trends.trending_searches()), DataFrame)

    def test_suggestions(self):
        self.assertEqual(type(self.trends.suggestions("україна")), list)
