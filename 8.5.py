#!/usr/bin/env python3
import math


def read_input_file(file_name):
    space = []
    with open(file_name, 'r') as file:
        for line in file:
            space.append(list(line.strip()))  # Strip newlines and convert each line to a list
    return space


def unique_values(space):
    uniques = {}
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] != '.':  # Ignore the '.' character
                key = space[i][j]  # Current key
                value = (i, j)  # Current value (tuple of coordinates)
                if key not in uniques:
                    uniques[key] = [value]  # Initialize the key with a list containing the value
                else:
                    uniques[key].append(value)  # Append the value to the existing list
    return uniques


def extend_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Calculate direction vector (dx, dy)
    dx = x2 - x1
    dy = y2 - y1

    # Compute the original segment length (distance)
    length = math.sqrt(dx ** 2 + dy ** 2)

    # Normalize the direction vector
    dx /= length
    dy /= length

    # Extend in both directions by the original distance
    extended_point1 = (x1 - dx * length, y1 - dy * length)
    extended_point2 = (x2 + dx * length, y2 + dy * length)

    return extended_point1, extended_point2


def debug(bugs, file):
    printer = file[:]
    for i in range(len(printer)):
        for j in range(len(printer[i])):
            if (i, j) in bugs:
                printer[i][j] = '#'

    for i in range(len(file)):
        print(file[i])


def main():
    file = read_input_file('day8.txt')
    unique = unique_values(file)
    bounds_x = (0, len(file[0]))
    bounds_y = (0, len(file))
    count = 0
    input()
    anti_nodes = set()
    for key, values in unique.items():
        for i, value1 in enumerate(values):
            for value2 in values[i + 1:]:
                new_value1, new_value2 = extend_line(value1, value2)
                if bounds_x[0] <= new_value1[0] < bounds_x[1] and bounds_y[0] <= new_value1[1] < bounds_y[1]:
                    if new_value1 not in anti_nodes:
                        anti_nodes.add(new_value1)
                        count += 1
                if bounds_x[0] <= new_value2[0] < bounds_x[1] and bounds_y[0] <= new_value2[1] < bounds_y[1]:
                    if new_value2 not in anti_nodes:
                        anti_nodes.add(new_value2)
                        count += 1
    print(count)
    debug(anti_nodes, file)


if __name__ == "__main__":
    main()
