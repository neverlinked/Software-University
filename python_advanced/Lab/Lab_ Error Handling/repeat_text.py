text = input()

try:
    occurrences = int(input())
    print(text * occurrences)
except ValueError:
    print("Variable times must be an integer")

