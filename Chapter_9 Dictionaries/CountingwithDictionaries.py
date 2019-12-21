# This is a way of counting using Dictionaries

ccc = dict()            #frequency counter
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
print(" ")

# We can use the 'in' operator to see if a key is  present in a Dictionary
if 'csev' in ccc:
    print('csev is present in ccc')
print(" ")

#
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
print(" ")

# A quicker way to solve the same question
# The get method for Dictionaries
for name in names :
    counts[name] = counts.get(name, 0) + 1    # The get method is used to see if a name is present
    # in the dictionary and adds 1 to the value if it is not then it creates a label by that name
    # by defaulting the value to zero and then adds 1 to it
