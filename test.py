import os.path
import unittest
import adventCalendar

my_path = os.path.abspath(os.path.dirname(__file__))


class Test1(unittest.TestCase):

    # todo exchange the place of parameters in assertEqual function

    def test_first_problem_1(self):
        self.assertEqual(2, adventCalendar.first_problem(['14']))

    def test_first_problem_2(self):
        self.assertEqual(50346, adventCalendar.first_problem_part_two(['100756']))

    def test_second_problem_1(self):
        self.assertEqual([2, 0, 0, 0, 99], adventCalendar.second_problem([1, 0, 0, 0, 99], 0, 0))

    def test_second_problem_2(self):
        self.assertEqual([2, 4, 4, 5, 99, 9801], adventCalendar.second_problem([2, 4, 4, 5, 99, 0], 4, 4))

    def test_third_problem_1(self):
        path = os.path.join(my_path, "input_3_1.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            if len(lines) > 2:
                raise ValueError('More than two inputs are not accepted. Please check the input format')
            self.assertEqual(159, adventCalendar.third_problem(lines[0].split(','), lines[1].split(','))[0])

    def test_third_problem_2(self):
        path = os.path.join(my_path, "input_3_2.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            if len(lines) > 2:
                raise ValueError('More than two inputs are not accepted. Please check the input format')
            self.assertEqual(135, adventCalendar.third_problem(lines[0].split(','), lines[1].split(','))[0])

    def test_third_problem_3(self):
        path = os.path.join(my_path, "input_3_1.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            if len(lines) > 2:
                raise ValueError('More than two inputs are not accepted. Please check the input format')
            self.assertEqual(610, adventCalendar.third_problem(lines[0].split(','), lines[1].split(','))[1])

    def test_third_problem_4(self):
        path = os.path.join(my_path, "input_3_2.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            if len(lines) > 2:
                raise ValueError('More than two inputs are not accepted. Please check the input format')
            self.assertEqual(410, adventCalendar.third_problem(lines[0].split(','), lines[1].split(','))[1])

    def test_sixth_problem_1(self):
        path = os.path.join(my_path, "input_6_1.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            self.assertEqual(42, adventCalendar.find_satellite_total_orbit_count(lines))

    def test_sixth_problem_2(self):
        path = os.path.join(my_path, "input_6_3.txt")
        with open(path) as input_file:
            lines = input_file.read().splitlines()
            self.assertEqual(4, adventCalendar.find_min_orbit_transfer(lines, "YOU", "SAN"))
