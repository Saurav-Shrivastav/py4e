#  Data frame is a special object that will hold the data in rows and columns.

import pandas

# Creating a data frame object manually:
df1 = pandas.DataFrame([[2,4,6],[1,2,3]])
print(df1)

# So you can have custom column and row names as well. As follows:
df1 = pandas.DataFrame([[2,4,6],[1,2,3]], columns = ["Price", "Age", "Value"], index = ["First", "second"])
print(df1)

# Passing dictionaries instead of lists :
df2 = pandas.DataFrame([{"Name":"Saurav", "Surname":"Shrivastav"},{"Name":"Vaibhav"}])
print(df2)

# This was about data structure and now comes the part about data analysis :
# the "dir(df1)" command in the command prompt will give all the methods that can be
# applied on the given data frame object.
# for example :

print(df1.mean())     # df1.mean() gives a series object which is then printed out.
print(df1.Price)      # this also gives a series object of the column price and is then printed out.

# So basically a DataFrame is a combination of series.

print(df1.Price.mean())
