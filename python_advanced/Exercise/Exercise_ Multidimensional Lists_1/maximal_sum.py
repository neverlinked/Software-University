import sys

rows, columns = [int(n) for n in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_square_sum = -sys.maxsize
max_submatrix = []

for i in range(rows - 2):
    for j in range(columns - 2):
        current_submatrix = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
                            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
                            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]

        if sum(current_submatrix) > max_square_sum:
            max_square_sum = sum(current_submatrix)
            max_submatrix = current_submatrix

print(f'Sum = {max_square_sum}')
print(max_submatrix[0], max_submatrix[1], max_submatrix[2])
print(max_submatrix[3], max_submatrix[4], max_submatrix[5])
print(max_submatrix[6], max_submatrix[7], max_submatrix[8])