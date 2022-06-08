chars_to_be_replaced = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for char in chars_to_be_replaced:
                result = result.replace(char, '@')
            print(result)