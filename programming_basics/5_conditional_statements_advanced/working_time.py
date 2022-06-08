hour = int(input())
week_day = str(input())

if 18 >= hour >= 10 :
    if week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day =='Friday' or week_day =='Saturday':
        print('open')
    else:
        print('closed')
else:
    print('closed')
