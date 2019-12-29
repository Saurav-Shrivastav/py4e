# Geocoding is converting Address to coordinates(lattitude and longitude)
# Reverse Geocoding is ulta process.
import pandas
from geopy.geocoders import Nominatim

nom = Nominatim(user_agent = "geocoding.py")
n = nom.geocode("Thapar University, Patiala, India")
print(n)
print(n.latitude, "\n")

df = pandas.read_csv("supermarkets.csv")
df["Address"] = df["Address"] + "," + df["City"] + "," +  df["State"]
df["Coordinates"] = df["Address"].apply(nom.geocode)
df["Latitudes"] = df["Coordinates"].apply(lambda x : x.latitude if x != None else None)
df["longitude"] = df["Coordinates"].apply(lambda y : y.longitude if y!= None else None)
print(df)
