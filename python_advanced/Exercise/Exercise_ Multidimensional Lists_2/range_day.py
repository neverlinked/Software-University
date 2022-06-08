def move_command(row, col, direction, steps):
    if direction == 'up':
        return row - steps, col
    elif direction == 'down':
        return row + steps, col
    elif direction == 'left':
        return row, col - steps
    elif direction == 'right':
        return row, col + steps


size = 5
matrix = [[char for char in input().split()] for row in range(size)]
number_of_commands = int(input())
total_targets = 0
targets = []

current_row = 0
current_col = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'A':
            current_row, current_col = i, j
        elif matrix[i][j] == 'x':
            total_targets += 1

targets_left = total_targets

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == 'move':
        direction = command[1]
        steps = int(command[2])

        next_row, next_col = move_command(current_row, current_col, direction, steps)

        if 0 <= next_row < size and 0 <= next_col < size and matrix[next_row][next_col] == '.':
            matrix[current_row][current_col] = '.'
            current_row, current_col = next_row, next_col
            matrix[current_row][current_col] = 'A'

    elif command[0] == 'shoot':
        direction = command[1]
        bullet_row, bullet_col = current_row, current_col
        while True:
            bullet_row, bullet_col = move_command(bullet_row, bullet_col, direction, 1)

            if bullet_row < 0 or bullet_col < 0 or bullet_row >= size or bullet_col >= size:
                break

            if matrix[bullet_row][bullet_col] == 'x':
                targets_left -= 1
                matrix[bullet_row][bullet_col] = '.'
                targets.append([bullet_row, bullet_col])
                break

        if targets_left == 0:
            break

if targets_left == 0:
    print(f'Training completed! All {total_targets} targets hit.')
else:
    print(f'Training not completed! {targets_left} targets left.')

for target in targets:
    print(target)
