total_steps_count = 0

command = input()

while command != 'Going home':
    steps = int(command)

    total_steps_count += steps

    if total_steps_count >= 10000:
        break

    command = input()



else:
   steps = int(input())
   total_steps_count += steps

if total_steps_count >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{total_steps_count - 10000} steps over the goal!')
elif total_steps_count < 10000:
    print(f'{10000-total_steps_count} more steps to reach goal.')
