def is_knight(row, col, matrix):
    return matrix[row][col] == 'K'


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def attacks_counter(row, col, matrix):
    result = 0

    if is_inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
        result += 1
    if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result += 1
    if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result += 1
    if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1
    if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result += 1
    if is_inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result += 1

    return result


size = int(input())
board = [[char for char in input()] for row in range(size)]

removed_knights = 0

while True:
    knights = {}

    for i in range(size):
        for j in range(size):
            if board[i][j] == '0':
                continue
            counter = attacks_counter(i, j, board)
            if counter:
                knights[(i, j)] = counter

    if len(knights) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0

    for coordinates, counter in knights.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coordinates[0]
            knight_col = coordinates[1]

    board[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)