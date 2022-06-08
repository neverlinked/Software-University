size = int(input())
matrix = [[char for char in input().split()] for row in range(size)]
start_row = 0
start_col = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'A':
            start_row, start_col = i, j

tea_bags = 0
is_partying = False

while True:
    matrix[start_row][start_col] = '*'

    if tea_bags >= 10:
        is_partying = True
        break

    move_command = input()

    if move_command == 'up':
        start_row -= 1
    elif move_command == 'down':
        start_row += 1
    elif move_command == 'left':
        start_col -= 1
    elif move_command == 'right':
        start_col += 1

    if start_row < 0 or start_col < 0 or start_row >= size or start_col >= size:
        break

    if matrix[start_row][start_col] == 'R':
        matrix[start_row][start_col] = '*'
        break

    if matrix[start_row][start_col].isdigit():
        tea_bags += int(matrix[start_row][start_col])

if not is_partying:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(' '.join(row))
