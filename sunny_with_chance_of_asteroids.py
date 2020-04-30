#!/usr/bin/python3


def calc_param_mode(i, mass_list, p1, p2, p3, relative_base):
    param1 = None
    param2 = None
    output = None
    if p1 is not None:
        if p1 == 0:
            param1 = mass_list[mass_list[i + 1]]
        elif p1 == 2:
            param1 = mass_list[mass_list[i + 1] + relative_base[0]]
        else:
            param1 = mass_list[i + 1]

    if p2 is not None:
        if p2 == 0:
            param2 = mass_list[mass_list[i + 2]]
        elif p2 == 2:
            param2 = mass_list[mass_list[i + 2] + relative_base[0]]
        else:
            param2 = mass_list[i + 2]

    if p3 is not None:
        if p3 == 0:
            output = mass_list[i + 3]
        elif p3 == 2:
            output = mass_list[i + 3] + relative_base[0]
        else:
            output = i + 3
    return output, param1, param2


def op_add(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3, relative_base)
    mass_list[output] = param1 + param2
    return i + 4, 0


def op_mul(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3, relative_base)
    mass_list[output] = param1 * param2
    return i + 4, 0


def op_write(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3, relative_base)
    if p1 == 2:
        mass_list[mass_list[i + 1] + relative_base[0]] = input_value
    else:
        mass_list[mass_list[i + 1]] = input_value
    return i + 2, 0


def op_show(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, None, None, relative_base)
    print(param1)
    return i + 2, param1


def op_jump_true(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3, relative_base)
    if param1 != 0:
        return param2, 0
    else:
        return i + 3, 0


def op_jump_false(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3, relative_base)
    if param1 == 0:
        return param2, 0
    else:
        return i + 3, 0


def op_less_than(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3, relative_base)
    if param1 < param2:
        mass_list[output] = 1
    else:
        mass_list[output] = 0
    return i + 4, 0


def op_equals(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3, relative_base)
    if param1 == param2:
        mass_list[output] = 1
    else:
        mass_list[output] = 0
    return i + 4, 0


def update_relative_base(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, None, None, relative_base)
    relative_base[0] = relative_base[0] + param1
    return i + 2, param1


def op_quit(mass_list, op_code, p1, p2, p3, i, input_value, relative_base):
    return -1, 0


op_codes = {
    1: op_add,
    2: op_mul,
    3: op_write,
    4: op_show,
    5: op_jump_true,
    6: op_jump_false,
    7: op_less_than,
    8: op_equals,
    9: update_relative_base,
    99: op_quit
}


def calculate_opcodes_parameter_modes(code):
    code = str(code)
    if len(code) <= 2:  # todo not handled for double digits if the tense place is not zero
        return int(code), 0, 0, 0
    elif len(code) == 3:
        return int(code[1:len(code)]), int(code[0]), 0, 0
    elif len(code) == 4:
        return int(code[2:len(code)]), int(code[1]), int(code[0]), 0
    elif len(code) == 5:
        return int(code[3:len(code)]), int(code[2]), int(code[1]), int(code[0])
    else:
        print(code)
        return


def fifth_problem(mass_list):
    i = 0
    while i != -1:
        op_code, p1, p2, p3 = calculate_opcodes_parameter_modes(mass_list[i])
        if op_code == 3:
            input_signal = int(input("Enter: "))  # todo: Not working when we have to enter input more than once
        i = op_codes[op_code](mass_list, op_code, p1, p2, p3, i, input_signal, None)[0]
    return mass_list


if __name__ == '__main__':
    print(fifth_problem([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                         27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]))
