number_of_guests = int(input())
reservations = set()

for _ in range(number_of_guests):
    reservation_code = input()
    reservations.add(reservation_code)

while True:
    incoming_guest = input()

    if incoming_guest == 'END':
        break

    reservations.remove(incoming_guest)

print(len(reservations))
print('\n'.join(sorted((reservations))))