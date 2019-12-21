#a file handle can be treated as a sequence of strings.
#Each line in the file is a string in the sequence

#line counter
fhand = open('mbox.txt')
count = 0
for cheese in fhand :
    count = count + 1
print('line count :', count)

#reading the whole file (number of characters(includes the newline characters as well))
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))

#Searching through a file
fhand = open('mbox.txt')
for line in fhand :
    if line.startswith('From:') :
        print(line)
#There will be extra new lines because "print" adds a newline at the end
#and the lines already have a newline character at end of each line

#Searching through a file (fixed)
fhand = open('mbox.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

#skipping a particular line with continue(same as above)
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)

#using 'in' to find a line
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

#prompt for filename
fname = input('Enter the file name: ')
try :               #handlingbad file names
    fhand = open(fname)
except :
    print('File cannot be opened', fname)
    quit()
count = 0
for line in fhand :
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)
