# TO FIND THE 10 MOST COMMON WORDS IN A FILE
fhand = open('romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

first = list()
for key, val in counts.items() :
    newtup = (val, key)
    first.append(newtup)

first = sorted(first, reverse = True)

for val, key in first[:10]:     #till 10(not included)
    print(key, val)
