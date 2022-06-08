def flights(*args):
    index = 1
    flights = {}

    current_flight = ''
    for arg in args:
        if arg == 'Finish':
            break

        if index % 2 != 0:
            if arg not in flights:
                flights[arg] = 0
            current_flight = arg
        else:
            flights[current_flight] += int(arg)
        index += 1

    return flights


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))