from collections import deque

materials_stack = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

craft_presents = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
first_pair = set()
second_pair = set()

while materials_stack and magic_values:
    current_material = materials_stack.pop()
    current_value = magic_values.popleft()

    result = current_material * current_value

    if result in (150, 250, 300, 400):
        if result == 150:
            craft_presents['Doll'] += 1
            first_pair.add('Doll')
        elif result == 250:
            craft_presents['Wooden train'] += 1
            first_pair.add('Wooden train')
        elif result == 300:
            craft_presents['Teddy bear'] += 1
            second_pair.add('Teddy bear')
        else:
            craft_presents['Bicycle'] += 1
            second_pair.add('Bicycle')
    elif result < 0:
        result = current_material + current_value
        materials_stack.append(result)
    elif result > 0:
        materials_stack.append(current_material + 15)
    elif current_material == 0 or current_value == 0:
        if current_material == 0 and current_value > 0:
            magic_values.appendleft(current_value)
        elif current_value == 0 and current_material > 0:
            materials_stack.append(current_material)

if len(first_pair) == 2 or len(second_pair) == 2:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_stack:
    print(f"Materials left: {', '.join(str(material) for material in reversed(materials_stack))}")
if magic_values:
    print(f"Magic left: {', '.join(str(value) for value in magic_values)}")

for toy, amount in sorted(craft_presents.items()):
    if amount > 0:
        print(f'{toy}: {amount}')



