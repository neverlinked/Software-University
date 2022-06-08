rows, columns = input().split()
matrix = [[el for el in input().split()] for row in range(int(rows))]

count_of_squares = 0

for i in range(int(rows) - 1):
    for j in range(int(columns) - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            count_of_squares += 1

print(count_of_squares)