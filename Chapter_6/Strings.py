fruit = 'banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x-1]
print(w)
#You'll get an error if your string index goes out of range

a = len(fruit) #The len function gives the length of a string
print(a)

#printing using the indeterminate while loop
index = 0                 #index acts as the iteration variable
while index<len(fruit) :
    word = fruit[index]
    print(index, letter)
    index = index + 1

#printing using the determinate for loop
for m in fruit :
    print(m)

#counting the nummber of a's in banana
count = 0
for alpha in fruit :
    if alpha == 'a' :
        count = count + 1
print(count)

#slicing  strings
s = 'Monty Python'
print(s[0:4])     #prints "Mont", 0:4 is from 0th till the fourth index but not incuding the 4th index
print(s[6:7])     #prints "P", from 6th till the 7th index
                  #if second number is beyond the range of the string then it stops @ the end of the string
print(s[:])       #prints the whole String
print(s[:4])      #prints the string from the 0th index till the 3rd index
print(s[3:])      #prints the string from the 3rd index till the last index
