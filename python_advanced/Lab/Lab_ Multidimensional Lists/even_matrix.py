rows = int(input())
matrix = [[int(n) for n in input().split(', ') if int(n) % 2 == 0] for i in range(rows)]
print(matrix)