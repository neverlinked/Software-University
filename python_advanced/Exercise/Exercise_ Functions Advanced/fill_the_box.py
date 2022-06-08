def fill_the_box(height, length, width, *args):
    cube_capacity = height * length * width
    cubes_left = 0

    for cube in args:
        if cube == 'Finish':
            break

        if cube > cube_capacity:
            cube -= cube_capacity
            cubes_left += cube
            cube_capacity = 0
        else:
            cube_capacity -= cube

    if cube_capacity > 0:
        return f'There is free space in the box. You could put {cube_capacity} more cubes.'
    else:
        return f'No more free space! You have {cubes_left} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))