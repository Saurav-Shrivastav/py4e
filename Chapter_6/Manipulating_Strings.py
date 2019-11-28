#Concatenating strings
a = 'Hello'
b = a + 'There'
print(b)                  #prints "HelloThere"
b = a + ' ' + 'There'
print(b)                  #prints "Hello There"

#using in as a logical operator (other use is in for loop)
#The in expression returns True or False
fruit = 'banana'
if 'a' in fruit :
    print('Found it!')

# '==' is used to compare strings

#Strings are objects
#For now objects are variables that have capabilities grafted or built into them

greet = 'Hello Saurav'
zap = greet.lower()   # This is,run a function lower() that's part of the string object, of the string class, that is going to give us back a lowercase copy.
#So what this functionally does, it says, make a copy of greet but all lowercase and return it to us, and then we're going to store that into zap.
print(zap)
print(greet)

#This part of code has to be typed in the console
type(greet)     #returns <class 'str'>
dir(greet)      #returns the methods of class string

#This link gives a detail ofvarious methods of strigs - "https://docs.python.org/3/library/stdtypes.html#string-methods"

#capitalize()
a = fruit.capitalize()
print(a)                #capitalizes the first letter of the word
b = 'ABC'.capitalize()
print(b)                #returns Abc

#find() - to find a letter or a bunch of letters within a string - gives the index of the position
#if a letter is not foundit return -1

#upper() & lower() are used to change the case
#This can be used while comparing two strings, they have to be of the same case even if they are the same woords for the equality to return True

#replace() - saercha word in a string and replace it with another letter
nstr = greet.replace('Saurav', 'saulav')

#lstrip() and rstrip() remove spaces from the left or right resp.
#strip() removes beginning and ending spaces
greet = '   Hello Saurav       '
print(greet)
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

#prefixes - startswith()
line = 'Please have a nice day'
if line.startswith('Please') :
    print('HI')

#parsing and extracting
data = "From sauravsrivastav@gmail.com sat Jan 5"
#we are going to extract the site address
atpos = data.find("@")
sppos = data.find(' ', atpos) #this finds a space after the atpos index
host = data[atpos+1: sppos]
print (host)

#in python 3 all strings are unicode
