# the datetime and time modules are used for various date and time related
# functionalities

import datetime
import time

now = datetime.datetime.now()
print(now)
yesterday = datetime.datetime(2019, 12, 24, 10, 2, 27, 226)
print(yesterday)
delta = now - yesterday
print("\n", "Difference between yesterday and now", delta)

print("\n", type(delta))
print("delta returns a datetime object of the datetime.datetime class")
print(delta.days)
print(delta.total_seconds())
print(delta.seconds)

filename = datetime.datetime.now()

# let's create a file with the current datetime as the filename

with open(filename.strftime("%Y-%m-%d-%H-%M-%S")+ ".txt", "w") as file :
    file.write("")      #  Writing empty string

# Using the time module to create delays

lst = list()
for i in range(5) :
    lst.append(datetime.datetime.now())
    time.sleep(1)          # Creates a delay of about 1 second

for i in range(5) :
    print(lst[i])
