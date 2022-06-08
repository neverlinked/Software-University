from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
passed_cars = 0
has_crashed = False

while True:
    line = input()

    if line == 'END':
        break

    if line == 'green':
        current_green_window = green_light_duration
        while cars and current_green_window > 0:
            car = cars.popleft()
            if current_green_window >= len(car) or current_green_window + free_window_duration >= len(car):
                passed_cars += 1
                current_green_window -= len(car)
            else:
                print('A crash happened!')
                print(f'{car} was hit at {car[current_green_window + free_window_duration]}.')
                has_crashed = True
                break
    else:
        cars.append(line)

    if has_crashed:
        break

if not has_crashed:
    print('Everyone is safe.')
    print(f'{passed_cars} total cars passed the crossroads.')