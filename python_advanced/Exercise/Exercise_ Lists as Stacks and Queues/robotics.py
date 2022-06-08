from collections import deque

data = input().split(';')
h, m, s = input().split(':')
starting_time = int(h) * 3600 + int(m) * 60 + int(s)
robots = {}
busy_until_by_robot = {}
products = deque()


def convert_seconds_to_str_time(seconds):
    seconds %= 24 * 60 * 60

    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


for element in data:
    robot, processing_time = element.split('-')
    robots[robot] = int(processing_time)
    busy_until_by_robot[robot] = -1

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    current_product = products.popleft()
    starting_time += 1

    for robot, busy_until in busy_until_by_robot.items():
        if starting_time >= busy_until:
            busy_until_by_robot[robot] = starting_time + robots[robot]
            print(f'{robot} - {current_product} [{convert_seconds_to_str_time(starting_time)}]')
            break
    else:
        products.append(current_product)