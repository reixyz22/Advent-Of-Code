#!/usr/bin/env python3

def main():
    # Initialize two empty lists to store numbers
    list1 = []
    list2 = []

    # Open the file 'day1.txt' in read mode
    with open('day1.txt', 'r') as file:
        for line in file:
            # Split the line into individual numbers
            numbers = line.split()
            # Convert the numbers to integers and store them in the lists
            numbers = [int(num) for num in numbers]
            list1.append(numbers[0])
            list2.append(numbers[1])

    # Sort both lists in ascending order
    list1 = sorted(list1)
    list2 = sorted(list2)

    # Initialize a variable to store the total of differences
    total = 0

    # Calculate the absolute differences and sum them
    for i in range(len(list1)):
        difference = abs(list1[i] - list2[i])
        total += difference

    # Print the total
    print(total)


# Entry point for the script
if __name__ == "__main__":
    main()
