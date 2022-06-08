from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    pureness = {}

    for rotation in range(k + 1):
        result = 0
        for index, num in enumerate(numbers):
            result += index * num
        if result not in pureness:
            pureness[result] = rotation
        numbers.rotate()

    highest_pureness = max(pureness)
    return f'Best pureness {highest_pureness} after {pureness[highest_pureness]} rotations'

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)