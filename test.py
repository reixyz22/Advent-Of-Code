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


def main():
    filename = 'day5.txt'
    rules, test_cases = read_input_file(filename)

    values = set()
    global_list = []

    for a, b in rules:
        values.add(a)
        values.add(b)

    # while len(values) > len(global_list):
    for item in values:
        big = True
        for a, b in rules:
            if item == a and b not in global_list:
                big = False
                print(f"{b} is bigger than {item}")
                break
        if big:
            global_list.insert(0, item)
    print(global_list)


if __name__ == '__main__':
    main()
