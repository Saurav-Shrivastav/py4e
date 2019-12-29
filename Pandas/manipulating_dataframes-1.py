import pandas

df1 = pandas.read_csv("supermarkets.csv")
df1["Continent"] = df1.shape[0]*["North America"] # Adding a new column named continent.
            # df1.shape is used to add the same data in all the rows.
print(df1, "\n")
df1["Continent"] = df1["Country"] + "," + df1["Continent"]

print(df1, "\n")

# Adding a row is a bit tricky:
df1_t = df1.T   #transposing the original data frame.
# Now add a column to this table and then again take the transpose to get your result
