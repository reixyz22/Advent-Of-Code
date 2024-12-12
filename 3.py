import re

total = 0


def mul(a, b):
    return a * b


with open('day3.txt', 'r') as file:
    for line in file:
        matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
        for match in matches:
            total += eval(match)
print(total)
