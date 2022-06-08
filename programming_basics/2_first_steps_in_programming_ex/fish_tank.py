length = int(input())
width = int(input())
heigth = int(input())
percentage_taken_space = float(input())

tank_space = length * width * heigth
free_space = tank_space * (100 - percentage_taken_space) / 100
free_space_in_liters = free_space / 1000
print(free_space_in_liters)
