#!/usr/bin/env python3
def read_input_file(filename):
    with open(filename, 'r') as file:
        data = file.read()

    # Split the input into two sections based on blank line
    sections = data.strip().split('\n\n')

    # Process the first section (pairs separated by '|')
    pairs = [tuple(map(int, line.split('|'))) for line in sections[0].split('\n')]

    # Process the second section (groups separated by ',')
    groups = [list(map(int, group.split(','))) for group in sections[1].split('\n')]

    return pairs, groups


def rule_checker(a, b, lst):
    try:
        index_a = lst.index(a)
        index_b = lst.index(b)
    except ValueError:
        # If either a or b is not in the list, return True, the rule can't be applied here
        return True
    return index_b > index_a


def main():
    filename = 'day5.txt'
    rules, test_cases = read_input_file(filename)
    # print("Pairs:", rules)
    # print("Groups:", test_cases)

    count = 0
    total = 0
    for test_case in test_cases:
        test = True
        for a, b in rules:
            if not rule_checker(a, b, test_case):
                test = False
        if test:
            # add the middle number of the successful test case
            total += test_case[len(test_case) // 2]
            count += 1

    print(f"{count} / {len(test_cases)} tests passed")
    print(f"Total: {total}")


if __name__ == '__main__':
    main()
