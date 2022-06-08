budget = float(input())
season = input()

destination = ""
cost = 0
vacation_type = ""

if season == 'summer':
    vacation_type = 'Camp'
elif season == 'winter':
    vacation_type = 'Hotel'

if budget <= 100:
    destination = 'Somewhere in Bulgaria'
    if season == 'summer':
        cost = budget * 0.3
    elif season == 'winter':
        cost = budget * 0.7
    if season == 'summer':
        vacation_type = 'Camp'
    elif season == 'winter':
        vacation_type = 'Hotel'

elif budget <= 1000:
    destination = 'Somewhere in Balkans'
    if season == 'summer':
        cost = budget * 0.4
    elif season == 'winter':
        cost = budget * 0.8
    if season == 'summer':
        vacation_type = 'Camp'
    elif season == 'winter':
        vacation_type = 'Hotel'
elif budget > 1000:
    destination = 'Somewhere in Europe'
    cost = budget * 0.9
    vacation_type = 'Hotel'
paid_price = budget - cost

print (destination)
print(f'{vacation_type} - {cost:.2f}')
