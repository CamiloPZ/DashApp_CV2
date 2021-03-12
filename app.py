import dash
import dash_bootstrap_components as dbc
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                title="AE CPZ",
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1,maximum-scale=1, minimum-scale=0.9'}]
                )
server = app.server
