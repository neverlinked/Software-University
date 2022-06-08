def calculate_field(m, i, j):
    if m[i][j] != '*':
        #left
        if j - 1 in range(len(m)) and m[i][j - 1] == '*':
            m[i][j] += 1
        #right
        if j + 1 in range(len(m)) and m[i][j + 1] == '*':
            m[i][j] += 1
        #up
        if i - 1 in range(len(m)) and m[i - 1][j] == '*':
            m[i][j] += 1
        #down
        if i + 1 in range(len(m)) and m[i + 1][j] == '*':
            m[i][j] += 1
        #upper left diagonal
        if i - 1 in range(len(m)) and j - 1 in range(len(m)) and m[i - 1][j - 1] == '*':
            m[i][j] += 1
        #upper right diagonal
        if i - 1 in range(len(m)) and j + 1 in range(len(m)) and m[i - 1][j + 1] == '*':
            m[i][j] += 1
        #lower left diagonal
        if i + 1 in range(len(m)) and j - 1 in range(len(m)) and m[i + 1][j - 1] == '*':
            m[i][j] += 1
        #lower right diagonal
        if i + 1 in range(len(m)) and j + 1 in range(len(m)) and m[i + 1][j + 1] == '*':
            m[i][j] += 1


size = int(input())
number_of_bombs = int(input())

matrix = [[0 for col in range(size)] for row in range(size)]

for _ in range(number_of_bombs):
    bomb_row, bomb_col = eval(input())
    matrix[bomb_row][bomb_col] = '*'

for row in range(size):
    for col in range(size):
        calculate_field(matrix, row, col)

for row in matrix:
    print(' '.join(str(char) for char in row))