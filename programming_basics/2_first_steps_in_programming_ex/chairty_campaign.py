days = int(input())
workers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

# cake - 45 lv., waffle - 5.80lv., pancake - 3.20lv.
# 1/8 of the final sum will be used to cover the company's expenses

cakes_income = cakes * 45
waffles_income = waffles * 5.80
pancakes_income = pancakes * 3.20
daily_income = (cakes_income + waffles_income + pancakes_income) * workers
campaign_gains = daily_income * days
final_gains = campaign_gains - campaign_gains / 8

print(final_gains)
