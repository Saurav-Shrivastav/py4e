#a program to prompt the user for hours and rate per hour using input to compute gross pay
hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter the rate:")
rate = float(rate)
pay = hrs*rate
print("Pay:", pay)
