number = int(input())
entry = int(input())

total_sum = 0
total_sum += entry

while number > total_sum:
    entry = int(input())
    total_sum += entry

if total_sum >= number:
    print(total_sum)