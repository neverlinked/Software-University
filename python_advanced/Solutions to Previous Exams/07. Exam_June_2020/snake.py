size = int(input())
matrix = [[char for char in input()]for row in range(size)]

current_position = 0
for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'S':
            current_position = i, j

food_quantity = 0
is_fed = False
while True:
    command = input()
    current_row = current_position[0]
    current_col = current_position[1]
    #left
    if command == 'left':
        current_col -= 1
    #right
    elif command == 'right':
        current_col += 1
    #up
    elif command == 'up':
        current_row -= 1
    #down
    elif command == 'down':
        current_row += 1

    matrix[current_position[0]][current_position[1]] = '.'
    if current_row in range(size) and current_col in range(size):
        current_position = current_row, current_col
        if matrix[current_row][current_col] == '*':
            matrix[current_row][current_col] = 'S'
            food_quantity += 1
        elif matrix[current_row][current_col] == '-':
            matrix[current_row][current_col] = 'S'
        elif matrix[current_row][current_col] == 'B':
            matrix[current_row][current_col] = '.'
            for i in range(size):
                for j in range(size):
                    if matrix[i][j] == 'B':
                        current_row = i
                        current_col = j
                        current_position = current_row, current_col
                        matrix[current_row][current_col] = 'S'
                        continue
    else:
        break

    if food_quantity >= 10:
        is_fed = True
        break

if not is_fed:
    print('Game over!')
else:
    print('You won! You fed the snake.')
print(f'Food eaten: {food_quantity}')

for row in matrix:
    print(f"{''.join(char for char in row)}")