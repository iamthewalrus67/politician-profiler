from unittest import TestCase
import unittest
from declaration import Declaration


class TestDeclaration(TestCase):
    def setUp(self):
        self.declaration1 = Declaration('Зеленський Володимир Олександрович')
        self.declaration2 = Declaration('Ляшко Олег Валерійович')

    def test_init(self):
        self.assertEqual((self.declaration1.name, type(self.declaration1.declaration_id), type(self.declaration1.declaration), type(self.declaration1.salary), type(self.declaration1.link)),
                         ('Зеленський Володимир Олександрович', str, dict, int, str))
        self.assertEqual((self.declaration2.name, type(self.declaration2.declaration_id), type(self.declaration2.declaration), type(self.declaration2.salary), type(self.declaration2.link)),
                         ('Ляшко Олег Валерійович', str, dict, int, str))

    def test_get_declaration(self):
        self.assertEqual(type(self.declaration1.get_declaration()), dict)
        self.assertEqual(type(self.declaration2.get_declaration()), dict)

    def test_get_declaration_details(self):
        self.assertEqual(
            type(self.declaration1.get_declaration_details()), dict)
        self.assertEqual(
            type(self.declaration2.get_declaration_details()), dict)

    def test_get_declaration_link(self):
        self.assertEqual(self.declaration1.get_declaration_link(
        ), 'https://public.nazk.gov.ua/documents/'+self.declaration1.declaration_id)
        self.assertEqual(self.declaration2.get_declaration_link(
        ), 'https://public.nazk.gov.ua/documents/'+self.declaration2.declaration_id)

    def test_get_salary(self):
        self.assertEqual(type(self.declaration1.get_salary()), int)
        self.assertEqual(type(self.declaration2.get_salary()), int)
