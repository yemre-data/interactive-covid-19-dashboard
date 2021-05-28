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
df_global = pd.read_csv('CovidData/data_confirmed.csv')
df_deaths = pd.read_csv('CovidData/data_deaths.csv')








