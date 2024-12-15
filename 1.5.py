#!/usr/bin/env python3

def freq_set(lst, bad):
    """
    Create a frequency dictionary for elements in the list, excluding 'bad' items.

    Args:
        lst (list): The list of elements to analyze.
        bad (list): Items to exclude from frequency calculation.

    Returns:
        dict: A dictionary where keys are elements and values are their frequencies.
    """
    freq = {}
    for num in lst:
        if num in bad:
            continue
        elif num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    return freq


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

    # Initialize a list for items that appear only once across both lists
    bad_items = []

    # Create a combined frequency dictionary from both lists
    combined = freq_set(list1 + list2, bad_items)

    # Identify items that occur only once and add them to 'bad_items'
    for key in combined.keys():
        if combined[key] == 1:
            bad_items.append(key)

    # Generate frequency dictionaries for each list, excluding bad items
    freq1 = freq_set(list1, bad_items)
    freq2 = freq_set(list2, bad_items)

    # Calculate the final answer
    ANS = 0
    for key in freq1.keys():  # Iterate through the keys in freq1
        ANS += freq1[key] * freq2[key] * key

    # Print the final result
    print(ANS)


# Entry point for the script
if __name__ == "__main__":
    main()
