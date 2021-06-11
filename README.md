# interactive-covid-19-dashboard
- Description
- Dev Process
- All version
- How to install
- License

## Description
- This project provides an interactive dashoboard of COVID-19  confirmed and death cases  data that you can run on your local server by running the main.py file on local software. 
- Theaim is to give a clear interactive vizualisation of the covid-19 epidemic in different countries of the world. 

The number of cases and deaths per country and date are provided as open-data by the [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19). 
Dashboard and Visualisation was created by the three students of [CRI-AIRE Master](https://master.cri-paris.org/en).

You can select new cases and new death, total confirmed cases per million(normalized) and total death cases per million(normalized), vaccination per hundred and conutry by date. Feel free to play and the the graph, your select will give by day results.


## Dev Process
- COVID DATA extracted from open source - 21/05/2021
- Population DATA extracted from Kaggle - 2020
- Creating streamlit interface on Pycharm

## How to install
- 1st You need to install [streamlit](https://streamlit.io/) and [pandas](https://pandas.pydata.org/), [plotly](https://plotly.com/)

Please install the project dependencies run pip install -r requirements.txt

```
$ pip install -r requirements.txt
```
There have: 
```
pandas == 1.2.4
streamlit==0.82.0
plotly==4.14.3
```

- 2nd Please install [Pycharm](https://www.jetbrains.com/fr-fr/pycharm/) ， you can choose PyCharm Community Edition, it's free.

- 3rd CE example:
run on Pycharm terminal:

```
$ streamlit run main.py
```

Congrats! You can try!

It's an practice of open source course by a group of students, feel free to give us feedback! Thank you!

## License

MIT Licence 

Copyright (c) 2021 yemre-data
