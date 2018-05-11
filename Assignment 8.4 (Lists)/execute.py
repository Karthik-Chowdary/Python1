fname = input("Enter file name: ")
fh = open(fname)
lst = list()
min = list()
for line in fh:
    min = line.split()
    for word in min:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
