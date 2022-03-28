file_name = input('Enter file name: ')
fh = open(file_name)
lst = list()
for line in fh:
    words = line.strip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))
