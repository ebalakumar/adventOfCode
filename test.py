import unittest

from adventCalendar import first_problem, second_problem


class Test1(unittest.TestCase):

    def test_first_Problem(self):
        self.assertEqual(first_problem([['14']]), 2)

    def test_second_Problem(self):
        self.assertEqual(second_problem([['1969']]), 966)
