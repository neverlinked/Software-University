numbers = (float(n) for n in input().split())
occurrences = {}

for number in numbers:
    if number not in occurrences:
        occurrences[number] = 0
    occurrences[number] += 1

for data in occurrences.items():
    print(f'{data[0]:.1f} - {data[1]} times')