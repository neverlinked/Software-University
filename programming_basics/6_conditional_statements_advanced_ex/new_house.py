flower = input()
count = int(input())
budget = int(input())

flower_price = 0

if flower == 'Roses':
    flower_price = 5
    if count > 80:
        flower_price = flower_price * 0.90
elif flower == 'Dahlias':
    flower_price = 3.80
    if count > 90:
        flower_price = flower_price * 0.85
elif flower == 'Tulips':
    flower_price = 2.80
    if count > 80:
        flower_price = flower_price * 0.85
elif flower == 'Narcissus':
    flower_price = 3
    if count < 120:
        flower_price = flower_price * 1.15
elif flower == 'Gladiolus':
    flower_price = 2.50
    if count < 80:
        flower_price = flower_price * 1.20

flower_price = count * flower_price

if budget >= flower_price:
    remaining_money = budget - flower_price
    print(f'Hey, you have a great garden with {count} {flower} and {remaining_money:.2f} leva left.')
elif budget < flower_price:
    needed_money = flower_price - budget
    print(f'Not enough money, you need {needed_money:.2f} leva more.')
