import pandas as pd

df = pd.read_csv("E:\data\cm\dest\map.csv")
list_of_lists = df.values.tolist()
print(list_of_lists)