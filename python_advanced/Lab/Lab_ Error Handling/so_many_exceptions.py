numbers_list = [int(num) for num in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif number > 5 or number >= 10:
        result /= number

print(int(result))

#4, 5, 6, 1, 3
