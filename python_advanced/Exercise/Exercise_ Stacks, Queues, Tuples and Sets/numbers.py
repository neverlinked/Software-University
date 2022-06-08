first_sequence = set(int(n) for n in input().split())
second_sequence = set(int(n) for n in input().split())

n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]
    sequence = command[1]

    if action == 'Add':
        numbers = command[2:]
        if sequence == 'First':
            [first_sequence.add(int(num)) for num in numbers]
        else:
            [second_sequence.add(int(num)) for num in numbers]
    elif action == 'Remove':
        numbers = command[2:]
        if sequence == 'First':
            first_sequence = first_sequence.difference([int(num) for num in numbers])
        else:
            second_sequence = second_sequence.difference([int(num) for num in numbers])
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
