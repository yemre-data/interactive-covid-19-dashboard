import pandas as pd
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import json
from geopy.geocoders import Nominatim
import requests
import streamlit as st
import folium

# Read data
df_global = pd.read_csv('CovidData/CONVENIENT_global_confirmed_cases.csv')
df_deaths = pd.read_csv('CovidData/CONVENIENT_global_deaths.csv')

# Some data wrangling
df_global.dropna(axis=0,inplace=True)
df_deaths.dropna(axis=0,inplace=True)
df_global.rename(columns = {'Country/Region':'Date'}, inplace = True)
df_deaths.rename(columns = {'Country/Region':'Date'}, inplace = True)

# Creating streamlit Interface

# setting title
st.markdown("# Welcome to Interactive Covid-19 Analyze Board ")
st.markdown("This project has performed by the CRI team at Paris. "
            "As vaccinations increase and covid-19 approaches towards the end, "
            "we would like analyze current situation of Covid on the world. "
            "The page has created for analyze Covid-19 confirmed cases and deaths data from Jan 2020 to now.   ")
st.markdown("(Data has taken from open source: https://github.com/CSSEGISandData/COVID-19) ")

st.image('CovidData/covid.jpg')






