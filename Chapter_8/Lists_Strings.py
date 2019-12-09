#Spliting Strings : splits a string and stores it in a list.
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(" ")
print("Length of the string:", len(stuff))
print(" ")
print(stuff[0])
print(" ")
for w in stuff :
    print(w)
print(" ")

#Multiple spaces are treated as a single space when a delimiter is not specified
line = 'first;second;third'
thing = line.split()
print(thing)
print(" ")
print(len(thing))
print(" ")
thing = line.split(';')     #We tell python that ';' has tobe used as a delimiter
                            #instead of white spaces
print(thing)
print(" ")
print(len(thing))
print(" ")

#Finding the day on which an email was sent from the mbox file
fhand = open('mbox.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    words = line.split()
    print(words[2])

print(" ")

#The Double Split Pattern
fhand = open('mbox.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])
