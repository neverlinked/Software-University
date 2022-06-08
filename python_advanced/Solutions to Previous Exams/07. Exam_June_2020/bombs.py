from collections import deque

bomb_effects = deque(int(effect) for effect in input().split(', '))
bomb_casings = [int(casing) for casing in input().split(', ')]

bomb_pouch = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
is_fulfilled = False

while True:
    current_effect = bomb_effects[0]
    current_casing = bomb_casings[-1]

    if current_effect + current_casing == 40:
        bomb_pouch['Datura Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif current_effect + current_casing == 60:
        bomb_pouch['Cherry Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif current_effect + current_casing == 120:
        bomb_pouch['Smoke Decoy Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if not bomb_effects or not bomb_casings:
        break

    if bomb_pouch['Datura Bombs'] >= 3 and bomb_pouch['Cherry Bombs'] >= 3 and bomb_pouch['Smoke Decoy Bombs'] >= 3:
        is_fulfilled = True
        break

if is_fulfilled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print('Bomb Effects: empty')
else:
    print(f"Bomb Effects: {', '.join(str(effect) for effect in bomb_effects)}")

if not bomb_casings:
    print('Bomb Casings: empty')
else:
    print(f"Bomb Casings: {', '.join(str(casing) for casing in bomb_casings)}")

for bomb, quantity in sorted(bomb_pouch.items()):
    print(f'{bomb}: {quantity}')