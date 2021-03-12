import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly_express as px
from dash.dependencies import Input, Output
from datetime import date
from app import app
from app import server
from apps import preg1,preg2,preg3,preg4



app.layout = html.Div(children=[
    # html.H1("1era PC AE - Camilo Poma Zamudio",style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
    dbc.NavbarSimple(
            children=[
                 dbc.NavLink("Preguntas 1-4", href="/apps/preg1", id="page-1-link",style={"font-size": "1.35em"}),
                 dbc.NavLink("Preguntas 5-8", href="/apps/preg2", id="page-2-link",style={"font-size": "1.35em"}),
                 dbc.NavLink("Preguntas 9-11", href="/apps/preg3", id="page-4-link",style={"font-size": "1.35em"}),
                 dbc.NavLink("Preguntas 12-13", href="/apps/preg4", id="page-5-link",style={"font-size": "1.35em"}),
                       ],
            brand="1PC AE - Camilo Poma Zamudio",
            brand_style={"position": "relative","font-size": "4.9 em","font-style":"italic","textAlign": "center","font-weight":"bold"},
            color="success",
            dark=True,),



    html.Div(id='page-content',children=[],style={"background":"#DCDCDC","padding":"0.01%"}),
    # dcc.Input(id="input1",value='La UNI es la UNI'),
    # html.Div(id="output"),
    dcc.Location(id='url', refresh=False)
  ],)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    # if pathname == '/':
    #     # return dcc.Graph(figure=fig)
    #     return app.layout
    if pathname == '/apps/preg1':
        return preg1.layout
    if pathname == '/apps/preg2':
        return preg2.layout
    if pathname == '/apps/preg3':
        return preg3.layout
    if pathname == '/apps/preg4':
        return preg4.layout
    else:
        return preg1.layout


# @app.callback(
#     Output("output", "children"),
#     Input("input1", "value"),
#     )
# def update_output(texto):
#   dff = cuenta_texto(texto)
#   return dff

if __name__ == '__main__':
    app.run_server(debug=True)
