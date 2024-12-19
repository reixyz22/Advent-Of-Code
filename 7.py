#!/usr/bin/env python3
def read_file(file_name):
    space = []
    with open(file_name, 'r') as file:
        for line in file:
            space.append(list(line.strip()))  # Strip newlines and convert each line to a list
    return space


def main():
    read_file('day7.txt')


if __name__ == "__main__":
    main()
