fhand = open('mbox.txt', 'r')   #returns a handle used to manipulate a file
#if mode is not specified then by default it is taken as read
#mbox.txt is the filename and r is the mode, we use w for the write mode
#file handle is not the data it is just the way to get at the data

stuff = 'Hello\nWorld'   #the newline character indicates the beginning of a new line
print(stuff)             #\n is one character and not two(as treated by python)

#a file is like a sequence of lines
