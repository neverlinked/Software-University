trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = puzzle_count * 2.60
dolls_price = dolls_count * 3
bears_price = bears_count * 4.10
minions_price = minions_count * 8.20
trucks_price = trucks_count * 2

ordered_toys_count = puzzle_count + dolls_count + bears_count + minions_count + trucks_count
ordered_toys_price = puzzle_price + dolls_price + bears_price + minions_price + trucks_price
if ordered_toys_count >= 50:                          # if the toys are over 50, there's a 25% discount
    discounted_price = ordered_toys_price * 0.75
elif ordered_toys_count < 50:
    discounted_price = ordered_toys_price

final_price = discounted_price * 0.90                # because 10% need to be paid for the store rent

if final_price >= trip_price:
    print(f"Yes! {final_price - trip_price:.2f} lv left.")
elif final_price < trip_price:
    needed_money = trip_price - final_price
    print(f"Not enough money! {needed_money:.2f} lv needed.")
