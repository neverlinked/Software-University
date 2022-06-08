presents = int(input())
size = int(input())
matrix = [[char for char in input().split()] for row in range(size)]

total_nice_kids = 0
delivered_presents_to_nice_kids = 0

santa_row = 0
santa_col = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'S':
            santa_row = i
            santa_col = j
        elif matrix[i][j] == 'V':
            total_nice_kids += 1

while True:
    direction = input()

    if direction == 'Christmas morning':
        break

    matrix[santa_row][santa_col] = '-'

    if direction == 'up':
        santa_row -= 1
    elif direction == 'down':
        santa_row += 1
    elif direction == 'left':
        santa_col -= 1
    elif direction == 'right':
        santa_col += 1

    if matrix[santa_row][santa_col] == 'X':
        matrix[santa_row][santa_col] = '-'
    elif matrix[santa_row][santa_col] == 'V':
        presents -= 1
        delivered_presents_to_nice_kids += 1
        matrix[santa_row][santa_col] = '-'
    elif matrix[santa_row][santa_col] == 'C':
        if matrix[santa_row - 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
        if matrix[santa_row - 1][santa_col] == 'V' and presents:
            presents -= 1
            delivered_presents_to_nice_kids += 1
            matrix[santa_row - 1][santa_col] = '-'

        if matrix[santa_row + 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row + 1][santa_col] = '-'
        if matrix[santa_row + 1][santa_col] == 'V' and presents:
            presents -= 1
            delivered_presents_to_nice_kids += 1
            matrix[santa_row + 1][santa_col] = '-'

        if matrix[santa_row][santa_col - 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col - 1] = '-'
        if matrix[santa_row][santa_col - 1] == 'V' and presents:
            presents -= 1
            delivered_presents_to_nice_kids += 1
            matrix[santa_row][santa_col - 1] = '-'

        if matrix[santa_row][santa_col + 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col + 1] = '-'
        if matrix[santa_row][santa_col + 1] == 'V' and presents:
            presents -= 1
            delivered_presents_to_nice_kids += 1
            matrix[santa_row][santa_col + 1] = '-'

    matrix[santa_row][santa_col] = 'S'

    if presents == 0 or delivered_presents_to_nice_kids == total_nice_kids:
        break

if not presents and delivered_presents_to_nice_kids < total_nice_kids:
    print('Santa ran out of presents!')

for row in matrix:
    print(*row, sep=' ')

if delivered_presents_to_nice_kids == total_nice_kids:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - delivered_presents_to_nice_kids} nice kid/s.')

