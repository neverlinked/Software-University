def bunny_coordinates(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'B':
                return row, col


def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


size = int(input())
field = [[char for char in input().split()] for row in range(size)]
bunny_row, bunny_col = bunny_coordinates(field)

directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}

best_score = float('-inf')
best_direction = ''
best_path = []

for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_score = 0
    path = []

    while True:
        current_row, current_col = step(current_row, current_col)

        if current_row < 0 or current_col < 0 or current_row >= size or current_col >= size:
            break

        if field[current_row][current_col] == 'X':
            break

        path.append([current_row, current_col])
        current_score += int(field[current_row][current_col])

    if current_score > best_score and path:
        best_score = current_score
        best_direction = direction
        best_path = path
print(best_direction)
for step in best_path:
    print(step)
print(best_score)
