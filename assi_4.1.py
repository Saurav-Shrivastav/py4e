def computepay(h,r):
    if h>40 :
        p = 40*r + (h-40)*1.5*r
        return p
    else :
        p = h*r
        return p

hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
p = computepay(float(hrs), float(rate))
print(p)
