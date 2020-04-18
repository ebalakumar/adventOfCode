#!/usr/bin/python3


def calc_param_mode(i, mass_list, p1, p2, p3):
    param1 = None
    param2 = None
    output = None
    if p1 is not None:
        if p1 == 0:
            param1 = mass_list[mass_list[i + 1]]
        else:
            param1 = mass_list[i + 1]

    if p2 is not None:
        if p2 == 0:
            param2 = mass_list[mass_list[i + 2]]
        else:
            param2 = mass_list[i + 2]

    if p3 is not None:
        if p3 == 0:
            output = mass_list[i + 3]
        else:
            output = i + 3
    return output, param1, param2


def op_add(mass_list, op_code, p1, p2, p3, i):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3)
    mass_list[output] = param1 + param2
    return i + 4


def op_mul(mass_list, op_code, p1, p2, p3, i):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3)
    mass_list[output] = param1 * param2
    return i + 4


def op_write(mass_list, op_code, p1, p2, p3, i):
    mass_list[mass_list[i + 1]] = int(input("Enter: "))
    return i + 2


def op_show(mass_list, op_code, p1, p2, p3, i):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, None, None)
    print(param1)
    return i + 2


def op_jump_true(mass_list, op_code, p1, p2, p3, i):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3)
    if param1 != 0:
        return param2
    else:
        return i + 3


def op_jump_false(mass_list, op_code, p1, p2, p3, i):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3)
    if param1 == 0:
        return param2
    else:
        return i + 3


def op_less_than(mass_list, op_code, p1, p2, p3, i):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3)
    if param1 < param2:
        mass_list[output] = 1
    else:
        mass_list[output] = 0
    return i + 4


def op_equals(mass_list, op_code, p1, p2, p3, i):
    output, param1, param2 = calc_param_mode(i, mass_list, p1, p2, p3)
    if param1 == param2:
        mass_list[output] = 1
    else:
        mass_list[output] = 0
    return i + 4


def op_quit(mass_list, op_code, p1, p2, p3, i):
    return -1


op_codes = {
    1: op_add,
    2: op_mul,
    3: op_write,
    4: op_show,
    5: op_jump_true,
    6: op_jump_false,
    7: op_less_than,
    8: op_equals,
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
        i = op_codes[op_code](mass_list, op_code, p1, p2, p3, i)
    return mass_list


if __name__ == '__main__':
    fifth_problem([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])
    # fifth_problem([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1])
