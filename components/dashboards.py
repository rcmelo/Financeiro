from dash import Input, Output, State, Dash, html, dcc, callback
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import *



# =========  Layout  =========== #
layout = dbc.Col([
       html.H5('Página Extratos')
    ], )



# =========  Callbacks  =========== #
