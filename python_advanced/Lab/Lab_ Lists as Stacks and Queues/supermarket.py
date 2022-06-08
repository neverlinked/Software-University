from collections import deque

line = deque()

while True:
    customer = input()

    if customer == 'Paid':
        while line:
            print(line.popleft())
    else:
        if customer == 'End':
            print(f'{len(line)} people remaining.')
            break
        else:
            line.append(customer)

