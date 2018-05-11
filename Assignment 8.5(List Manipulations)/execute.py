fname = input("Enter file name: ")
fh = open(fname)
lst = list()
count = 0
for line in fh:
	if line.startswith('From:'): continue
	if line.startswith('From'):
		count = count + 1
		line = line.rstrip()
		lst = line.split()
		print(lst[1])
print('There were',count, 'lines in the file with From as the first word')
