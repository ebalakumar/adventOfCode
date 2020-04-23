def calculate_bios_password(wide, tall, encoded_data):
    individual_layer = []
    total_layers = {}
    k = 0
    while k < len(encoded_data):
        individual_layer.clear()
        for j in range(tall):
            for i in range(wide):
                individual_layer.append(encoded_data[k])
                k += 1

        total_layers[find_numbers(individual_layer[:], "0")] = individual_layer[:]
    return find_numbers(total_layers[min(total_layers)], "1") * find_numbers(total_layers[min(total_layers)], "2")


def find_numbers(layers, num):
    count = 0
    for i in layers:
        if i == num:
            count += 1
    return count


if __name__ == "__main__":
    print(calculate_bios_password(3, 2, '123456789012'))
