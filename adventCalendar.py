#!/usr/bin/env python
import math
import os.path
from logging import exception


# if statement can be simplified with max (inbuilt fn)
# math.floor(a / b) is same as a // b
def calculate_mass(int_mass):
    return max(0, int_mass // 3 - 2)

# Often you don't have to use loops
# this uses iterator comprehension and builtin sum function
def first_problem(mass_list):
    return sum(calculate_mass(int(input_mass)) for input_mass in mass_list)

# -> object typehint doesnt really have much use
# everything is an object
# isinstance(1, object) -> True
# isinstance(lambda x: x, object) -> True
# isinstance("asdf", object) -> True
def first_problem_part_two(mass_list, total_fuel=0) -> object:
    total_final_masses = []
    for mass in mass_list:
        int_mass = int(mass)
        total_fuel = 0
        while int_mass > 0:
            int_mass = calculate_mass(int_mass)
            total_fuel += int_mass
        total_final_masses.append(total_fuel)
    return sum(total_final_masses)


def second_problem(mass_list) -> object:
    # Replacing position 1 with value 12 and replace position 2 with the value 2
    mass_list[1] = 12
    mass_list[2] = 2
    i = 0
    while i < len(mass_list):
        opcodes = mass_list[i]
        if opcodes == 1:
            mass_list[mass_list[i + 3]] = mass_list[mass_list[i + 1]] + mass_list[mass_list[i + 2]]
        if opcodes == 2:
            mass_list[mass_list[i + 3]] = mass_list[mass_list[i + 1]] * mass_list[mass_list[i + 2]]
        if opcodes == 99:
            break
        i += 4
    return mass_list


def third_problem(red_wire, blue_wire) -> []:
    count = 0
    x = 0
    y = 0
    red_wire_path = ['0,0']
    blue_wire_path = ['0,0']
    update_path(red_wire, red_wire_path, x, y)
    update_path(blue_wire, blue_wire_path, x, y)
    # Removing initial co-ordinates
    red_wire_path.pop(0)
    blue_wire_path.pop(0)
    print(red_wire_path)
    print(blue_wire_path)
    common_coordinates = common_member(red_wire_path, blue_wire_path)
    arr_common_coordinates = []
    for coordinate in common_coordinates:
        arr_common_coordinates.append(abs(int(str(coordinate).split(',')[0])) + abs(int(str(coordinate).split(',')[1])))
    lowest_intersection_steps = find_minimum_step(common_coordinates, red_wire_path, blue_wire_path)
    lowest_intersection = min(arr_common_coordinates)
    return [lowest_intersection, lowest_intersection_steps]


def update_path(wire, wire_path, x, y):
    for input_path in wire:
        if 'R' == input_path[0]:
            count = int(input_path[1:len(input_path)])
            for value in range(count):
                x += 1
                wire_path.append(str(x) + ',' + str(y))
        if 'L' == input_path[0]:
            count = int(input_path[1:len(input_path)])
            for value in range(count):
                x -= 1
                wire_path.append(str(x) + ',' + str(y))
        if 'U' == input_path[0]:
            count = int(input_path[1:len(input_path)])
            for value in range(count):
                y += 1
                wire_path.append(str(x) + ',' + str(y))
        if 'D' == input_path[0]:
            count = int(input_path[1:len(input_path)])
            for value in range(count):
                y -= 1
                wire_path.append(str(x) + ',' + str(y))


def common_member(a, b) -> object:
    common_co_ordinates = []
    a_set = set(a)
    b_set = set(b)
    if a_set & b_set:
        common_co_ordinates = list(a_set & b_set)
    else:
        print("No common elements")
    return common_co_ordinates


def find_minimum_step(common_coordinates, red_wire_path, blue_wire_path) -> int:
    wire_intersections_steps = []
    total_steps_in_red_wire_for_intersection = 0
    total_steps_in_blue_wire_for_intersection = 0
    for common_coordinate in common_coordinates:
        total_steps_in_red_wire_for_intersection = len(red_wire_path) - 1 - red_wire_path[::-1].index(
            common_coordinate) + 1
        total_steps_in_blue_wire_for_intersection = len(blue_wire_path) - 1 - blue_wire_path[::-1].index(
            common_coordinate) + 1
        wire_intersections_steps.append(
            total_steps_in_red_wire_for_intersection + total_steps_in_blue_wire_for_intersection)
    return min(wire_intersections_steps)

# this is the equivalent of main method
# will not be true, if this script is e.g. imported
# (helpful for unit tests)
if __name__ == "__main__":
    num = 1 #int(input('Enter problem number: '))
    if num == 1:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "input_1.csv")
        with open(path) as f:
            masses_1 = f.read().splitlines()
        print(first_problem(masses_1))
        print(first_problem_part_two(masses_1))

    if num == 2:
        path = os.path.join(my_path, "input_2.txt")
        with open(path) as f:
            masses_2 = list(map(int, list(csv.reader(f))[0]))
        print(second_problem(masses_2))

    if num == 3:
        path = os.path.join(my_path, "input_3.txt")
        lines = open(path).read().splitlines()
        if len(lines) > 2:
            raise ValueError('More than two inputs are not accepted. Please check the input format')
        print(third_problem(lines[0].split(','), lines[1].split(',')))
