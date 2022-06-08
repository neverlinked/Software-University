figure = input()

if figure == 'square':
    square2 = float(input())
    square3 = square2 * square2
    print(f"{square3:.3f}")

elif figure == 'rectangle':
    rectangle2 = float(input())
    rectangle3 = float(input())
    rectangle4 = rectangle2 * rectangle3
    print(f"{rectangle4:.3f}")

elif figure == 'circle':
    circle2 = float(input())
    from math import pi

    circle3 = pi * circle2 * circle2

    print(f"{circle3:.3f}")

elif figure == 'triangle':
    triangle2 = float(input())
    triangle3 = float(input())
    triangle4 = (triangle2*triangle3)/2
    print(f"{triangle4:.3f}")

