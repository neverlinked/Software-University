n = int(input())
even_set = set()
odd_set = set()

current_row = 1

for _ in range(n):
    name = input()
    sum_of_ascii = 0

    for char in name:
        sum_of_ascii += ord(char)

    sum_of_ascii = sum_of_ascii // current_row

    if sum_of_ascii % 2 == 0:
        even_set.add(sum_of_ascii)
    else:
        odd_set.add(sum_of_ascii)

    current_row += 1

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    result = odd_set.union(even_set)
    print(', '.join([str(x) for x in result]))
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
    print(', '.join([str(x) for x in result]))
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
    print(', '.join([str(x) for x in result]))

