from math import floor

size = int(input())
matrix = [[char for char in input().split()] for row in range(size)]

first_position = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'P':
            first_position = (i, j)

collected_coins = 0
path = [first_position]

current_row = first_position[0]
current_col = first_position[1]
while True:
    direction = input()

    if direction == 'left':
        current_col -= 1
    elif direction == 'right':
        current_col += 1
    elif direction == 'up':
        current_row -= 1
    elif direction == 'down':
        current_row += 1

    if current_row in range(size) and current_col in range(size):
        current_position = matrix[current_row][current_col]
        if current_position.isdigit():
            collected_coins += int(current_position)
        elif current_position == 'X':
            break
        matrix[current_row][current_col] = '0'
        path.append((current_row, current_col))
    else:
        if direction == 'left':
            current_col = size - 1
        elif direction == 'right':
            current_col = 0
        elif direction == 'up':
            current_row = size - 1
        elif direction == 'down':
            current_row = 0
        current_position = matrix[current_row][current_col]
        if current_position.isdigit():
            collected_coins += int(current_position)
        elif current_position == 'X':
            break
        matrix[current_row][current_col] = '0'
        path.append((current_row, current_col))

    if collected_coins >= 100:
        break

if matrix[current_row][current_col] == 'X':
    path.append((current_row, current_col))
    collected_coins = floor(collected_coins / 2)
    print(f"Game over! You've collected {collected_coins} coins.")
else:
    print(f"You won! You've collected {collected_coins} coins.")

print('Your path:')
for step in path:
    print(f'[{step[0]}, {step[1]}]')