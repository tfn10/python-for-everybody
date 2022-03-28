file_name = input('Enter file name: ')
fn = open(file_name)
count = 0
address = dict()
for line in fn:
    words = line.strip().split()
    try:
        if words[0] == 'From':
            email = words[1]
            if email not in address:
                address[email] = 1
            else:
                address[email] += 1
    except IndexError:
        pass
larger = 0
highest_occurrence = ''
for mail, value in address.items():
    if value >= larger:
        highest_occurrence = mail
        larger = value
print(f'{highest_occurrence} {larger}')
