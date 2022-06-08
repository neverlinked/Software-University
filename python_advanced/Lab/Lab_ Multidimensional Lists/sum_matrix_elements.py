rows, columns = input().split(', ')
matrix = []
result = 0

for _ in range(int(rows)):
    column = [int(n) for n in input().split(', ')]
    matrix.append(column)
    result += sum(column)

print(result)
print(matrix)