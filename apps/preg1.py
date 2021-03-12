import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from dash.dependencies import Input, Output
from app import app

def cuenta_texto(texto):
  if texto != None:
    a = 0
    df = texto.lower().split()
    for i in list(range(len(df))):
      if df[i]=='uni':
        a+=1
    return a
  else:
     return 0
markdown_text = '''

```python
# Definimos la función
def cuenta_texto(texto):
  # Condicion para trabajar solo con textos no vacíos
  if len(texto.replace(" ",""))>0:
    # Inicializamos el contador
    a = 0
    # Definimos la variable que contendrá el texto ingresado separado y en minúsculas
    df = texto.lower().split()
    # Iteramos para cada elemento de df
    for i in list(range(len(df))):
      # En caso el elemento sea 'uni', el contador se incrementa en 1
      if df[i]=='uni':
        a+=1
    # La función retorna el valor requerido
    return a
  # En caso sea el texto sea vacío
  else:
  # La función retorna el valor de cero
     return 0
```

'''

markdown_text2 = '''

```python
# Definimos la lista
lista = [1,2,[3,4],[5,[100,200,['UNI']],23,11],1,7]
# Accedemos al cuarto elemento
lista[3]
# Dentro de este, accedemos al segundo elemento
lista[3][1]
# Y dentro de este accedemos al tercer elemento
lista[3][1][2]
# Convertimos a texto
''.join(lista[3][1][2])

```

'''

markdown_text3a = '''

```python
# Calculamos los 40 números igualmente espaciados
valores = np.arange(0, 1, 1/40)
# Convertimos en array bidimensional
valores = np.arange(0, 1, 1/40).reshape(8,5)
# Convertimos en objeto matrix con ciertas filas y columnas
matriz = np.asmatrix(np.arange(0, 1, 1/40).reshape(8,5))
# Imprimimos la variable matriz
print(matriz)
```

'''
markdown_text3ae = '''

```python
matrix([[0.   , 0.025, 0.05 , 0.075, 0.1  ],
       [0.125, 0.15 , 0.175, 0.2  , 0.225],
       [0.25 , 0.275, 0.3  , 0.325, 0.35 ],
       [0.375, 0.4  , 0.425, 0.45 , 0.475],
       [0.5  , 0.525, 0.55 , 0.575, 0.6  ],
       [0.625, 0.65 , 0.675, 0.7  , 0.725],
       [0.75 , 0.775, 0.8  , 0.825, 0.85 ],
       [0.875, 0.9  , 0.925, 0.95 , 0.975]])

```

'''

markdown_text3b = '''

```python
# Creamos números aleatorios normales con media 0 y varianza 1
aleatorios = np.random.normal(0, 1, 50)
# Representamos estos valores mediante un arreglo
# bidimensional
arreglo = aleatorios.reshape(10,5)
# Convertimos en objeto  matriz
matriz = np.asmatrix(aleatorios.reshape(10,5))
# Imprimimos
print(matriz)
```

'''
markdown_text3be = '''

```python
matrix([[-0.10226413, -1.34125047, -0.13386513,  2.15189292, -0.61179892],
        [-0.70664993,  0.60064399, -1.18887192, -1.04069256,  0.35992693],
        [-0.04139183, -0.81712515,  0.90562221, -0.22039505,  2.10836717],
        [-0.04877813,  0.84881221,  0.23984609,  2.36915812,  0.0280591 ],
        [ 0.32413859, -1.25694415,  0.23124854,  0.15399081, -1.0033962 ],
        [ 0.60683229,  0.36962607,  0.37681542, -0.37938665,  0.09107135],
        [ 0.02244731, -0.26146915, -0.81421217,  1.11174807, -0.67464456],
        [ 0.51495572,  0.07486584, -0.40001776,  1.02854471,  0.31850721],
        [ 0.12952579,  0.56693087, -0.25516074, -0.64943087,  0.60392216],
        [ 0.00833904, -0.21042716, -0.79300066, -0.76444293, -1.6353839 ]])
```

'''

