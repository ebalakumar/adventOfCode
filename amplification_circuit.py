import random

import sunny_with_chance_of_asteroids as fifth_problem
from itertools import permutations


def calculate_thruster_signal(mass_list):
    temp_mass_list = mass_list
    mass_list = tuple(mass_list)  # todo is this the best way to avoid mutation of list
    phase_setting_permutations = permutations([0, 1, 2, 3, 4])
    thruster_signal = []
    for phase_setting_sequence in list(phase_setting_permutations):
        output_signal = 0
        input_signal = 0
        for phase_input in phase_setting_sequence:
            temp_mass_list = list(mass_list)
            i = 0
            y = 0
            while i != -1:
                combined_inputs = [phase_input, input_signal]
                op_code, p1, p2, p3 = fifth_problem.calculate_opcodes_parameter_modes(temp_mass_list[i])
                i, output_signal = fifth_problem.op_codes[op_code](temp_mass_list,
                                                                   op_code, p1, p2, p3, i, combined_inputs[y])
                # output_signal will return non-zero for op_code 3. For the rest opcodes, 0 is returned
                if output_signal != 0:
                    input_signal = output_signal

                # When op_code is 99 output_signal has to be set the non-zero output_signal value which was
                # returned overall.
                if op_code == 99:
                    output_signal = input_signal

                # We have only two values in combined_inputs and has to be used only when op_code is 3
                if y == 0 and op_code == 3:
                    y += 1

        thruster_signal.append(output_signal)
    print(max(thruster_signal))


if __name__ == "__main__":
    calculate_thruster_signal([3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
                               1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0])
