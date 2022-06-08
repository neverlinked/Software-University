n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]

diagonal = 0

for row in range(n):
    for col in range(n):
        if row == col:
            diagonal += matrix[row][col]

print(diagonal)
