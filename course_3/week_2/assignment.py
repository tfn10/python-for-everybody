import re

total = 0
count = 0
file_name = input('Enter file: ')
with open(file_name) as file:
    for line in file:
        numbers = re.findall(r'[0-9]+', line)
        for number in numbers:
            total += int(number)
            count += 1
file.close()
print(f'Count: {count}')
print(f'Sum: {total}')
