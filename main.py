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
st.set_page_config(layout="wide")
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots


# Read data
def take_data():
    all_data = pd.read_csv(
        'https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv?raw=true').reset_index()

    all_data = all_data[['location', 'date', 'new_cases', 'new_deaths', 'total_cases_per_million',
                         'total_deaths_per_million','new_vaccinations', 'total_vaccinations_per_hundred']].copy()
    return all_data


# Import Data and some wrangling
all_data = take_data()
all_data['date'] = pd.to_datetime(all_data.date)
all_data = all_data.sort_values(by=['date'], ascending=False)
country_list = list(all_data.location.unique())
country_list.sort()
st.cache(persist=True)

# Creating streamlit Interface

# setting title
st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
st.markdown("# Welcome to Interactive Covid-19 Analysis DashBoard ")

st.markdown("This project is performed by the CRI team at Paris.  "
            "As vaccinations increase and covid-19 approaches towards the end, "
            "we would like analyze current situation of Covid on the world. "
            "This page is created to analyze Covid-19 confirmed cases,deaths and vacinations data from Jan 2020 to 2021.   ")

st.markdown("(Data is taken from open-source: https://github.com/owid/covid-19-data) ")

st.image('CovidData/covid.jpg')
st.sidebar.title("Selector")
st.sidebar.write("-----------")
st.sidebar.write("**Usage of Sidebar** ")
st.sidebar.write("You can select new cases & new death, total confirmed cases per million("
                 "normalized) & total death cases per million(normalized), vaccination per hundred and country by "
                 "date. Feel free "
                 "to play see the graph. ")
st.sidebar.write('Your select will give by day results.')
cd = st.sidebar.checkbox('New Cases and Death ')
total = st.sidebar.checkbox('Total Confirmed Cases and Deaths(normalized)')
vac = st.sidebar.checkbox('Vaccination')

start_date = st.sidebar.date_input('Select Start Date', datetime.date(2020, 1, 24))
end_date = st.sidebar.date_input('Select End Date', datetime.datetime.now().date())
if start_date and end_date:
    selected_date = pd.date_range(start_date, end_date - datetime.timedelta(days=1), freq='d')
else:
    selected_date = all_data['date'].unique()

select_country = st.sidebar.multiselect("Select Countries", country_list, default=["France"])
col1,col2 = st.beta_columns(2)

if cd:
    cases_death = all_data[all_data['date'].isin(selected_date)]
    cases_death = cases_death[cases_death['location'].isin(select_country)]
    cases_plot = px.line(cases_death, x='date', y='new_cases', color='location')
    death_plot = px.line(cases_death, x='date', y='new_deaths', color='location')
    cases_plot.update_layout(title="Number of Confirmed Cases",
                  xaxis=dict(title='Date'),
                  yaxis=dict(title='Number of People'),
                  legend_title=dict(text='<b>Countries</b>'),
                  )
    death_plot.update_layout(title="Number of Confirmed Deaths",
                             xaxis=dict(title='Date'),
                             yaxis=dict(title='Number of People'),
                             legend_title=dict(text='<b>Countries</b>'),
                             )
    col1.plotly_chart(cases_plot, use_container_width=True)
    col2.plotly_chart(death_plot, use_container_width=True)

if total:
    total_death_cases = all_data[all_data['date'].isin(selected_date)]
    total_death_cases = total_death_cases[total_death_cases['location'].isin(select_country)]
    total_cases_plot = px.line(total_death_cases, x='date', y='total_cases_per_million', color='location')
    total_death_plot = px.line(total_death_cases, x='date', y='total_deaths_per_million', color='location')
    total_cases_plot.update_layout(title="Cumulative Confirmed Cases(normalized)",
                             xaxis=dict(title='Date'),
                             yaxis=dict(title='Number of People per million'),
                             legend_title=dict(text='<b>Countries</b>')
                                    )
    total_death_plot.update_layout(title="Cumulative Confirmed Deaths(normalized)",
                                    xaxis=dict(title='Date'),
                                    yaxis=dict(title='Number of People per million'),
                                    legend_title=dict(text='<b>Countries</b>')
                                   )
    col1.plotly_chart(total_cases_plot, use_container_width=True)
    col2.plotly_chart(total_death_plot,use_container_width=True)

if vac:
    vac_df = all_data[all_data['date'].isin(selected_date)]
    vac_df = vac_df[vac_df['location'].isin(select_country)]
    total_vac_plot = px.line(vac_df, x='date', y='total_vaccinations_per_hundred', color='location')
    total_vac_plot.update_layout(title="CumulativeVaccinations(normalized)",
                                   xaxis=dict(title='Date'),
                                   yaxis=dict(title='Number of People per hundred'),
                                   legend_title=dict(text='<b>Countries</b>')
                                   )
    vac_plot = px.line(vac_df, x='date', y='new_vaccinations', color='location')
    vac_plot.update_layout(title="Vaccinations",
                                   xaxis=dict(title='Date'),
                                   yaxis=dict(title='Number of People per hundred'),
                                   legend_title=dict(text='<b>Countries</b>')
                                   )
    col1.plotly_chart(total_vac_plot,use_container_width=True)
    col2.plotly_chart(vac_plot,use_container_width=True)


world_death = all_data['new_deaths'].sum(axis = 0, skipna = True)
world_cases = all_data['new_cases'].sum(axis = 0, skipna = True)
world_vac = all_data['new_vaccinations'].sum(axis = 0, skipna = True)
col1.write('<span style="color:%s">%s</span>' % ('red', " **Total Deaths on World :** "+ str(world_death)), unsafe_allow_html=True)
col2.write('<span style="color:%s">%s</span>' % ('black', " **Total Confirmed Cases: **" +str(world_cases)), unsafe_allow_html=True)
st.write('<span style="color:%s">%s</span>' % ('green', " ** 💉💉💉💉💉💉💉💉💉💉💉💉💉 Total Vacinations: **" +str(world_vac) +" **💉💉💉💉💉💉💉💉💉💉💉💉💉💉**"), unsafe_allow_html=True)

