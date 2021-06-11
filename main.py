
import pandas as pd
import plotly.express as px
import datetime
import streamlit as st
st.set_page_config(layout="wide")



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
all_data["new_cases"] = all_data["new_cases"].abs()
all_data["new_deaths"] = all_data["new_deaths"].abs()
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
total = st.sidebar.checkbox('Cumulative Confirmed Cases and Deaths')
vac = st.sidebar.checkbox('Vaccination by day and Cumulative')
seven = st.sidebar.checkbox('Last Seven Day Average')

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
    cases_plot.update_layout(title="Number of Confirmed Cases by day",
                  xaxis=dict(title='Date'),
                  yaxis=dict(title='Number of People'),
                  legend_title=dict(text='<b>Countries</b>'),
                  )
    death_plot.update_layout(title="Number of Confirmed Deaths by day",
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
    vac_plot.update_layout(title="Vaccinations by day",
                                   xaxis=dict(title='Date'),
                                   yaxis=dict(title='Number of People per hundred'),
                                   legend_title=dict(text='<b>Countries</b>')
                                   )
    col1.plotly_chart(total_vac_plot,use_container_width=True)
    col2.plotly_chart(vac_plot,use_container_width=True)

if seven:
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    week_ago = yesterday - datetime.timedelta(days=7)
    date_seven = pd.date_range(week_ago, yesterday - datetime.timedelta(days=1), freq='d')
    seven_df = all_data[all_data['date'].isin(date_seven)]
    seven_df = seven_df[seven_df['location'].isin(select_country)]

    seven_df_c = seven_df.groupby('location', as_index=False)['new_cases'].mean()
    seven_df_d = seven_df.groupby('location', as_index=False)['new_deaths'].mean()
    seven_df_c['new_cases'] = seven_df_c['new_cases'].fillna(0)
    seven_df_d['new_deaths'] = seven_df_d['new_deaths'].fillna(0)

    list_cases = seven_df_c['new_cases'].to_list()
    list_death = seven_df_d['new_deaths'].to_list()

    list_cases = list(map(int, list_cases))
    list_death = list(map(int, list_death))
    countries = seven_df['location'].to_list()
    countries = list(set(countries))
    number_of_country = len(countries)
    df = pd.DataFrame(dict(country=countries * 2, average=list_death + list_cases,
                           case_or_death=["Deaths"] * number_of_country + ["Cases"] * number_of_country))

    plot_average = px.scatter(df, x="country", y="average", color="case_or_death",
               title=" Last Seven Days Rolling Average Deaths And Cases",
               labels={"average": "Rolling Average"}
               )
    st.plotly_chart(plot_average,use_container_width=True)

world_death = all_data['new_deaths'].sum(axis = 0, skipna = True)
world_death =  '{:,.2f}'.format(world_death)
world_cases = all_data['new_cases'].sum(axis = 0, skipna = True)
world_cases =  '{:,.2f}'.format(world_cases)
world_vac = all_data['new_vaccinations'].sum(axis = 0, skipna = True)
world_vac =  '{:,.2f}'.format(world_vac)
st.write('<span style="color:%s">%s</span>' % ('red', " **Total Deaths on World :** "+ str(world_death)), unsafe_allow_html=True)
st.write('<span style="color:%s">%s</span>' % ('black', " **Total Confirmed Cases on World: **" +str(world_cases)), unsafe_allow_html=True)
st.write('<span style="color:%s">%s</span>' % ('green', " ** 💉💉💉💉💉💉💉💉💉💉💉💉 Total Vacinations on World: **" +str(world_vac) +" **💉💉💉💉💉💉💉💉💉💉💉💉💉**"), unsafe_allow_html=True)

st.write("⚠️**If you want look deeply covid cases and deaths you should select from sidebar.**")