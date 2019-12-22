# Tuples are another kind of sequence that functions much like a list
# Index starts with 0
# Uses () instead of [] in a list
# Tuples are immutable
# Tuples are more efficient (in terms of memory use and performance)
# The items() method in dictionaries returns a list of Tuples.
# The comparision operators work with tuples and other sequences.
# if the first items are equal then it goes to the next item.
if (0,1,2)<(5,1,2) :
    print("t")
if (0,1,2000000000)<(0,3,2) :
    print("t")
# can compare strings as well!

# We can sort lists of Tuples
d = {'a':10, 'b':1, 'c':22}
print(d.items())
print('Sorted', sorted(d.items()))      #sorted function takes a sequence as a parameter and returns a sorted sequence
for k,v in sorted(d.items()):
    print(k,v)

# Sorting by value instead of key
tmp = list()
for k, v in d.items() :     # this loop reverses the tuples in d.items()
    tmp.append((v,k))
tmp = sorted(tmp, reverse=True)     #high to low by reverse=True
print(tmp)
