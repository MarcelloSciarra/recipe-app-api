"""Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Docstring"""

    def test_add_numbers(self):
        """Docstring"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Docstring"""
        res = calc.subtract(5, 6)
        self.assertEqual(res, 1)
