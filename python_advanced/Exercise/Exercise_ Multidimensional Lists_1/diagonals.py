def primary_diagonal(m):
    result = 0
    elements = []
    for index in range(len(m)):
        result += m[index][index]
        elements.append(m[index][index])
    return result, elements


def secondary_diagonal(n, m):
    result = 0
    elements = []
    for index in range(n):
        result += m[index][n - 1 - index]
        elements.append(m[index][n - 1 - index])
    return result, elements


n = int(input())
matrix = [[int(x) for x in input().split(', ')] for row in range(n)]
first_diagonal = primary_diagonal(matrix)
second_diagonal = secondary_diagonal(n, matrix)

print(f"Primary diagonal: {', '.join(str(x) for x in first_diagonal[1])}. Sum: {first_diagonal[0]}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second_diagonal[1])}. Sum: {second_diagonal[0]}")
