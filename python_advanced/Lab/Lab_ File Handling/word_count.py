import re

with open('words.txt', 'r') as file:
    words = file.read().split()

    word_count = {}
    pattern = "[A-Za-z']+"

    input_file = open('input.txt')
    result = re.findall(pattern, input_file.read().lower())

    for word in result:
        if word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    sorted_word_count = sorted(word_count.items(), key=lambda item: -item[1])
    for word, occurrences in sorted_word_count:
        print(f'{word} - {occurrences}')

