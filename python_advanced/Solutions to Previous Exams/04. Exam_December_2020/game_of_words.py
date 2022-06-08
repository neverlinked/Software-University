text = input()
size = int(input())
matrix = [[char for char in input()] for row in range(size)]

number_of_commands = int(input())

current_row = 0
current_col = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'P':
            current_row, current_col = i, j

for _ in range(number_of_commands):
    temp_row = 0
    temp_col = 0
    direction = input()

    if direction == 'up':
        temp_row = -1
    elif direction == 'down':
        temp_row = 1
    elif direction == 'left':
        temp_col = -1
    elif direction == 'right':
        temp_col = 1

    if current_row + temp_row in range(size) and current_col + temp_col in range(size):
        matrix[current_row][current_col] = '-'
        current_row += temp_row
        current_col += temp_col
        if matrix[current_row][current_col].isalpha():
            text += matrix[current_row][current_col]
            matrix[current_row][current_col] = 'P'
    else:
        if text:
            text = text[:-1]

print(text)
for row in matrix:
    print(''.join(row))