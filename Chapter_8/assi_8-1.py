fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print("Enter correct file name.")
words = list()
for line in fh :
    line = line.rstrip()
    data = line.split()
    for word in data :
        if word not in words :
            words.append(word)
words.sort()
print(words)
    
