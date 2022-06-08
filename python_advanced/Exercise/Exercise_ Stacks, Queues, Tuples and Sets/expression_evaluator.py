from collections import deque

data = input().split()

digits = deque()

for char in data:
    if char in '*+-/':
        while len(digits) > 1:
            first_num = digits.popleft()
            second_num = digits.popleft()

            result = 0
            if char == '*':
                result = first_num * second_num
            elif char == '+':
                result = first_num + second_num
            elif char == '-':
                result = first_num - second_num
            elif char == '/':
                result = first_num // second_num

            digits.appendleft(result)
    else:
        digits.append(int(char))

print(digits.pop())