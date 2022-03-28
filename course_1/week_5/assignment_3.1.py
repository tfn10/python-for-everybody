hrs = float(input('Enter Hours: '))
rate = float(input('Enter rate: '))
if hrs <= 40:
    pay = hrs * rate
else:
    pay = ((hrs - 40) * 1.5 + 40) * rate
print(pay)
