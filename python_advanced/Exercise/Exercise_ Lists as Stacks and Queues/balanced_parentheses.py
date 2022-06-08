sequence_of_parentheses = input()
opening_brackets = []
balanced = True

for char in sequence_of_parentheses:
    if char in '({[':
        opening_brackets.append(char)
    elif not opening_brackets:
        balanced = False
        break
    else:
        last_opening_bracket = opening_brackets.pop()
        if f'{last_opening_bracket}{char}' not in '(){}[]':
            balanced = False

if balanced and not opening_brackets:
    print('YES')
else:
    print('NO')
