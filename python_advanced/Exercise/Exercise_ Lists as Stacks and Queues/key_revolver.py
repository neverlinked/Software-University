from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets_stack = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())

used_bullets = 0

while locks and bullets_stack:
    current_bullet = bullets_stack.pop()
    current_lock = locks[0]

    used_bullets += 1

    if current_lock >= current_bullet:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

    if used_bullets % gun_barrel_size == 0 and bullets_stack:
        print('Reloading!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f'{len(bullets_stack)} bullets left. Earned ${value_of_intelligence - (used_bullets * price_per_bullet)}')