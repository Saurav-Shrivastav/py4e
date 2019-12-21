largest_so_far = 0
print("before", largest_so_far)
for i in [9,41,12,74,15]:
    if largest_so_far==0 :
        largest_so_far= i
        continue
    if largest_so_far<i :
        largest_so_far = i
print("after", largest_so_far)
