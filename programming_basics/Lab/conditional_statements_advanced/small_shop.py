product_name = str(input())
city = str(input())
quantity = float(input())

price = 0

if city == "Sofia":
    if product_name == "coffee":
        price = 0.50
    elif product_name == "water":
        price = 0.80
    elif product_name == "beer":
        price = 1.20
    elif product_name == "sweets":
        price = 1.45
    elif product_name == "peanuts":
        price = 1.60

elif city == "Plovdiv":
    if product_name == "coffee":
        price = 0.40
    elif product_name == "water":
        price = 0.70
    elif product_name == "beer":
        price = 1.15
    elif product_name == "sweets":
        price = 1.30
    elif product_name == "peanuts":
        price = 1.50
elif city == "Varna":
    if product_name == "coffee":
        price = 0.45
    elif product_name == "water":
        price = 0.70
    elif product_name == "beer":
        price = 1.10
    elif product_name == "sweets":
        price = 1.35
    elif product_name == "peanuts":
        price = 1.55

products_price = price*quantity

print(products_price)

