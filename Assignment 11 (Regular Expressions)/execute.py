import re

filename = input('Enter a file name:')
if len(filename) < 1 : filename = 'regex_sum_96113.txt'
handle = open(filename)
numberslist = list()
sum = 0
for line in handle:
    line = line.rstrip()
    numbers = re.findall('\S[0-9]+\S?', line)
    for number in numbers:
        numberslist.append(number)
for entry in numberslist:
    try:
        entry = int(entry)
    except Exception as e:
        entry = re.sub(r'\D', "", entry)
        entry = int(entry)

    sum = sum + entry

print(sum)
