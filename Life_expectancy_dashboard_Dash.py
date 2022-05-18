# This is a life expectancy dashboard built using Dash.

# Importing necessary libraries
import imp
import dash
from dash import html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import plotly.express as px
import os

# Reading the data file
data_dir_path = os.path.dirname(__file__)
data_url = os.path.join(data_dir_path, 'life_expectancy.csv')
life_expect = pd.read_csv(data_url, usecols = ['country','year','life expectancy'])

year_min = life_expect['year'].min()
year_max = life_expect['year'].max()

app = dash.Dash(external_stylesheets = [dbc.themes.SOLAR])

app.layout = html.Div(children=[
    html.H1('Life Expectancy Dashboard'),
    dcc.RangeSlider(id = 'year-slider',
                    min = year_min,
                    max = year_max,
                    value = [year_min, year_max],
                    marks = {i:str(i) for i in range(year_min, year_max + 1, 10)}),
    dcc.Graph(id = 'line-graph'),
])

if __name__=='__main__':
    app.run_server(debug = True)





print(life_expect.head())


