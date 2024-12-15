#!/usr/bin/env python3

def is_safe(test):
    """
    Determine if the given sequence of numbers is safe.

    A sequence is safe if it strictly increases or decreases, and consecutive
    numbers differ by no more than 3.

    Args:
        test (list): A list of integers to evaluate.

    Returns:
        bool: True if the sequence is safe, False otherwise.
    """
    increase = False
    if test[0] < test[len(test) - 1]:
        increase = True

    for i in range(len(test)):

        if increase:
            if not (test[i] < test[i + 1] and (test[i + 1] - test[i]) <= 3):
                return False

        if not increase:
            if not (test[i] > test[i + 1] and (test[i] - test[i + 1]) <= 3):
                return False

        if i >= len(test) - 2:
            return True


def main():
    # Initialize a counter for safe sequences
    safe = 0

    # Open the file 'day2.txt' in read mode
    with open('day2.txt', 'r') as file:
        for line in file:
            # Split the line into individual numbers
            numbers = line.split()
            # Convert to integers
            numbers = [int(num) for num in numbers]

            # Check if the sequence is safe
            if is_safe(numbers):
                safe += 1
            else:
                # Check if removing one number makes the sequence safe
                for i in range(len(numbers)):
                    test_case = numbers[:]
                    del test_case[i]
                    if is_safe(test_case):
                        safe += 1
                        break

    # Print the total count of safe sequences
    print(safe)


# Entry point for the script
if __name__ == "__main__":
    main()
