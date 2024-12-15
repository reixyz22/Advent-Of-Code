#!/usr/bin/env python3
import re

total = 0


def mul(a, b):
    return a * b


with open('day3.txt', 'r') as file:
    do = True
    for line in file:
        matches = re.finditer("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        for match in matches:
            if match.group() == "don't()":
                do = False
            elif match.group() == "do()":
                do = True
            elif do:
                total += eval(match.group())
print(total)
