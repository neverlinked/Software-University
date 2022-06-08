import sys
smallest_num = sys.maxsize

num = input()


while num != 'Stop':
    current_number = int(num)
    num = input()
    if current_number < smallest_num:
        smallest_num = current_number

print(smallest_num)
