rows, columns = [int(n) for n in input().split()]
snake = input()

index = 0
matrix = []

for row in range(rows):
    current_row = []
    for col in range(columns):
        current_row.append(snake[index % len(snake)])
        index += 1
    if row % 2 == 0:
        print(''.join(current_row))
    else:
        print(''.join(reversed(current_row)))