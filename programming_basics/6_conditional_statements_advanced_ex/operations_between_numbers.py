N1 = int(input())
N2 = int(input())
Operator = input()

output = ''

if Operator == '+':
    result = N1 + N2
    output = f'{N1} + {N2} = {result}'
    if result % 2 == 0:
        output += ' - even'
    else:
        output += ' - odd'
elif Operator == '-':
    result = N1 - N2
    output = f'{N1} - {N2} = {result}'
    if result % 2 == 0:
        output += ' - even'
    else:
        output += ' - odd'
elif Operator == '*':
    result = N1 * N2
    output = f'{N1} * {N2} = {result}'
    if result % 2 == 0:
        output += ' - even'
    else:
        output += ' - odd'
elif Operator == '/':
    if N2 == 0:
        output = f'Cannot divide {N1} by zero'
    else:
        result = N1 / N2
        output = f'{N1} / {N2} = {result:.2f}'

elif Operator == '%':
    if N2 == 0:
        output = f'Cannot divide {N1} by zero'
    else:
        result = N1 % N2
        output = f'{N1} % {N2} = {result}'

print (output)