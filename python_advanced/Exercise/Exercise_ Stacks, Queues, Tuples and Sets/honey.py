from collections import deque

working_bees = deque(int(bee) for bee in input().split())
nectar_stack = [int(n) for n in input().split()]
symbols = deque(input().split())

honey_made = 0

while working_bees and nectar_stack:
    bee = working_bees[0]
    nectar = nectar_stack.pop()

    if nectar < bee:
        continue

    working_bees.popleft()
    current_symbol = symbols.popleft()
    if nectar >= bee:
        if current_symbol == '+':
            honey_made += abs(bee + nectar)
        elif current_symbol == '-':
            honey_made += abs(bee - nectar)
        elif current_symbol == '*':
            honey_made += abs(bee * nectar)
        elif current_symbol == '/' and nectar > 0:
            honey_made += abs(bee / nectar)

print(f'Total honey made: {honey_made}')
if working_bees:
    print(f"Bees left: {', '.join(str(bee) for bee in working_bees)}")
if nectar_stack:
    print(f"Nectar left: {', '.join(str(n) for n in nectar_stack)}")
