def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = ((h - 40) * 1.5 + 40) * r
    return pay


hrs = int(input('Enter Hours: '))
rate = float(input('Enter rate: '))
p = computepay(hrs, rate)
print(f'Pay {p}')
