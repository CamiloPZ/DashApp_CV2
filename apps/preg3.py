import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import numpy as np
import plotly_express as px
import dash_bootstrap_components as dbc
from app import app

def texto_variable(planeta,diametro):
  cadena = 'El diámetro de la {} es de {} kilómetros'.format(planeta,diametro)
  return cadena

def dominio_correo(cadena):
  if cadena != None:
    dominio = cadena.split('@')[1]
  else:
    dominio = ''
  return dominio

def policia(velocidad,cumple= False):
  valla = 60
  if velocidad != None:
      if cumple == True:
        valla = valla + 5
      if velocidad <= valla:
        resultado = 'Sin Ticket'
      elif velocidad >=(valla+1) and velocidad <= (valla+20):
        resultado = 'Ticket pequeño'
      else:
        resultado = 'Ticket grande'
      return resultado
  else:
      return 'Sin Ticket'
markdown_text9 = '''

```python
# Definimos una función que retorna lo solicitado
def texto_variable(planeta,diametro):
  cadena = 'El diámetro de la {} es de {} kilómetros'.format(planeta,diametro)
  return cadena
# Usamos la función
texto_variable(planeta,diametro)
```

'''

markdown_text10 = '''

```python
# Definimos una función que reciba un string y retorne el dominio
def dominio_correo(cadena):
  dominio = cadena.split('@')[1]
  return dominio
```

'''

markdown_text11 = '''

```python
# Definimos una función que retorne el resultado de la detención
# teniendo como inputs la velocidad del carro y si es cumpleaños
# del chofer
def policia(velocidad,cumple= False):
  valla = 60
  if cumple == True:
    valla = valla + 5
  if velocidad <= valla:
    resultado = 'Sin Ticket'
  elif velocidad >=(valla+1) and velocidad <= (valla+20):
    resultado = 'Ticket pequeño'
  else:
    resultado = 'Ticket grande'
  return resultado
```

'''
layout = html.Div(children=[
  html.H1('Pregunta 9',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
  html.H3('Dadas las variables:planeta = "Tierra" diámetro = 12742 ** Utilice .format () para imprimir la siguiente cadena: El diámetro de la Tierra es de 12742 km'),
  dbc.Row([

        dbc.Col([
            html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
            html.Br(),
            dcc.Markdown(children=markdown_text9)
        ], #width={'size':5, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
        dbc.Col([
            html.H4("Texto Variable",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),

            html.Br(),
            dcc.Dropdown(id='mi_planeta', multi=False,
            value='Tierra',
            placeholder="Seleccione Planeta ...",
            options=[
            {'label': 'Tierra', 'value': 'Tierra'},
            {'label': 'Jupiter', 'value': 'Jupiter'},
            {'label': 'Saturno', 'value': 'Saturno'}
                    ],
            ),
            html.Br(),
            dcc.Dropdown(id='mi_ratio', multi=False,
            value='12742',
            placeholder="Seleccione kilómetros ...",
            options=[
            {'label': '12742', 'value': '12742'},
            {'label': '40742', 'value': '40742'},
            {'label': '80742', 'value': '80742'}
                    ],
            ),
            html.Br(),
            # dcc.Markdown(children=markdown_t    ext7e)
            # dcc.Markdown("'UNI'"),
            # dcc.Markdown(children=markdown_text4e),
            # dcc.Graph(id='In',figure= fig4),
            html.H3(id="salida"),

        ],# width={'size':5, 'offset':1, 'order':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

    ], no_gutters=False, justify='center'),
    html.Br(),
    html.H1('Pregunta 10',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
    html.H3('Cree una función que tome el dominio del sitio web de correo electrónico de una cadena.'),
    dbc.Row([

          dbc.Col([
              html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
              html.Br(),
              dcc.Markdown(children=markdown_text10)
          ], #width={'size':5, 'offset':0, 'order':2},
             xs=12, sm=12, md=12, lg=5, xl=5
          ),
          dbc.Col([
              html.H4("Dominio del correo electrónico",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),

              html.Br(),
              dcc.Dropdown(id='mi_dominio', multi=False,
              value='camilo@uni.pe',
              placeholder="Seleccione correo electrónico ...",
              options=[
              {'label': 'camilo@uni.pe', 'value': 'camilo@uni.pe'},
              {'label': 'pepe@gmail.com.pe', 'value': 'pepe@gmail.com.pe'},
              {'label': 'fiorella@yahoo.es', 'value': 'fiorella@yahoo.es'},
              {'label': 'olivia@outlook.bo', 'value': 'olivia@outlook.bo'}
                      ],
              ),

              html.Br(),
              # dcc.Markdown(children=markdown_t    ext7e)
              # dcc.Markdown("'UNI'"),
              # dcc.Markdown(children=markdown_text4e),
              # dcc.Graph(id='In',figure= fig4),
              html.H3(id="salida2"),

          ],# width={'size':5, 'offset':1, 'order':1},
             xs=12, sm=12, md=12, lg=5, xl=5
          ),

      ], no_gutters=False, justify='center'),
      html.Br(),
      html.H1('Pregunta 11',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
      html.H3('Conduce demasiado rápido y un oficial de policía lo detiene. Escriba una función para devolver uno de los 3 resultados posibles: "Sin ticket", "Ticket pequeño" o "Ticket grande"'),
      dbc.Row([

            dbc.Col([
                html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                html.Br(),
                dcc.Markdown(children=markdown_text11)
            ], #width={'size':5, 'offset':0, 'order':2},
               xs=12, sm=12, md=12, lg=5, xl=5
            ),
            dbc.Col([
                html.H4("Detención del vehículo",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),

                html.Br(),
                dbc.Label("Velocidad del vehículo"),
                dbc.Input(id='Veloz', placeholder="Ingrese la velocidad ...",value=60),

                html.Br(),
                dbc.Label("¿Hoy es tu cumpleaños"),
                dcc.RadioItems( id='Cumple',
                        options=[
                            {'label': 'Sí', 'value': 'True'},
                            {'label': 'No', 'value': 'False'},

                        ],
                        value='False'
                    )  ,
                html.Br(),
                # dcc.Markdown(children=markdown_t    ext7e)
                # dcc.Markdown("'UNI'"),
                # dcc.Markdown(children=markdown_text4e),
                # dcc.Graph(id='In',figure= fig4),
                html.H3(id="salida3"),

            ],# width={'size':5, 'offset':1, 'order':1},
               xs=12, sm=12, md=12, lg=5, xl=5
            ),

        ], no_gutters=False, justify='center'),

])

@app.callback(
    Output("salida2", "children"),
    Input("mi_dominio", "value"))
def dominiof(texto):
    dominio = dominio_correo(texto)
    return dominio


@app.callback(
    Output("salida", "children"),
    [Input("mi_planeta", "value"),
     Input("mi_ratio", "value")])
def display_color(planeta, ratio):
    texto = texto_variable(planeta,ratio)
    return texto

@app.callback(
    Output("salida3", "children"),
    [Input("Veloz", "value"),
     Input("Cumple", "value")])
def display_color2(velocidad, cumple):
    if cumple == 'True':
        cumple2 = True
    else:
        cumple2 = False
    if velocidad=='':
        velocidad='1'
    resultado = policia(int(velocidad),cumple2)
    return resultado
