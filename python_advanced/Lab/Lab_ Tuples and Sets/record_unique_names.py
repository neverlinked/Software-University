names_quantity = int(input())
names = set()

for _ in range(names_quantity):
    name = input()
    names.add(name)

for name in names:
    print(name)
