largest_so_far = None
print("before", largest_so_far)
for i in [9,41,12,74,15]:
    if largest_so_far is None: #"is" is also an operaot but stronger than "=="s
        largest_so_far= i
    elif largest_so_far<i :
        largest_so_far = i
print("after", largest_so_far)
