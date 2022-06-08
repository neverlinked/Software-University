def numbers_searching(*args):
    result = []

    for num in sorted(args):
        if num + 1 not in sorted(args):
            result.append(num + 1)
            break

    duplicated_values = []
    for num in args:
        if args.count(num) >= 2:
            if num not in duplicated_values:
                duplicated_values.append(num)
    result.append(sorted(duplicated_values))

    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
