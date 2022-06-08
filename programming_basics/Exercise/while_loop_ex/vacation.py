trip_money = float(input())
user_money = float(input())

spend_days_cnt = 0
days_spent = 0

while spend_days_cnt < 5:
    #day starts
    action = input()   #spend or save
    value = float(input())  #amount of money
    days_spent += 1

    if action == 'spend':
        spend_days_cnt += 1  # adds 1 day spending spree

        user_money -= value  #removes the spent money
        if user_money < 0:   #less than 0 equals no money
            user_money = 0

    elif action == 'save':
        spend_days_cnt = 0  #nulifies spending spree

        user_money += value #adds the savings

    if user_money >= trip_money: # money successfully saved
        break



if user_money >= trip_money:
    print(f'You saved the money for {days_spent} days.')
else:
    print("You can't save the money.")
    print(days_spent)
