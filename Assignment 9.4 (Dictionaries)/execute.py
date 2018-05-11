name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
personlist = list()
counts = dict()
maxcount = None
bigword = None
#Loop through everyline, remove extra spaces, if there is 'From ' in a line then split it and append second word to a list
for line in handle:
    line = line.rstrip()
    if 'From ' in line:
        linelist = line.split()
        personlist.append(linelist[1])
# For every word in list count the number of occurences and create a histogram of counts
for person in personlist:
    counts[person] = counts.get(person,0) + 1
# Loop through each key value pair and extraxt the biggest count that a word occurs and print it
for key,value in counts.items():
    if key == None or value > maxcount:
        maxcount = value
        bigword = key
print(bigword,maxcount)
