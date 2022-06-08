from sys import maxsize

rows, cols = [int(n) for n in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_square_sum = -maxsize
max_square = []
for row in range(rows - 1):
    for col in range(cols - 1):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]

        if sum(sub_matrix) > max_square_sum:
            max_square_sum = sum(sub_matrix)
            max_square = sub_matrix.copy()

print(max_square[0], max_square[1])
print(max_square[2], max_square[3])
print(max_square_sum)