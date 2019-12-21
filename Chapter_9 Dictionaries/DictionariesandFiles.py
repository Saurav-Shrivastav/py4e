counts = dict()
line = input('Enter a line of text :')
words = line.split()

print('Words:', words)
print('Counting...')

for word in words :
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

for key in counts :
    print(key, counts[key])

# We can get a list of keys, values or items(both)
print(list(counts))         # Prints the labels
print(counts.keys())        # Prints the labels
print(counts.values())      # Prints the values in each key
print(counts.items())       # Prints a list with each key as a tuple(another data structure)

# Two iteration variables
# First variable is the key and the 2nd is the value
for aaa,bbb in counts.items() :
    print(aaa, bbb)
