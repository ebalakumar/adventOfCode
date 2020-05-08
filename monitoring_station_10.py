import os
from adventCalendar import my_path


def find_position_meteor_station(asteroid_map):  # todo: refactoring needed
    asteroid_positions = []
    possible_meteor_stations = {}
    find_asteroid_positions(asteroid_map, asteroid_positions)
    for possible_meteor_station in asteroid_positions:
        possible_meteor_stations[str(possible_meteor_station)] = find_asteroids_neighbour_position_in_same_row(
            possible_meteor_station, [var for var in asteroid_positions if var[0] == possible_meteor_station[0]],
            len(asteroid_map[0]))
        for asteroid_position in asteroid_positions:
            if asteroid_position != possible_meteor_station and asteroid_position[0] != possible_meteor_station[0]:
                positions_in_between_asteroids = find_in_between_locations(possible_meteor_station, asteroid_position)
                for positions_in_between_asteroid in positions_in_between_asteroids:
                    if positions_in_between_asteroid in asteroid_positions:
                        break
                else:
                    possible_meteor_stations[str(possible_meteor_station)] = possible_meteor_stations[
                                                                                 str(possible_meteor_station)] + 1

    print(max(possible_meteor_stations, key=possible_meteor_stations.get), max(possible_meteor_stations.values()))


def find_asteroid_positions(asteroid_map, asteroid_positions):
    row = 0
    while row < len(asteroid_map):
        column = 0
        while column < len(asteroid_map[row]):
            if asteroid_map[row][column] == '#':
                asteroid_positions.append([row, column])
            column += 1
        row += 1
    return


def find_in_between_locations(p1, p2):
    in_between_locations = []
    if p1[0] > p2[0]:
        x1, y1 = p2[0], p2[1]
        x2, y2 = p1[0], p1[1]
    else:
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]

    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m * x1)
    for x in list(range(x1, x2))[1:]:
        y = (m * x) + b
        if y.is_integer():
            y = round(y)
        else:
            y = round(y, 2)
        in_between_locations.append([x, y])
    return in_between_locations


def find_asteroids_neighbour_position_in_same_row(asteroid_position, asteroid_positions_row, row_length):
    right_count = 0
    i = asteroid_position[1] + 1
    while i < row_length:
        for j in asteroid_positions_row:
            if i == j[1]:
                right_count += 1
                break
        i += 1
        if right_count > 0:
            break

    left_count = 0
    i = asteroid_position[1] - 1
    while row_length > i >= 0:
        for j in asteroid_positions_row:
            if i == j[1]:
                left_count += 1
                break
        i -= 1
        if left_count > 0:
            break
    return left_count + right_count


if __name__ == "__main__":
    path = os.path.join(my_path, "input_10_test_1.txt")
    with open(path) as f:
        lines = list(map(list, f.read().splitlines()))
    find_position_meteor_station(lines)
