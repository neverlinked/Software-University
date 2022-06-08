# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit = float(input())
deposit_period = int(input())
yearly_percent = float(input())

interest = deposit * yearly_percent /100
monthly_interest = interest / 12
total = deposit + (deposit_period * monthly_interest)
print(total)
