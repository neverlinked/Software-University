data_stack = []
lines = int(input())

for line in range(lines):
    query = input()

    if ' ' in query:
        _, number = query.split()
        data_stack.append(int(number))
    else:
        query = int(query)
        if query == 2 and data_stack:
            data_stack.pop()
        elif query == 3 and data_stack:
            print(f'{max(data_stack)}')
        elif query == 4 and data_stack:
            print(f'{min(data_stack)}')

while data_stack:
    last_element = data_stack.pop()
    if data_stack:
        print(last_element, end = ', ')
    else:
        print(last_element)
        break