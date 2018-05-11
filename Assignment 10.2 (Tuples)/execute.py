# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
hourlist = list()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        linelist = line.split()
        time = linelist[5]
        timesplit = time.split(':')
        hour = timesplit[0]
        hourlist.append(hour)
for hours in hourlist:
    counts[hours] = counts.get(hours, 0) + 1
wordlist = list()
for k,v in counts.items():
    wordlist.append((k, v))
wordlist.sort()
for k,v in wordlist:
    print(k,v)
