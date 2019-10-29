largest_so_far = None
smallest_so_far = None
while True :
    sval = input('Enter a number:')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    if largest_so_far is None:
        largest_so_far=fval
    elif fval>largest_so_far:
        largest_so_far=fval
    if smallest_so_far is None:
        smallest_so_far=fval
    elif fval<smallest_so_far :
        smallest_so_far=fval
print('Maximum is', int(largest_so_far))
print('Minimum is', int(smallest_so_far))
