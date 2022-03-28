file_name = input('Enter file name: ')
fh = open(file_name)
text = 'X-DSPAM-Confidence:'
addition = 0
count = 0
for line in fh:
    if text in line:
        position = line.find('0')
        number = float(line[position:])
        count += 1
        addition += number
average = addition / count
fh.close()
print(f'Average spam confidence: {average}')