markdown_text4 = '''

```python
# Defino una función que recibe un arreglo bidimensional
# o matriz y retorna el valor de la desviación estándar
# de todos sus elementos y un arreglo de la desviación
# estándar de sus filas.
def desviacion_matriz(matriz):
  # Convertimos en objeto matriz para un mejor tratamiento
  mt = np.asmatrix(matriz)
  # Calculamos la std de todos los elementos de la matriz
  std_total = mt.std()
  # Inicializamos una lista que contrendá la std por filas
  lista_std = []
  # Iteramos para obtener
  for i in list(range(len(mt))):
    # Calculos la std para cada fila
    filastd = mt[i,:].reshape(-1).std()
    # Colocamos los std por filas en la lista
    lista_std.append(filastd)
  return std_total,lista_std

```

'''

markdown_text4e = '''

```python
# Utilizamos la función:
std_total,std_por_filas = desviacion_matriz(mat)
# Desviación estándar de todo los elementos:
print(std_total)
7.21
# Desvición estándar por filas
print(std_por_filas)
[1.4142135623730951,
 1.4142135623730951,
 1.4142135623730951,
 1.4142135623730951,
 1.4142135623730951]

```

'''

layout = html.Div(children=[
  html.H1('Pregunta 1',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
  html.H4('Debe usted crear una función que reciba un texto y cuente en número de veces que aparece UNI. Por ejemplo, en el texto "La UNI es la mejor universidad del país, porque los estudiantes UNI son los mejores", la función te debería retornar el valor de 2 (No debe diferenciar entre mayúsculas y minúsculas.'),

  # dcc.Markdown(children=markdown_text)
  # dbc.Row([dbc.Col(html.Div([dcc.Loading(id="loading-16",type="cube",children=[html.Div(dcc.Graph(id='graph2',))])]),xs=12, sm=12, md=11, lg=6, xl=6),
  #         dbc.Col(html.Div([dcc.Loading(id="loading-17",type="cube",children=[html.Div(dcc.Markdown(children=markdown_text))])]),xs=12, sm=12, md=11, lg=6, xl=6)]
  # ,justify="center"),

  dbc.Row([

        dbc.Col([
            html.H4("Cuenta las veces que aparece la palabra UNI",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
            # html.P(
            #     "Ingrese una frase",
            #
            # ),
            dcc.Input(id="input_1",placeholder='Escriba una frase ...',size='70'),
            html.Br(),
            dcc.Graph(id='Ind1'),
            # html.Div(id="output"),

        ],# width={'size':5, 'offset':1, 'order':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
            dcc.Markdown(children=markdown_text)
        ], #width={'size':5, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

    ], no_gutters=False, justify='center'),
    html.Br(),
    html.H1('Pregunta 2 ',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
    html.H4("De la lista muestre UNI => lst = [1,2,[3,4],[5,[100,200,['UNI']],23,11],1,7]"),
    dbc.Row([

          dbc.Col([
              html.H4("Muestra el elemento 'UNI'",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
              # html.P(
              #     "Ingrese una frase",
              #
              # ),
              # dcc.Input(id="input_1",placeholder='Escriba una frase ...',),
              html.Br(),
              # dcc.Markdown("'UNI'"),
              html.H1("'UNI'",style={"textAlign": "center"}),
              # dcc.Graph(id='Ind2'),
              # html.Div(id="output"),

          ],# width={'size':5, 'offset':1, 'order':1},
             xs=12, sm=12, md=12, lg=5, xl=5
          ),

          dbc.Col([
              html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
              dcc.Markdown(children=markdown_text2)
          ], #width={'size':5, 'offset':0, 'order':2},
             xs=12, sm=12, md=12, lg=5, xl=5
          ),

      ], no_gutters=False, justify='center'),
      html.Br(),
      html.H1('Pregunta 3 (a)',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
      html.H4("Cree una matriz de 40 puntos linealmente espaciados entre 0 y 1"),
      dbc.Row([

            dbc.Col([
                html.H4("Muestra la matriz",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                # html.P(
                #     "Ingrese una frase",
                #
                # ),
                # dcc.Input(id="input_1",placeholder='Escriba una frase ...',),
                html.Br(),
                # dcc.Markdown("'UNI'"),
                # html.H4("markdown_text3ae",style={"textAlign": "center"}),
                dcc.Markdown(children=markdown_text3ae)
                # dcc.Graph(id='Ind2'),
                # html.Div(id="output"),

            ],# width={'size':5, 'offset':1, 'order':1},
               xs=12, sm=12, md=12, lg=5, xl=5
            ),

            dbc.Col([
                html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                html.Br(),
                dcc.Markdown(children=markdown_text3a)
            ], #width={'size':5, 'offset':0, 'order':2},
               xs=12, sm=12, md=12, lg=5, xl=5
            ),

        ], no_gutters=False, justify='center'),
        html.Br(),
        html.H1('Pregunta 3 (b)',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
        html.H4("Genere una matriz de 50 números aleatorios muestreados a partir de una distribución normal estándar"),
        dbc.Row([

              dbc.Col([
                  html.H4("Muestra la matriz",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                  # html.P(
                  #     "Ingrese una frase",
                  #
                  # ),
                  # dcc.Input(id="input_1",placeholder='Escriba una frase ...',),
                  html.Br(),
                  # dcc.Markdown("'UNI'"),
                  dcc.Markdown(children=markdown_text3be),
                  # dcc.Graph(id='Ind2'),
                  # html.Div(id="output"),

              ],# width={'size':5, 'offset':1, 'order':1},
                 xs=12, sm=12, md=12, lg=5, xl=5
              ),

              dbc.Col([
                  html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                  html.Br(),
                  dcc.Markdown(children=markdown_text3b)
              ], #width={'size':5, 'offset':0, 'order':2},
                 xs=12, sm=12, md=12, lg=5, xl=5
              ),

          ], no_gutters=False, justify='center'),
          html.Br(),
          html.H1('Pregunta 4',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
          html.H4("De la matriz 'mat = np.arange(1,26).reshape(5,5)' calcule la desviación estandar de las filas y toda la matriz"),
          dbc.Row([

                dbc.Col([
                    html.H4("Muestra las desvición estándar total y por filas",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                    # html.P(
                    #     "Ingrese una frase",
                    #
                    # ),
                    # dcc.Input(id="input_1",placeholder='Escriba una frase ...',),
                    html.Br(),
                    # dcc.Markdown("'UNI'"),
                    dcc.Markdown(children=markdown_text4e),
                    # dcc.Graph(id='Ind2'),
                    # html.Div(id="output"),

                ],# width={'size':5, 'offset':1, 'order':1},
                   xs=12, sm=12, md=12, lg=5, xl=5
                ),

                dbc.Col([
                    html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                    html.Br(),
                    dcc.Markdown(children=markdown_text4)
                ], #width={'size':5, 'offset':0, 'order':2},
                   xs=12, sm=12, md=12, lg=5, xl=5
                ),

            ], no_gutters=False, justify='center')

])

@app.callback(
    Output("Ind1", "figure"),
    Input("input_1", "value"),
    )
def update_output(texto):
  num = cuenta_texto(texto)
  fig = go.Figure(go.Indicator(
    mode = "number",
    title = {"text": "Veces"},
    value = num,
    # title = {'text': "Speed"},
    domain = {'x': [0, 1], 'y': [0, 1]}
    ))
  fig.update_layout(
    autosize=False,
    # width=490,
    height=390,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor ='rgba(0,0,0,0)',
    margin=dict(
        l=53,
        r=10,
        b=50,
        t=50,
        pad=1
    )
    )
  return fig
