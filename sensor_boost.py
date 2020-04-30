# problem 9
from sunny_with_chance_of_asteroids import calculate_opcodes_parameter_modes, op_codes


def ninth_problem(mass_list):
    mass_list = mass_list + [0] * 10000  # todo: intialising the list with more empty items
    i = 0
    relative_base = [
        0]  # todo: using list because int is immutable and relative base has to be mutated on every iteration
    while i != -1:
        op_code, p1, p2, p3 = calculate_opcodes_parameter_modes(mass_list[i])
        if op_code == 3:
            input_signal = int(input("Enter: "))  # todo: Not working when we have to enter input more than once
        else:
            input_signal = 0
        i = op_codes[op_code](mass_list, op_code, p1, p2, p3, i, input_signal, relative_base)[0]
    return


if __name__ == '__main__':
    # print(ninth_problem([1102, 34915192, 34915192, 7, 4, 7, 99, 0]))
    # print(ninth_problem([104, 1125899906842624, 99]))
    # print(ninth_problem([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]))
    ninth_problem([109, 1, 203, 2, 204, 2, 99])
