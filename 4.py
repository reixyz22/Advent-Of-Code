#!/usr/bin/env python3

def main():
    space = []  # Initialize an empty list to store the grid
    match = 0  # Initialize the match counter

    # Read the input file 'day4.txt' and store each line as a list of characters
    with open('day4.txt', 'r') as file:
        for line in file:
            space.append(list(line.strip()))  # Strip newlines and convert each line to a list

    # Horizontal and horizontal backwards
    for i in range(len(space)):
        for j in range(len(space[i]) - 3):
            # Check for the pattern 'XMAS' and its reverse 'SAMX' horizontally
            if (space[i][j] == 'X' and space[i][j + 1] == 'M' and space[i][j + 2] == 'A' and space[i][j + 3] == 'S') or \
                    (space[i][j] == 'S' and space[i][j + 1] == 'A' and space[i][j + 2] == 'M' and space[i][
                        j + 3] == 'X'):
                match += 1

    # Vertical and vertical backwards
    for i in range(len(space) - 3):
        for j in range(len(space[i])):
            # Check for the pattern 'XMAS' and its reverse 'SAMX' vertically
            if (space[i][j] == 'X' and space[i + 1][j] == 'M' and space[i + 2][j] == 'A' and space[i + 3][j] == 'S') or \
                    (space[i][j] == 'S' and space[i + 1][j] == 'A' and space[i + 2][j] == 'M' and space[i + 3][
                        j] == 'X'):
                match += 1

    # Diagonal (Down and to the right) and backwards
    for i in range(len(space) - 3):
        for j in range(len(space[i]) - 3):
            # Check for the pattern 'XMAS' and its reverse 'SAMX' diagonally (down and to the right)
            if (space[i][j] == 'X' and space[i + 1][j + 1] == 'M' and space[i + 2][j + 2] == 'A' and space[i + 3][
                j + 3] == 'S') or \
                    (space[i][j] == 'S' and space[i + 1][j + 1] == 'A' and space[i + 2][j + 2] == 'M' and space[i + 3][
                        j + 3] == 'X'):
                match += 1

    # Diagonal (Down and to the left)
    for i in range(len(space) - 3):
        for j in range(3, len(space[i])):
            # Check for the pattern 'XMAS' and its reverse 'SAMX' diagonally (down and to the left)
            if (space[i][j] == 'X' and space[i + 1][j - 1] == 'M' and space[i + 2][j - 2] == 'A' and space[i + 3][
                j - 3] == 'S') or \
                    (space[i][j] == 'S' and space[i + 1][j - 1] == 'A' and space[i + 2][j - 2] == 'M' and space[i + 3][
                        j - 3] == 'X'):
                match += 1

    # Print the total number of matches found
    print(match)


# Call the main function
if __name__ == '__main__':
    main()
