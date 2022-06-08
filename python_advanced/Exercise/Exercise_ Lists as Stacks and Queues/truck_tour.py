from collections import deque

n = int(input())
petrol_pumps = deque()

for _ in range(n):
    data = [int(x) for x in input().split()]
    petrol_pumps.append(data)

for attempt in range(n):
    tank = 0
    failed = False
    for fuel, distance in petrol_pumps:
        tank += fuel

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance

    if failed:
        petrol_pumps.append(petrol_pumps.popleft())
    else:
        print(attempt)
        break
