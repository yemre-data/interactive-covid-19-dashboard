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
import datetime
import streamlit as st
import folium
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
# Read data
df_confirm = pd.read_csv('CovidData/df_confirm.csv')
df_deaths = pd.read_csv('CovidData/df_death.csv')

df_confirm['date'] =pd.to_datetime(df_confirm.date)
df_deaths['date'] = pd.to_datetime(df_deaths.date)
df_confirm = df_confirm.sort_values(by=['date'], ascending = False)
df_deaths = df_deaths.sort_values(by=['date'], ascending = False)

# Some data wrangling

country_list =list(df_confirm.country.unique())
country_list.sort()
#total_deaths =
#total_confirmed =df_confirm.

# Creating streamlit Interface
# setting title
st.markdown("# Welcome to Interactive Covid-19 Analyze Board ")
st.markdown("This project has performed by the CRI team at Paris. "
            "As vaccinations increase and covid-19 approaches towards the end, "
            "we would like analyze current situation of Covid on the world. "
            "The page has created for analyze Covid-19 confirmed cases and deaths data from Jan 2020 to now.   ")
st.markdown("(Data has taken from open source: https://github.com/CSSEGISandData/COVID-19) ")

st.image('CovidData/covid.jpg')
st.sidebar.title("Selector")
st.sidebar.write("-----------")
st.sidebar.write("**Usage of Sidebar** ")
st.sidebar.write("You can choose whether you can select confirmed cases and death cases by country and data. Feel free "
                 "to play see the graph. ")


case_death = st.sidebar.radio("Coivd 19 Patients Status",('Confirmed cases','Death cases'))
select_country = st.sidebar.multiselect("Select Countries",country_list)
start_date = st.sidebar.date_input('Select Start Date', datetime.date(2020,1,23))
end_date = st.sidebar.date_input('Select End Date', datetime.date(2021,6,4))
st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
#st.write('<span style="color:%s">%s</span>' % ('red', " **Total Confirmed Cases : and Total Deaths : ** "), unsafe_allow_html=True)
new_confirmed = df_confirm[df_confirm['country'].isin(select_country)]
new_confirmed = new_confirmed.sort_values(by=['date'], ascending = False)
confirmed_plot = px.line(new_confirmed, x = 'date', y = 'value',color='country')
confirmed_plot.update_layout(title="Confirmed Cases",
                 xaxis = dict(title = 'Date'),
                 yaxis = dict(title = 'Number of People'),
                 legend_title=dict(text='<b>Countries</b>'),
                  )
new_death =  df_deaths[df_deaths['country'].isin(select_country)]
new_death = new_death.sort_values(by=['date'], ascending = False)
death_plot = px.line(new_death, x = 'date', y = 'value',color='country')
death_plot.update_layout(title="Deaths Cases",
                 xaxis = dict(title = 'Date'),
                 yaxis = dict(title = 'Number of People'),
                 legend_title=dict(text='<b>Countries</b>'),
                  )
if case_death  == 'Confirmed cases':
    # st.write('<span style="color:%s">%s</span>' % ('red', " **Total Confirmed Cases : and Total Deaths : ** "), unsafe_allow_html=True)
    st.plotly_chart(confirmed_plot,use_container_width=True)
elif case_death == 'Death cases':
    st.plotly_chart(death_plot, use_container_width=True)






