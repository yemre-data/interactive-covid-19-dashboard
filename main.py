import pandas as pd
df = pd.read_csv('Covid_Data/time_series_covid19_confirmed_global.csv')
mis = df.isnull().sum()
print(df.head())
print(mis)
