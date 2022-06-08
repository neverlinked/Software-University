strawberries_price = float(input())
kgbananas = float(input())
kgoranges = float(input())
kgraspberries = float(input())
kgstrawberries = float(input())

raspberries_price = strawberries_price / 2
oranges_price = (raspberries_price * 0.6)
bananas_price = (raspberries_price * 0.2)

raspberries_sum = kgraspberries * raspberries_price
oranges_sum = kgoranges * oranges_price
bananas_sum = kgbananas * bananas_price
strawberries_sum = strawberries_price * kgstrawberries

finalsum = raspberries_sum + oranges_sum + bananas_sum + strawberries_sum
print(finalsum)
