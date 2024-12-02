list1 = []
list2 = []

with open('day1.txt', 'r') as file:
    for line in file:
        # Split the line into individual numbers
        numbers = line.split()
        # Convert the numbers to integers (if required)
        numbers = [int(num) for num in numbers]
        # Add them to our lists
        list1.append(numbers[0])
        list2.append(numbers[1])


def freq_set(lst, bad):
    freq = {}
    for num in lst:
        if num in bad:
            continue
        elif num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    return freq


# a list of items which only appear one time, in one of the lists. These aren't needed for our final calculations
bad_items = []
# make a combined frequency dict
combined = freq_set(list1 + list2, bad_items)
for key in combined.keys():
    if combined[key] == 1:
        bad_items.append(key)

freq1 = freq_set(list1, bad_items)
freq2 = freq_set(list2, bad_items)


ANS = 0
for key in freq1.keys():  # Iterate through the keys in freq1
    ANS += freq1[key] * freq2[key] * key
print(ANS)
