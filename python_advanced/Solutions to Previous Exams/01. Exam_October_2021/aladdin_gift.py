from collections import deque

present_materials = [int(n) for n in input().split()]
genie_magic_levels = deque(int(n) for n in input().split())

special_presents = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while True:
    current_material = present_materials.pop()
    current_magic_level = genie_magic_levels.popleft()

    result = current_material + current_magic_level

    if result < 100:
        if result % 2 == 0:
            current_material *= 2
            current_magic_level *= 3
        else:
            current_material *= 2
            current_magic_level *= 2

    if result > 499:
        current_material /= 2
        current_magic_level /= 2

    result = current_material + current_magic_level

    if 100 <= result <= 499:
        if 100 <= result <= 199:
            special_presents['Gemstone'] += 1
        elif 200 <= result <= 299:
            special_presents['Porcelain Sculpture'] += 1
        elif 300 <= result <= 399:
            special_presents['Gold'] += 1
        elif 400 <= result <= 499:
            special_presents['Diamond Jewellery'] += 1

    if not present_materials or not genie_magic_levels:
        break

succeeded = False
if special_presents['Gemstone'] > 0 and special_presents['Porcelain Sculpture'] > 0:
    succeeded = True
elif special_presents['Gold'] > 0 and special_presents['Diamond Jewellery'] > 0:
    succeeded = True

if succeeded:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if present_materials:
    print(f"Materials left: {', '.join(str(n) for n in present_materials)}")
if genie_magic_levels:
    print(f"Magic left: {', '.join(str(n) for n in genie_magic_levels)}")

for key, value in sorted(special_presents.items()):
    if value > 0:
        print(f'{key}: {value}')