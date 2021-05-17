from unittest import TestCase
import unittest
from wiki import WikiADT


class TestWiki(TestCase):
    def setUp(self):
        self.wiki = WikiADT('Володимир Зеленський')

    def test_init(self):
        self.assertEqual(type(self.wiki.wiki_desc), str)
        self.assertEqual(type(self.wiki.links), str)
