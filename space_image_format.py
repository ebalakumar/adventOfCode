def calculate_bios_password(wide, tall, encoded_data):
    individual_layer = []
    total_layers = []
    k = 0
    while k < len(encoded_data):
        individual_layer.clear()
        for j in range(tall):
            for i in range(wide):
                individual_layer.append(encoded_data[k])
                k += 1
        total_layers.append((find_numbers(individual_layer[:], "0"), individual_layer[:]))
    return (find_numbers(min(total_layers)[1], "1") * find_numbers(min(total_layers)[1],
                                                                   "2")), ''.join(
        decode_message(total_layers, (wide * tall)))


def find_numbers(layers, num):
    count = 0
    for i in layers:
        if i == num:
            count += 1
    return count


def decode_message(layers, total_len):
    final_layer = []
    i = 0
    while i < total_len:
        color_1 = None
        for individual_layer in layers:
            # if color_1 is None:
            #     color_1 = (individual_layer[1])[i]
            # else:
            #     color_1 = find_color_precedence(color_1, (individual_layer[1])[i])
            if (individual_layer[1])[i] == '0' or (individual_layer[1])[i] == '1':
                color_1 = (individual_layer[1])[i]
                break
            else:
                color_1 = (individual_layer[1])[i]
        final_layer.append(color_1)
        i += 1
    return final_layer


if __name__ == "__main__":
    print(calculate_bios_password(2, 2, '0222112222120000'))
