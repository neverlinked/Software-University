number_of_commands = int(input())
parking_lot = set()

for _ in range(number_of_commands):
    direction, car_number = input().split(', ')

    if direction == 'IN':
        parking_lot.add(car_number)
    else:
        parking_lot.discard(car_number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print('Parking Lot is Empty')