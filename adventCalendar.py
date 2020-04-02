import csv
import math
import os.path


def calculate_mass(int_mass):
    return math.floor((int_mass / 3)) - 2


def first_problem(mass_list) -> object:
    total_final_mass = 0
    for mass in mass_list:
        # print(mass[0])
        int_mass = int(mass[0])
        final_mass = calculate_mass(int_mass)
        total_final_mass += final_mass
    return total_final_mass


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


def third_problem(red_wire, blue_wire) -> int:
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
    common_coordinates = common_member(red_wire_path, blue_wire_path)
    arr_common_coordinates = []
    for coordinate in common_coordinates:
        arr_common_coordinates.append(abs(int(str(coordinate).split(',')[0]))+abs(int(str(coordinate).split(',')[1])))
    return min(arr_common_coordinates)


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


my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input_1.csv")
with open(path) as f:
    masses_1 = list(csv.reader(f))
print(first_problem(masses_1))

path = os.path.join(my_path, "input_2.txt")
with open(path) as f:
    masses_2 = list(map(int, list(csv.reader(f))[0]))
print(second_problem(masses_2))

path = os.path.join(my_path, "input_3.txt")
lines = open(path).read().splitlines()
if len(lines) > 2:
    raise ValueError('More than two inputs are not accepted. Please check the input format')
print(third_problem(lines[0].split(','), lines[1].split(',')))
