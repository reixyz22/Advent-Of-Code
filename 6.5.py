#!/usr/bin/env python3
import copy


def read_input_file(filename):
    space = []
    # Read the input file 'day4.txt' and store each line as a list of tiles
    with open(filename, 'r') as file:
        for line in file:
            space.append(list(line.strip()))  # Strip newlines and convert each line to a list
    return space


def finder(space):
    lst = []
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] == '^' or space[i][j] == 'v' or space[i][j] == '>' or space[i][j] == '<':
                lst.append(i)
                lst.append(j)
                return lst


def move(start, space):
    direction = "up"

    for _ in range(20000):
        if direction == "up":
            if 0 <= start[0] - 1 < len(space):  # Check bounds for "up"
                if space[start[0] - 1][start[1]] == '#':
                    direction = "right"
                else:
                    start = (start[0] - 1, start[1])  # Move up
            else:
                return False

        elif direction == "down":
            if 0 <= start[0] + 1 < len(space):  # Check bounds for "down"
                if space[start[0] + 1][start[1]] == '#':
                    direction = "left"
                else:
                    start = (start[0] + 1, start[1])  # Move down
            else:
                return False

        elif direction == "right":
            if 0 <= start[1] + 1 < len(space[0]):  # Check bounds for "right"
                if space[start[0]][start[1] + 1] == '#':
                    direction = "down"
                else:
                    start = (start[0], start[1] + 1)  # Move right
            else:
                return False

        elif direction == "left":
            if 0 <= start[1] - 1 < len(space[0]):  # Check bounds for "left"
                if space[start[0]][start[1] - 1] == '#':
                    direction = "up"
                else:
                    start = (start[0], start[1] - 1)  # Move left
            else:
                return False
    return True  # infinite loop (more than 20k steps)


def main():

    space = read_input_file('day6.txt')

    player_index = finder(space)

    loop_count = 0
    for i in range(0, len(space)):
        for j in range(0, len(space[i])):
            sub_space = copy.deepcopy(space)
            if sub_space[i][j] != '#':
                sub_space[i][j] = '#'
                if move(player_index, sub_space):
                    loop_count += 1
    print(loop_count)


if __name__ == '__main__':
    main()
