numbers = []
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
        numbers.append(num)
    except ValueError:
        print('Invalid input')
largest = max(numbers)
smallest = min(numbers)
print(f'Maximum is {largest}')
print(f'Minimum is {smallest}')
