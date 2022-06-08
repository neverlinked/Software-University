from collections import deque

customers = deque(int(customer) for customer in input().split(', '))
taxis = [int(taxi) for taxi in input().split(', ')]

total_time = 0

while True:
    current_customer = customers[0]
    current_taxi = taxis[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

    if not customers or not taxis:
        break

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f"Customers left: {', '.join(str(customer) for customer in customers)}")