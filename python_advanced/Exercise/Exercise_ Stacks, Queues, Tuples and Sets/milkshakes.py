from collections import deque

chocolates = [int(n) for n in input().split(', ')]
cups_of_milk = deque(int(n) for n in input().split(', '))

milkshakes = 0


while chocolates and cups_of_milk and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_cup = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cup <= 0:
        continue

    if current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup)
        continue

    if current_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_cup:
        milkshakes += 1
    else:
        chocolates.append(current_chocolate - 5)
        cups_of_milk.append(current_cup)


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print('Chocolate: empty')

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print('Milk: empty')