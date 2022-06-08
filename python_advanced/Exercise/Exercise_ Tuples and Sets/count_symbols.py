data = input()
symbols = {}

for char in data:
    if char not in symbols:
        symbols[char] = 0
    symbols[char] += 1

for symbol, occurrences in sorted(symbols.items()):
    print(f'{symbol}: {occurrences} time/s')