def sum_column(m, column):
    column_sum = 0
    for row in range(len(m)):
        if m[row][column].isdigit():
            column_sum += int(m[row][column])
    return column_sum


size = 6
matrix = [[char for char in input().split()] for row in range(size)]

score = 0
for _ in range(3):
    coordinates = eval(input())
    row = coordinates[0]
    col = coordinates[1]

    if row in range(size) and col in range(size):
        if matrix[row][col] == 'B':
            added_score = sum_column(matrix, col)
            score += added_score
            matrix[row][col] = 0

if score < 100:
    print(f'Sorry! You need {100 - score} points more to win a prize.')
else:
    price = ''
    if 100 <= score <= 199:
        price = 'Football'
    elif 200 <= score <= 299:
        price = 'Teddy Bear'
    elif score >= 300:
        price = 'Lego Construction Set'
    print(f"Good job! You scored {score} points, and you've won {price}.")


