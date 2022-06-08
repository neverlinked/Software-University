screening_type = input()
rows = int(input())
columns = int(input())
# Premiere - премиерна прожекция, на цена 12.00 лева;
# Normal - стандартна прожекция, на цена 7.50 лева;
# Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

taken_seats = rows * columns
price = 0

if screening_type == 'Premiere':
    price = taken_seats * 12
elif screening_type == 'Normal':
    price = taken_seats * 7.50
elif screening_type == 'Discount':
    price = taken_seats * 5

print(f'{price:.2f} leva')
