rows, columns = [int(n) for n in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]

while True:
    command = input()

    if command == 'END':
        break

    command = command.split()

    if command[0] == 'swap' and len(command) == 5:
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])

        if row1 >= 0 and col1 >= 0 and row2 >= 0 and col2 >= 0:
            if len(matrix) >= row1 and len(matrix) >= col1 and len(matrix) >= row2 and len(matrix) >= col2:
                first_value = matrix[row1][col1]
                second_value = matrix[row2][col2]
                matrix[row1][col1] = second_value
                matrix[row2][col2] = first_value

                for row in matrix:
                    for value in row:
                        print(value, end=' ')
                    print()
            else:
                print('Invalid input!')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
