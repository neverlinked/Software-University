def sum_odds(*args):
    odds = 0
    for num in args:
        if num % 2 != 0:
            odds += num
    return len(args) * odds


def sum_evens(*args):
    evens = 0
    for num in args:
        if num % 2 == 0:
            evens += num
    return len(args) * evens


command = input()
integers = [int(num) for num in input().split()]

if command == 'Odd':
    print(sum_odds(*integers))
else:
    print(sum_evens(*integers))