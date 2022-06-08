name = input()
average_grade = 0
bad_grades = 0
is_expelled = False
grade_count = 1

while grade_count <= 12:
    grade = float(input())
    if grade < 4:
        bad_grades += 1
        if bad_grades > 1:
            is_expelled = True
            break
        else:
            continue
    grade_count += 1
    average_grade += grade

if is_expelled:
    print(f'{name} has been excluded at {grade_count} grade')
else:
    average_grade /= 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")