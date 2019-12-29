import pandas

df1 = pandas.read_csv("supermarkets.csv")
print(df1)
print("")

# Label indexing and splitting
df1=df1.set_index("Address")
print(df1.loc["3666 21st St": "3995 23rd St","City":"Country"])
print("")

# splitting with the help of indexes
print(df1.iloc[1:3,1:3])    # upper bound exclusive
print("")

print(df1.ix[2,"Name"])
print(df1.ix[2,4])

# Deleting columns and rows :
print(df1.drop("332 Hill St", 0))    #We use 0 for rows
    # OR "print(df1.drop(df1.indexes))"
print(df1)

print(df1.drop(df1.columns[0:3], 1))    #Deleting columns
