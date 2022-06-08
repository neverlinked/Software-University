from collections import deque

quantity_of_food = int(input())
orders = deque([int(n) for n in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]

    if current_order > quantity_of_food:
        break

    orders.popleft()
    quantity_of_food -= current_order

if len(orders) == 0:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join(str(n) for n in orders)}")

