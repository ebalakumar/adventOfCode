#!/usr/bin/python3


def calc_param_mode(i, mass_list, p1, p2, p3):
    if p1 == 0:
        param1 = mass_list[mass_list[i + 1]]
    else:
        param1 = mass_list[i + 1]

    if p2 == 0:
        param2 = mass_list[mass_list[i + 2]]
    else:
        param2 = mass_list[i + 2]

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
    print(mass_list[mass_list[i + 1]])
    return i + 2


def op_quit(mass_list, op_code, p1, p2, p3, i):
    return -1


op_codes = {
    1: op_add,
    2: op_mul,
    3: op_write,
    4: op_show,
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
    fifth_problem([3, 0, 4, 0, 99])
    fifth_problem([1002, 4, 3, 4, 33])
