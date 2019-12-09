#Algorithms are a set of rules or steps to solve a problem
#Data structures - A particular way of organizing data in a computer
#A list element can be any python object.(even another list.)
#A collection allows us to put many values in a single variable.
#A list can be empty, list constants are surrounded by square brackets and the elements are eperated by commas.
#A list can have different types of data.
for i in [5,4,3,2,1] :
    print(i)
print("out of the loop")

friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])

#Strings are "immutable" - we cannot change the contents of a string.
#Lists are mutable - can be changed using the index operator.

lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print("new:", lotto)

#the len() function gives the number of elements present in a list.
#The range function returns a list of numbers that range from zero to one less than the parameter.
print(len(lotto))
print(range(len(lotto)))
print(" ")
for i in range(len(lotto)) :
    m = lotto[i]
    print(i+1, m)
