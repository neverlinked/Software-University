count_of_inputs = int(input())
periodic_table = set()

for _ in range(count_of_inputs):
    chemical_compounds = input().split()
    for element in chemical_compounds:
        periodic_table.add(element)

print('\n'.join(periodic_table))