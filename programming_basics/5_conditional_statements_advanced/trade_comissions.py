city = input()
sells_volume = float(input())
final_price = 0
valid_city = 0
if city == 'Sofia' or city == 'Varna' or city == 'Plovdiv':
    valid_city = 1

if city == 'Sofia':
    if 0 <= sells_volume <= 500:
        final_price = sells_volume * 0.05
    elif 500 < sells_volume <= 1000:
        final_price = sells_volume * 0.07
    elif 1000 < sells_volume <= 10000:
        final_price = sells_volume * 0.08
    elif sells_volume > 10000:
        final_price = sells_volume * 0.12
elif city == 'Varna':
    if 0 <= sells_volume <= 500:
        final_price = sells_volume * 0.045
    elif 500 < sells_volume <= 1000:
        final_price = sells_volume * 0.075
    elif 1000 < sells_volume <= 10000:
        final_price = sells_volume * 0.10
    elif sells_volume > 10000:
        final_price = sells_volume * 0.13
elif city == 'Plovdiv':
    if 0 <= sells_volume <= 500:
        final_price = sells_volume * 0.055
    elif 500 < sells_volume <= 1000:
        final_price = sells_volume * 0.08
    elif 1000 < sells_volume <= 10000:
        final_price = sells_volume * 0.12
    elif sells_volume > 10000:
        final_price = sells_volume * 0.145

if not valid_city:
    print('error')
elif final_price <= 0:
    print('error')
else:
    print(f'{final_price:.2f}')
