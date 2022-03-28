file_name = input('Enter file: ')
hours = dict()
with open(file_name) as file:
    for line in file:
        words = line.strip().split()
        try:
            if words[0] == 'From':
                date = words[5]
                hrs = date[:2]
                if hrs not in hours:
                    hours[hrs] = 1
                else:
                    hours[hrs] += 1
        except IndexError:
            pass
hour = hours.keys()
for h in sorted(hour):
    print(f'{h} {hours[h]}')
