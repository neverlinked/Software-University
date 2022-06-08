from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_liters = 0

while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups.popleft() - current_bottle

    if current_cup > 0:
        cups.appendleft(current_cup)
    else:
        wasted_liters += abs(current_cup)

if bottles:
    print(f"Bottles: {' '.join(str(bottle) for bottle in reversed(bottles))}")
else:
    print(f"Cups: {' '.join(str(cup) for cup in cups)}")

print(f'Wasted litters of water: {wasted_liters}')