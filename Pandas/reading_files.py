# We can read various kinds of files and add their data to a DataFrame object.

import pandas
import os

print(os.listdir())     # prints the list of the files present in the current dir
                        # or the dir in which this script is saved

df1 = pandas.read_json("supermarkets.json")
print(df1)

df1 = pandas.read_json("supermarkets.json")
df1 = df1.set_index("ID")     # sets the "ID" column for indexing purpose
print(df1)

# "pandas.read_json?" gives info about this command

df2 = pandas.read_csv("supermarkets.csv")
print(df2)
