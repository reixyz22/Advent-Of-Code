space = []
match = 0

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

with open('day4.txt', 'r') as file:
    for line in file:
        space.append(list(line.strip()))  # Added strip() to remove newline characters

# traverse the input space in 3x3 chunks
for i in range(0, len(space) - 2):
    for j in range(0, len(space[i]) - 2):
        # middle value should always be A, checking this first saves us some time
        if space[i + 1][j + 1] == 'A':
            # 0,0 * 2,0
            #  *  *  *
            # 0,2 * 2,2
            sub_space = [space[i][j], space[i + 2][j], space[i][j + 2], space[i + 2][j + 2]]
            if sub_space == match1 or sub_space == match2 or sub_space == match3 or sub_space == match4:
                match += 1
print(match)

