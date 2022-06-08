def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    previous_row = [1, 1]
    for row in range(2, n):
        next_row = []
        for index in range(row):
            if index == 0:
                next_row.append(1)
            else:
                next_row.append(previous_row[index - 1] + previous_row[index])
        next_row.append(1)
        triangle.append(next_row)
        previous_row = next_row
    return triangle


print(get_magic_triangle(10))


# [     [1],
#      [1, 1],
#     [1, 2, 1],
#    [1, 3, 3, 1],
#   [1, 4, 6, 4, 1]]
