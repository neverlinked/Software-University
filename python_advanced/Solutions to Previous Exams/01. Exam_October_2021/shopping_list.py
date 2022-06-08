def shopping_list(budget, **kwargs):

    if budget < 100:
        return 'You do not have enough budget.'

    result = ''
    shopping_basket = 5

    while True:
        for product, values in kwargs.copy().items():
            price, quantity = values
            if budget >= price * quantity:
                budget -= price * quantity
                shopping_basket -= 1
                result += f'You bought {product} for {(price * quantity):.2f} leva.\n'

                if shopping_basket == 0:
                    break

                if not kwargs:
                    break

            del kwargs[product]

        if shopping_basket == 0:
            break

        if not kwargs:
            break

    return result.rstrip()

print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))


print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))