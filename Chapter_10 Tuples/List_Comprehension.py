# Same program as in tuples-ex but in a shorter version.
# List Comprehension - creates a dynamic list

# TO FIND THE 10 MOST COMMON WORDS IN A FILE
fhand = open('romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

first = sorted( [ (v,k) for k,v in counts.items() ] , reverse = True)

for val, key in first[:10] :
    print(val, key)
