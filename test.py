import unittest

from adventCalendar import first_problem, second_problem


class Test1(unittest.TestCase):

    def test_first_Problem(self):
        self.assertEqual(first_problem([['14']]), 2)

    def test_second_Problem_1(self):
        self.assertEqual(second_problem(['1', '0', '0', '0', '99']), [2, '0', '0', '0', '99'])

    def test_second_Problem_2(self):
        self.assertEqual(second_problem(['2', '3', '0', '3', '99']), ['2', '3', '0', 6, '99'])
