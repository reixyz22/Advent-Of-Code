
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

list1 = sorted(list1)
list2 = sorted(list2)

total = 0
for i in range(len(list1)):
    difference = abs(list1[i] - list2[i])
    total += difference

print(total)
