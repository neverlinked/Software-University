clothes_in_box = [int(n) for n in input().split()]
rack_capacity = int(input())

current_rack = rack_capacity
racks_used = 1

while clothes_in_box:
    current_cloth = clothes_in_box[-1]

    if current_cloth <= current_rack:
        clothes_in_box.pop()
        current_rack -= current_cloth
    else:
        racks_used += 1
        current_rack = rack_capacity


print(racks_used)

#7 + 9 // 7 + 8 // 3 + 6 // 8 + 4 // 5