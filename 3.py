#!/usr/bin/env python3
import re

total = 0  # Initialize the total sum


def mul(a, b):
    """
    Multiplies two numbers and returns the result.
    """
    return a * b


def main():
    global total  # Access the global total variable
    # Open the file 'day3.txt' for reading
    with open('day3.txt', 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Find all occurrences of the pattern 'mul(a, b)' where a and b are numbers
            matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
            # Loop through all matches found
            for match in matches:
                # Evaluate the match as a Python expression and add to the total
                total += eval(match)
    # Print the final total
    print(total)


# Call the main function
if __name__ == '__main__':
    main()
