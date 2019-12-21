name = input("Enter file:")
try :
    fhand = open(name)
except :
    print("Enter the correct file name.")
    exit()

counts = dict()

for line in fhand :
    line = line.strip()
    if line.startswith('From:') :
        continue
    if line.startswith('From ') :
        words = line.split()
        s = words[1]
        counts[s] = counts.get(s, 0) + 1

bigword = None
bigcount = None
for word, count in counts.items() :
    if bigcount is None or count>bigcount :
        bigword = word
        bigcount = count

print(bigword, bigcount)
