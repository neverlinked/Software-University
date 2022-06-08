def king_location(m):
    for i in range(len(m) - 1):
        for j in range(len(m) - 1):
            if m[i][j] == 'K':
                return i, j


def is_queen_capturing(i, j):
    for index in range(1, 9):
        current_row = king_row - index * i
        current_col = king_col - index * j
        if not (0 <= current_row < 8 and 0 <= current_col < 8):
            break
        if matrix[current_row][current_col] == 'Q':
            capturing_queens.append([current_row, current_col])
            break


matrix = [[char for char in input().split()] for row in range(8)]
capturing_queens = []

king_row, king_col = king_location(matrix)

for row in range(-1, 2):
    for col in range(-1, 2):
        is_queen_capturing(row, col)

if capturing_queens:
    for queen in capturing_queens:
        print(queen)
else:
    print('The king is safe!')