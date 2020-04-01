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


def main():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "input.csv")
    with open(path) as f:
        masses = list(csv.reader(f))
    first_problem(masses)
    # second_problem(masses)


main()
