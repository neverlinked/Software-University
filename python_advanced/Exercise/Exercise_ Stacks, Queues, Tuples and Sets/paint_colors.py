from collections import deque

data = deque(input().split())
colors = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
collected_colors = []

while data:
    first_substring = data.popleft()
    second_substring = data.pop() if data else ''

    result = first_substring + second_substring
    if result in colors:
        collected_colors.append(result)
        continue

    result = second_substring + first_substring
    if result in colors:
        collected_colors.append(result)
        continue

    first_substring = first_substring[:-1]
    second_substring = second_substring[:-1]

    if first_substring:
        data.insert(len(data) // 2, first_substring)
    if second_substring:
        data.insert(len(data) // 2, second_substring)

result = []
required_colors = {'orange': ['red', 'yellow'],
                   'purple': ['red', 'blue'],
                   'green': ['yellow', 'blue']}

for color in collected_colors:
    if color in ('red', 'blue', 'yellow'):
        result.append(color)
    else:
        is_valid = True
        for required_color in required_colors[color]:
            if required_color not in collected_colors:
                is_valid = False
                break
        if is_valid:
            result.append(color)

print(result)