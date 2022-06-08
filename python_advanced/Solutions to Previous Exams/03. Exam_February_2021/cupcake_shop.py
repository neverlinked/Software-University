from collections import deque


def stock_availability(inventory_list, command, *args):
    new_inventory_list = deque(str(item) for item in inventory_list)

    if command == 'delivery':
        for arg in args:
            new_inventory_list.append(arg)
    else:
        if args:
            numbers = [arg for arg in args if arg in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
            if numbers:
                items_sold = numbers[0]
                for _ in range(items_sold):
                    new_inventory_list.popleft()
            else:
                for item in inventory_list:
                    if item in args:
                        new_inventory_list.remove(item)
        else:
            new_inventory_list.popleft()

    return list(new_inventory_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))