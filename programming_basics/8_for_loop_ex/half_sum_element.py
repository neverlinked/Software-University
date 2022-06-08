import sys

n = int(input())

total_sum = 0
max_number = -sys.maxsize

for i in range(n):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

final_number = total_sum - max_number
if max_number == final_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(final_number - max_number)
    print('No')
    print(f'Diff = {diff}')
