from dash import html, dcc
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


card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

# =========  Layout  =========== #
layout = dbc.Col([
       dbc.Row([
           
           # Saldo Total
            dbc.Col([
               dbc.CardGroup([
                  dbc.Card([
                     html.Legend('Saldo'),
                     html.H5('R$ 5400', id='p-saldo-dashboards', style={})
                  ], style={'padding-left': '20px', 'padding-top': '10px'}),
                  dbc.Card(
                      html.Div(className='fa fa-university', style=card_icon),
                      color='warning',
                      style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                  )
                ])
            ], width=4),
           
           # Receita
           dbc.Col([
               dbc.CardGroup([
                  dbc.Card([
                     html.Legend('Receita'),
                     html.H5('R$ 5400', id='p-receita-dashboards', style={})
                  ], style={'padding-left': '20px', 'padding-top': '10px'}),
                  dbc.Card(
                      html.Div(className='fa fa-university', style=card_icon),
                      color='warning',
                      style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                  )
                ])
            ], width=4),
           
           # Despesas
           dbc.Col([
               dbc.CardGroup([
                  dbc.Card([
                     html.Legend('Despesas'),
                     html.H5('R$ 5400', id='p-despesas-dashboards', style={})
                  ], style={'padding-left': '20px', 'padding-top': '10px'}),
                  dbc.Card(
                      html.Div(className='fa fa-university', style=card_icon),
                      color='warning',
                      style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                  )
                ])
            ], width=4),
           
        ])
    ])



# =========  Callbacks  =========== #
