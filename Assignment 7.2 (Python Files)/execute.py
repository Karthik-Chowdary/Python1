# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x = line.find(':')
    strip = line[x+2:]
    num = float(strip)
    total = total + num
    count = count + 1
print('Average spam confidence:',total/count)
