max_fails = int(input()) #брой незадоволителни оценки

failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ''
has_failed = True

while failed_times < max_fails:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem_name

if has_failed:
    print(f'You need a break, {max_fails} poor grades.')
else:
    print(f'Average score: {grades_sum / solved_problems_count:.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')



fff