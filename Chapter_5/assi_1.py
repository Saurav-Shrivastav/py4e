num = 0
tot = 0
while True :
    sval = input("Enter a number :")
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print("Enter correct data")
        continue
    num = num + 1
    tot = tot + fval
print('All Done')
print(tot, num, tot/num)

    
