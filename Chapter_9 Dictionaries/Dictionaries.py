# Dictionary - a "bag" of values, each with its own label
# Also known as Assocaiative arrays in perl/php
# Dictonaries are like bags with no order(no index). So we look up in a dictionary with a "lookup tag"
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
print(purse['candy'])

#Dictionaries are mutable
purse['candy'] = purse['candy'] + 2
print('Updated List:')
print(purse)

jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
print(jjj)
ooo = { } #empty dictionary
print(ooo)
