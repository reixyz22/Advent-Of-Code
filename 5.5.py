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


def sort(test, pairs):
    output = []

    # remove irrelevant rules, per this test
    new_pairs = []
    for a, b in pairs:
        if a in test and b in test:
            new_pairs.append((a, b))

    while len(output) < len(test):
        for item in test:
            big = True
            for a, b in new_pairs:
                if item == a and b not in output:
                    big = False
                    # print(f"{b} is bigger than {item}")
                    break
            if big and item not in output:
                output.insert(0, item)
                # print(f"{item} is biggest")
    return output


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

    total = 0
    for test_case in test_cases:
        correct = True
        for a, b in rules:
            if not rule_checker(a, b, test_case):
                correct = False
        if not correct:
            sortd = sort(test_case, rules)
            total += sortd[len(sortd) // 2]
    print(total)


if __name__ == '__main__':
    main()
