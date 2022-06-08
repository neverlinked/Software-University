wanted_book = str(input())

command = str(input())

books_counter = 0

while command != wanted_book:
    command = str(input())
    books_counter += 1
    if command == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {books_counter} books.')
        break

if command == wanted_book:

    print(f'You checked {books_counter} books and found it.')



