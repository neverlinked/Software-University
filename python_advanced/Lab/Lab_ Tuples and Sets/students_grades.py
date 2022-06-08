numbers_of_students = int(input())
students_grades = {}

for _ in range(numbers_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for data in students_grades.items():
    print(f"{data[0]} -> {' '.join([f'{grade:.2f}' for grade in data[1]])} (avg: {(sum(data[1]) / len(data[1])):.2f})")