#the user may input bad data and now we have to prevent the program from blowing up
hrs = input("Enter Hours:")
try :
    hrs = float(hrs)
except :
    print("Please enter numeric data")
    quit()
rate = input("Enter the rate per hour:")
try:
    rate = float(rate)
except :
    print("Please enter numeric data")
    quit()
if hrs <= 40 :
    s = hrs*rate
    print(s)
elif hrs>40 :
    s = 40*rate + (hrs-40)*rate*1.5
    print(s)
