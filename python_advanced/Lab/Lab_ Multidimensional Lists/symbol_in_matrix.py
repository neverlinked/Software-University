n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

symbol = input()
is_found = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            is_found = True
            print(f'({row}, {col})')
            break

    if is_found:
        break

if not is_found:
    print(f'{symbol} does not occur in the matrix')