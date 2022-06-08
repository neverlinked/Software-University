days = int(input())  # дни за престой
room_type = input()  # вид помещение
grade = input()  # oценка

# room for one person – 18.00 лв за нощувка
# apartment – 25.00 лв за нощувка
# president apartment– 35.00 лв за нощувка

room_price = 0
nights = days - 1  # нощи престой (11 дни = 10 нощувки)

if room_type == 'room for one person':
    room_price = 18
elif room_type == 'apartment':
    room_price = 25
    if days < 10:
        room_price = room_price * 0.7
    elif 10 <= days <= 15:
        room_price = room_price * 0.65
    elif days > 15:
        room_price = room_price * 0.5
elif room_type == 'president apartment':
    room_price = 35
    if days < 10:
        room_price = room_price * 0.9
    elif 10 <= days <= 15:
        room_price = room_price * 0.85
    elif days > 15:
        room_price = room_price * 0.8

staying_price = room_price * nights

if grade == 'positive':
    staying_price = staying_price * 1.25
elif grade == 'negative':
    staying_price = staying_price * 0.9

print(f'{staying_price:.2f}')
