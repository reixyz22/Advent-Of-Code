#!/usr/bin/env python3

space = []  # Initialize an empty list to store the grid
match = 0  # Initialize the match counter

# Define possible matching patterns
# s * s
# * a *
# m * m
match1 = ["S", "S", "M", "M"]
# m * s
# * a *
# m * s
match2 = ["M", "S", "M", "S"]
# m * m
# * a *
# s * s
match3 = ["M", "M", "S", "S"]
# s * m
# * a *
# s * m
match4 = ["S", "M", "S", "M"]


def main():
    global match  # Access the global match variable

    # Read the input file 'day4.txt' and store each line as a list of characters
    with open('day4.txt', 'r') as file:
        for line in file:
            space.append(list(line.strip()))  # Strip newlines and convert each line to a list

    # Traverse the input grid in 3x3 chunks
    for i in range(0, len(space) - 2):
        for j in range(0, len(space[i]) - 2):
            # middle value should always be A, checking this first saves us some time
            if space[i + 1][j + 1] == 'A':
                # Extract the four corner elements from the 3x3 chunk
                sub_space = [space[i][j], space[i + 2][j], space[i][j + 2], space[i + 2][j + 2]]
                # If the corners match any of the defined patterns, increment the match counter
                if sub_space == match1 or sub_space == match2 or sub_space == match3 or sub_space == match4:
                    match += 1

    # Print the total number of matches found
    print(match)


# Call the main function
if __name__ == '__main__':
    main()
