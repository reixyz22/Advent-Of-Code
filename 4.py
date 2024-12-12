space = []
match = 0

with open('day4.txt', 'r') as file:
    for line in file:
        space.append(list(line.strip()))  # Added strip() to remove newline characters

# Horizontal and horizontal backwards
for i in range(len(space)):
    for j in range(len(space[i]) - 3):
        if (space[i][j] == 'X' and space[i][j+1] == 'M' and space[i][j+2] == 'A' and space[i][j+3] == 'S') or \
           (space[i][j] == 'S' and space[i][j+1] == 'A' and space[i][j+2] == 'M' and space[i][j+3] == 'X'):
            match += 1

# Vertical and vertical backwards
for i in range(len(space) - 3):
    for j in range(len(space[i])):
        if (space[i][j] == 'X' and space[i+1][j] == 'M' and space[i+2][j] == 'A' and space[i+3][j] == 'S') or \
           (space[i][j] == 'S' and space[i+1][j] == 'A' and space[i+2][j] == 'M' and space[i+3][j] == 'X'):
            match += 1

# Diagonal (Down and to the right) and backwards
for i in range(len(space) - 3):
    for j in range(len(space[i]) - 3):
        if (space[i][j] == 'X' and space[i+1][j+1] == 'M' and space[i+2][j+2] == 'A' and space[i+3][j+3] == 'S') or \
           (space[i][j] == 'S' and space[i+1][j+1] == 'A' and space[i+2][j+2] == 'M' and space[i+3][j+3] == 'X'):
            match += 1

# Diagonal (Down and to the left)
for i in range(len(space) - 3):
    for j in range(3, len(space[i])):
        if (space[i][j] == 'X' and space[i+1][j-1] == 'M' and space[i+2][j-2] == 'A' and space[i+3][j-3] == 'S') or \
           (space[i][j] == 'S' and space[i+1][j-1] == 'A' and space[i+2][j-2] == 'M' and space[i+3][j-3] == 'X'):
            match += 1

print(match)
