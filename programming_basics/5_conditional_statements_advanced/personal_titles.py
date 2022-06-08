age = int(input())
gender = str(input())

if gender == 'f':
    if age < 16:
        print('Miss')
    else:
        print("Ms.")

if gender == "m":
    if age < 16:
        print('Master')
    else:
        print("Mr.")
