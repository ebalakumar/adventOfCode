#!/usr/bin/env python
import csv
import math
import os.path
import random
from collections import Counter
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
def first_problem_part_two(mass_list, total_fuel=0):
    total_final_masses = []
    for mass in mass_list:
        int_mass = int(mass)
        total_fuel = 0
        while int_mass > 0:
            int_mass = calculate_mass(int_mass)
            total_fuel += int_mass
        total_final_masses.append(total_fuel)
    return sum(total_final_masses)


def find_verb_noun(mass_list_distinct):
    output = 0
    # output == 19690720:
    while True:
        noun = random.randint(0, 99)
        verb = random.randint(0, 99)
        temp_mass_list = list(mass_list_distinct)
        if second_problem(temp_mass_list, noun, verb) == 19690720:
            print('noun: ', noun)
            print('verb: ', verb)
            print((100 * noun) + verb)
            break


def second_problem(mass_list, noun, verb) -> object:
    # Replacing position 1 with value 12 and replace position 2 with the value 2
    mass_list[1] = noun
    mass_list[2] = verb
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
    return mass_list[0]


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
    return lowest_intersection, lowest_intersection_steps


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


def find_doubles(password):
    passwords = [char for char in password]
    unique_count_password = Counter(passwords).values()
    is_double = False
    is_more_double = False
    for count in unique_count_password:
        if count == 2:
            is_double = True
        elif count > 2:
            is_more_double = True
    return (is_double and is_more_double) or is_double


def is_sequence(password):
    j = 0
    while j < len(password) - 1:
        if password[j + 1] >= password[j]:
            flag_greater_value = True
            j += 1
        else:
            return False
    return flag_greater_value


def find_passwords(password_start_range, password_end_range):
    password_range = range(password_start_range, password_end_range)
    selected_passwords = []
    i = 0
    while i < len(password_range):
        password = str(password_range[i])
        if is_sequence(password):
            if find_doubles(password):
                selected_passwords.append(password)
        i += 1
    print(selected_passwords)
    print(len(selected_passwords))


def find_indirect_orbit(satellite_map, initial_satellite, indirect_orbit_count) -> int:
    for satellites in satellite_map:
        if initial_satellite == satellites.split(')')[1]:
            indirect_orbit_count += 1
            indirect_orbit_count = find_indirect_orbit(satellite_map, satellites.split(')')[0], indirect_orbit_count)
            break
    return indirect_orbit_count


def find_satellite_all_orbit_path(satellite_map, initial_satellite, orbit_transfer, satellite_orbit_transfer_data):
    # satellite_orbit_transfer_data = {}
    for satellites in satellite_map:
        if initial_satellite == satellites.split(')')[1]:
            satellite_orbit_transfer_data[satellites.split(')')[1]] = orbit_transfer
            orbit_transfer += 1
            satellite_orbit_transfer_data = find_satellite_all_orbit_path(satellite_map, satellites.split(')')[0],
                                                                          orbit_transfer, satellite_orbit_transfer_data)
            break
    return satellite_orbit_transfer_data


def find_direct_orbit(satellite_map, initial_satellite):
    for satellites in satellite_map:
        if initial_satellite == satellites.split(')')[1]:
            return satellites.split(')')[0]
    return None


def find_satellite_total_orbit_count(satellite_map):
    satellites_total_orbits = {}
    for satellites in satellite_map:
        name = satellites.split(')')[1]
        if name not in satellites_total_orbits:
            direct_orbit = 1
            indirect_orbit = find_indirect_orbit(satellite_map, satellites.split(')')[0], 0)
            satellites_total_orbits[name] = direct_orbit + indirect_orbit
        name = satellites.split(')')[0]
        if name not in satellites_total_orbits:
            calculate_direct_orbit = find_direct_orbit(satellite_map, name)
            if calculate_direct_orbit is not None:
                direct_orbit = 1
                indirect_orbit = find_indirect_orbit(satellite_map, calculate_direct_orbit, 0)
            else:
                direct_orbit = 0
                indirect_orbit = 0
            satellites_total_orbits[name] = direct_orbit + indirect_orbit
    count = 0
    for satellites in satellites_total_orbits:
        count += satellites_total_orbits[satellites]
    return count


def find_min_orbit_transfer(satellite_map, satellite_1, satellite_2):
    """The function is used to find the minimum number of transfer
     satellite1 has to do in order to go the orbit where satellite 2 is orbiting"""
    satellite_transfers_1 = {}
    satellite_transfers_2 = {}
    total_orbit_transfer = 0
    for satellites in satellite_map:
        if satellites.split(')')[1] == satellite_1:
            you_initial_orbit = satellites.split(')')[0]
            satellite_transfers_1 = find_satellite_all_orbit_path(satellite_map, you_initial_orbit, 0, {})
        if satellites.split(')')[1] == satellite_2:
            you_initial_orbit = satellites.split(')')[0]
            satellite_transfers_2 = find_satellite_all_orbit_path(satellite_map, you_initial_orbit, 0, {})
    for satellites in satellite_transfers_1:
        if satellite_transfers_2.get(satellites) is not None:
            total_orbit_transfer = satellite_transfers_2.get(satellites) + satellite_transfers_1[satellites]
            break
    return total_orbit_transfer


# this is the equivalent of main method
# will not be true, if this script is e.g. imported
# (helpful for unit tests)
my_path = os.path.abspath(os.path.dirname(__file__))
if __name__ == "__main__":
    num = int(input('Enter problem number: '))
    if num == 1:
        path = os.path.join(my_path, "input_1.csv")
        with open(path) as f:
            masses_1 = f.read().splitlines()
        print(first_problem(masses_1))
        print(first_problem_part_two(masses_1))

    if num == 2:
        path = os.path.join(my_path, "input_2.txt")
        with open(path) as f:
            masses_2 = list(map(int, list(csv.reader(f))[0]))
        print(find_verb_noun(tuple(masses_2)))
        print(second_problem(masses_2, 12, 2))

    if num == 3:
        path = os.path.join(my_path, "input_3.txt")
        lines = open(path).read().splitlines()
        if len(lines) > 2:
            raise ValueError('More than two inputs are not accepted. Please check the input format')
        print(third_problem(lines[0].split(','), lines[1].split(',')))

    if num == 4:
        password_range_start = 138307
        password_range_end = 654504
        find_passwords(password_range_start, password_range_end)

    if num == 6:
        path = os.path.join(my_path, "input_6.txt")
        lines = open(path).read().splitlines()
        print("Satellite's Direct and Indirect orbits :", find_satellite_total_orbit_count(lines))
        print("Minimum orbit transfer :", find_min_orbit_transfer(lines, "YOU", "SAN"))
