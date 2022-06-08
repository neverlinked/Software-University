movie_budget = float(input())
actors = int(input())
clothes_price_per_actor = float(input())

actors_clothes_price = actors * clothes_price_per_actor
decoration = movie_budget * 0.1

if actors > 150:
    actors_clothes_price = actors_clothes_price * 0.90

if decoration + actors_clothes_price > movie_budget:
    needed_money = (decoration + actors_clothes_price) - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
elif decoration + actors_clothes_price <= movie_budget:
    money_left = movie_budget - (decoration + actors_clothes_price)
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
