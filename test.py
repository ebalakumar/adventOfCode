import os.path
import unittest

from adventCalendar import (first_problem, first_problem_part_two,
                            second_problem, third_problem)

my_path = os.path.abspath(os.path.dirname(__file__))


class Test1(unittest.TestCase):

    def test_first_Problem(self):
        self.assertEqual(first_problem(['14']), 2)

    def test_first_Problem(self):
        self.assertEqual(50346, first_problem_part_two(['100756']))

    def test_second_Problem_1(self):
        self.assertEqual(second_problem([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])

    def test_second_Problem_2(self):
        self.assertEqual(second_problem([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])

    def test_third_problem_1(self):
        path = os.path.join(my_path, "input_3_1.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            if len(lines) > 2:
                raise ValueError('More than two inputs are not accepted. Please check the input format')
            self.assertEqual(third_problem(lines[0].split(','), lines[1].split(','))[0], 159)

    def test_third_problem_2(self):
        path = os.path.join(my_path, "input_3_2.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            if len(lines) > 2:
                raise ValueError('More than two inputs are not accepted. Please check the input format')
            self.assertEqual(third_problem(lines[0].split(','), lines[1].split(','))[0], 135)

    def test_third_problem_3(self):
        path = os.path.join(my_path, "input_3_1.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            if len(lines) > 2:
                raise ValueError('More than two inputs are not accepted. Please check the input format')
            self.assertEqual(third_problem(lines[0].split(','), lines[1].split(','))[1], 610)

    def test_third_problem_4(self):
        path = os.path.join(my_path, "input_3_2.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            if len(lines) > 2:
                raise ValueError('More than two inputs are not accepted. Please check the input format')
            self.assertEqual(third_problem(lines[0].split(','), lines[1].split(','))[1], 410)


# unittest.main()
