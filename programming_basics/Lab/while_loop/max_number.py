import sys
biggest_num = -sys.maxsize

num = input()


while num != 'Stop':
    current_number = int(num)
    num = input()
    if current_number > biggest_num:
        biggest_num = current_number

print(biggest_num)
