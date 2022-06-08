data = list(input())
reversed_stack = ''

while data:
    char = data.pop()
    reversed_stack += char

print(reversed_stack)