size = int(input())
matrix = [[int(n) for n in input().split()] for rows in range(size)]

while True:
    command = input()

    if command == 'END':
        break

    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if (0 <= row <= len(matrix) - 1) and (0 <= col <= len(matrix) - 1):
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for row in matrix:
    print(' '.join(str(n) for n in row))
