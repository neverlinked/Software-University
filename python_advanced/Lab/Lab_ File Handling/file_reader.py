try:
    with open('numbers.txt') as file:
        nums_sum = 0
        for num in file:
            nums_sum += int(num)
        print(nums_sum)
except FileNotFoundError:
    print('File was not found')