import pandas as pd
import missingno as msno

# Read data
df_global = pd.read_csv('Covid_Data/time_series_covid19_confirmed_global.csv')
df_deaths = pd.read_csv('Covid_Data/time_series_covid19_deaths_global.csv')

# To see our data
print(df_global.head())
print(df_deaths.head())

# See missing values
mis_global = df_global.isnull().sum()
mis_deaths = df_deaths.isnull().sum()
print(mis_global)
print(mis_deaths)

# Visualisation of the missing values
print(msno.bar(df_global,color="dodgerblue", sort="ascending", figsize=(10,5), fontsize=12))
print(msno.bar(df_deaths,color="dodgerblue", sort="ascending", figsize=(10,5), fontsize=12))





