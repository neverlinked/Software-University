from collections import deque

pizza_orders = deque(int(order) for order in input().split(', '))
employees = [int(capacity) for capacity in input().split(', ')]

total_pizza_made = 0

while True:
    current_order = pizza_orders[0]
    current_employee_capacity = employees[-1]

    if current_employee_capacity >= current_order > 0 and current_order <= 10:
        total_pizza_made += current_order
        pizza_orders.popleft()
        employees.pop()

    elif current_employee_capacity < current_order > 0 and current_order <= 10:
        temp = current_order
        while current_order > 0:
            if current_order - current_employee_capacity <= 0:
                pizza_orders.popleft()
                employees.pop()
                break
            current_order -= current_employee_capacity
            pizza_orders[0] = current_order
            employees.pop()
            if not employees:
                break
            current_employee_capacity = employees[-1]
        total_pizza_made += temp

    if current_order <= 0 or current_order > 10:
        pizza_orders.popleft()

    if not employees or not pizza_orders:
        break

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza_made}')
    print(f"Employees: {', '.join(str(employee) for employee in employees)}")
else:
    print('Not all orders are completed.')
    print(f"Orders left: {', '.join(str(order) for order in pizza_orders)}")