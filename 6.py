#!/usr/bin/env python3

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
    count = 1
    direction = "up"
    while True:
        if direction == "up":
            if 0 <= start[0] - 1 < len(space):  # Check bounds for "up"
                if space[start[0] - 1][start[1]] == '#':
                    direction = "right"
                else:
                    if space[start[0] - 1][start[1]] != 'X':
                        space[start[0] - 1][start[1]] = 'X'
                        count += 1
                    start = (start[0] - 1, start[1])  # Move up
            else:
                print(count)
                quit()

        elif direction == "down":
            if 0 <= start[0] + 1 < len(space):  # Check bounds for "down"
                if space[start[0] + 1][start[1]] == '#':
                    direction = "left"
                else:
                    if space[start[0] + 1][start[1]] != 'X':
                        space[start[0] + 1][start[1]] = 'X'
                        count += 1
                    start = (start[0] + 1, start[1])  # Move down
            else:
                print(count)
                quit()

        elif direction == "right":
            if 0 <= start[1] + 1 < len(space[0]):  # Check bounds for "right"
                if space[start[0]][start[1] + 1] == '#':
                    direction = "down"
                else:
                    if space[start[0]][start[1] + 1] != 'X':
                        space[start[0]][start[1] + 1] = 'X'
                        count += 1
                    start = (start[0], start[1] + 1)  # Move right
            else:
                print(count)
                quit()

        elif direction == "left":
            if 0 <= start[1] - 1 < len(space[0]):  # Check bounds for "left"
                if space[start[0]][start[1] - 1] == '#':
                    direction = "up"
                else:
                    if space[start[0]][start[1] - 1] != 'X':
                        space[start[0]][start[1] - 1] = 'X'
                        count += 1
                    start = (start[0], start[1] - 1)  # Move left
            else:
                print(count)
                quit()


def main():

    space = read_input_file('day6.txt')

    player_index = finder(space)
    space[player_index[0]][player_index[1]] = "X"
    move(player_index, space)


if __name__ == '__main__':
    main()
