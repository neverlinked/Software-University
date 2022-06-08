from collections import deque

quantity_of_water = int(input())
name = input()
people = deque()

while name != 'Start':
    people.append(name)
    name = input()

command = input()

while command != 'End':
    if command.isdigit():
        required_liters = int(command)
        name = people.popleft()
        if quantity_of_water >= required_liters:
            quantity_of_water -= required_liters
            print(f'{name} got water')
        else:
            print(f'{name} must wait')
    else:
        _, liters_to_refill = command.split()
        quantity_of_water += int(liters_to_refill)

    command = input()

print(f'{quantity_of_water} liters left')


