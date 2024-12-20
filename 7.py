#!/usr/bin/env python3
from itertools import product


def read_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            # Split the line into key and values
            key, values = line.split(':')
            # Convert the key to an integer and parse the values into a list of integers
            entry = [int(key.strip())] + list(map(int, values.strip().split()))
            data.append(entry)
    return data


def generate_combinations(symbols, length):
    """
    Generate all combinations of the given symbols up to the specified length.

    Parameters:
        symbols (list): The list of symbols to use for combinations.
        length (int): The length of each combination.

    Returns:
        list: A list of all combinations as strings.
    """
    return [''.join(combo) for combo in product(symbols, repeat=length)]


def solve(test_case, symbols):
    test_case = test_case[:]  # Create a copy of the list
    symbols = symbols[:]  # Create a copy of the symbols list
    for symbol in symbols:
        if symbol == '*':
            test_case[1] = test_case[1] * test_case[2]
            del test_case[2]
        else:
            test_case[1] = test_case[1] + test_case[2]
            del test_case[2]
        if test_case[1] > test_case[0]:
            break
    return test_case[1] == test_case[0]


def main():
    file = read_file('day7.txt')
    symbols = ['*', '+']

    unique_lengths = set()
    for line in file:
        if len(line) not in unique_lengths:
            unique_lengths.add(len(line))

    operator_sets = []
    for length in unique_lengths:
        operator_sets.append(generate_combinations(symbols, length - 2))

    count = 0
    for test in file:
        match = False
        operators_set = operator_sets[len(test) - min(unique_lengths)]
        for operators in operators_set:
            if solve(test, operators):
                match = True
                break
        if match:
            count += test[0]
    print(count)


if __name__ == "__main__":
    main()
