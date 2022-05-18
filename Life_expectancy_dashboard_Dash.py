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



print(life_expect.head())


