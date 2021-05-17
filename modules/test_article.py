from unittest import TestCase
import unittest
from article import ArticleADT


class TestArticle(TestCase):
    def setUp(self):
        self.article = ArticleADT('Володимир Зеленський')

    def test_init(self):
        self.assertEqual(
            self.article.link, 'https://www.google.com/search?q=+Володимир+Зеленський+новини&source=lnms&tbm=isch')
        self.assertEqual(len(self.article.articles), 5)
