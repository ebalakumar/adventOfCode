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


my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input_1.csv")
with open(path) as f:
    masses_1 = list(csv.reader(f))
print(first_problem(masses_1))

path = os.path.join(my_path, "input_2.txt")
with open(path) as f:
    masses_2 = list(map(int, list(csv.reader(f))[0]))
massValue = ','.join(str(e) for e in second_problem(masses_2))
print(massValue)
