temp = int(input())
day_phase = (input())

outfit = ""
shoes = ""

if day_phase == 'Morning':
    if 10 <= temp <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < temp <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temp >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif day_phase == 'Afternoon':
    if 10 <= temp <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temp <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif temp >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot' 
elif day_phase == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'


print(f"It's {temp} degrees, get your {outfit} and {shoes}.")
