#concatenating Lists (By using the '+' operator)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#Slicing lists
d = c[1:3]      #Just like in strings, the second number is upto but not including
print(d)

#http://docs.python.org/tutorial/datastructures.html - all the list methods

#Building a list from scratch
stuff = list()       #creates an empty list by the name of stuff
stuff.append('book')
stuff.append(99)
print(stuff)

if(99 in stuff) :
    print("9 is present in the list")
if('cookie' not in stuff) :
    print("cookie is not present in the list")

#sort() function is used to sort(order them) lists
#max(), min(), sum() are built in functions in lists - They use lists as parameters

numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' :
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print("Average:", average)
