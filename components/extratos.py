from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 
import calendar
from app import app

from dash import dash_table
from dash.dash_table.Format import Group
import dash



# =========  Layout  =========== #
layout = dbc.Col([
    html.H5('Página Extratos')
    ])

# =========  Callbacks  =========== #
# Tabela
