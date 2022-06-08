def sum_negatives(*args):
    result = 0
    for num in args:
        if num < 0:
            result += num
    return result


def sum_positives(*args):
    result = 0
    for num in args:
        if num > 0:
            result += num
    return result


data = [int(n) for n in input().split()]
print(sum_negatives(*data))
print(sum_positives(*data))

if abs(sum_negatives(*data)) > sum_positives(*data):
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')



