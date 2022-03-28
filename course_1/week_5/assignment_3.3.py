score = float(input('Enter a score: '))
if 0.9 <= score <= 1.0:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif 0 <= score < 0.6:
    print('F')
