safe = 0


def is_safe(test):
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


with open('day2.txt', 'r') as file:
    for line in file:
        # Split the line into individual numbers
        numbers = line.split()
        # Convert to integers
        numbers = [int(num) for num in numbers]
        if is_safe(numbers):
            safe += 1
        # part 2
        else:
            for i in range(len(numbers)):
                test_case = numbers[:]
                del test_case[i]
                if is_safe(test_case):
                    safe += 1
                    break

print(safe)
