from unittest import TestCase
import unittest
from check_database import *


class TestCheckDatabase(TestCase):
    def test_check_all_politicians(self):
        self.assertEqual(check_all_politicians(
            'Володимир Зеленський'), (True, 'Зеленський Володимир Олександрович'))
        self.assertEqual(check_all_politicians(
            'Джон Леннон'), (False, None))

    def test_check_knopkodavu(self):
        self.assertEqual(check_knopkodavu('Володимир Зеленський'), False)
        self.assertEqual(check_knopkodavu('Тетяна Чорновол'), True)

    def test_check_progulshiki(self):
        self.assertEqual(check_progulshiki('Володимир Зеленський'), False)
        self.assertEqual(check_progulshiki('Тетяна Чорновол'), True)

    def test_check_vorishki(self):
        self.assertEqual(check_vorishki('Володимир Зеленський'), False)
        self.assertEqual(check_vorishki('Ілля Кива'), True)
