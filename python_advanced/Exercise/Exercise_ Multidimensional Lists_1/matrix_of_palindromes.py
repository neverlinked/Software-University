import string

rows, columns = [int(n) for n in input().split()]
alphabet = list(string.ascii_letters[:26])

matrix = []
for i in range(rows):
    current_row = []
    for j in range(columns):
        current_row.append(alphabet[i] + alphabet[i + j] + alphabet[i])
    print(' '.join(current_row))