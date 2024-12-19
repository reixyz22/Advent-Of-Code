#!/usr/bin/env python3
import re


def mul(a, b):
    return a * b


def main():
    total = 0
    # Open the file 'day3.txt' for reading
    with open('day3.txt', 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Find all occurrences of the pattern 'mul(a, b)' where a and b are numbers, using regex
            matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
            # Loop through all matches found
            for match in matches:
                total += eval(match)  # Evaluate the match as a Python expression and add to the total
    print(total)


# Call the main function
if __name__ == '__main__':
    main()
