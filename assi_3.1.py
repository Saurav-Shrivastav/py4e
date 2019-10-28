hrs = input("Enter Hours:")
rate = input("Enter the rate per hour:")
hrs = float(hrs)
rate = float(rate)
if hrs <= 40 :
    s = hrs*rate
    print(s)
elif hrs>40 :
    s = 40*rate + (hrs-40)*rate*1.5
    print(s)
