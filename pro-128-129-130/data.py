import csv
import pandas as pd

df = pd.read_csv("total_stars.csv")

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

print(list(df))

df.to_csv('cleaned_data.csv')