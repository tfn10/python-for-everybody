file_name = input('Enter file name: ')
fn = open(file_name)
count = 0
for line in fn:
    words = line.strip().split()
    try:
        if words[0] == 'From':
            print(words[1])
            count += 1
    except IndexError:
        pass
print(f'There were {count} lines in the file with From as the first word')
