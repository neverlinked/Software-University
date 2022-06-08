n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]

primary_diagonal = 0
secondary_diagonal = 0

for index in range(n):
    primary_diagonal += matrix[index][index]
    secondary_diagonal += matrix[index][n - 1 - index]

result = abs(primary_diagonal - secondary_diagonal)
print(result)