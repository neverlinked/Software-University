def recursive_power(n, power):
    if power == 0:
        return 1
    return n * recursive_power(n, power - 1)


print(recursive_power(2, 10))
