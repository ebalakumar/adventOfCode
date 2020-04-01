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

    print(total_final_mass)
    return total_final_mass


# def second_problem(mass_list) -> object:
#     total_final_mass = 0
#     for mass in mass_list:
#         # print(mass[0])
#         int_mass = int(mass[0])
#         # final_mass = calculate_mass(int_mass)
#         # if final_mass != 0 & final_mass < 0:
#         while final_mass  != 0 & final_mass < 0:
#
#
#
#         total_final_mass += final_mass
#
#     print(total_final_mass)
#     return total_final_mass

def second_problem(mass_list) -> object:
    # print(mass_list)
    i = 0
    test_mass_list = mass_list
    print(opcode_calculator(i, mass_list))
    return 0


def opcode_calculator(i, mass_list) -> object:
    while i < len(mass_list):
        opcode = mass_list[i]
        if opcode == '1':
            mass_list[i + 3] = int(mass_list[i + 1]) + int(mass_list[i + 2])
        i += 4
    return mass_list


def main():
    my_path = os.path.abspath(os.path.dirname(__file__))
    # path = os.path.join(my_path, "input_1.csv")
    # with open(path) as f:
    #     masses_1 = list(csv.reader(f))
    # first_problem(masses_1)

    path = os.path.join(my_path, "input_2.csv")
    with open(path) as f:
        masses_2 = list(csv.reader(f))
    second_problem(masses_2[0])


main()
