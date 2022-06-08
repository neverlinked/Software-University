rows, cols = input().split(', ')
matrix = [[int(n) for n in input().split()]for i in range(int(rows))]

for column in range(len(matrix[0])):
    column_sum = 0
    for row in matrix:
        column_sum += row[column]
    print(column_sum)