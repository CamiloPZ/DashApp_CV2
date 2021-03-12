import pandas as pd
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import dash_core_components as dcc
import plotly_express as px
import dash_table
import pathlib
import plotly.figure_factory as ff
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("Belcorp.csv"),sep=';',encoding='latin-1')
dff  = pd.read_csv(DATA_PATH.joinpath("Salaries.csv"),sep=',')
dff2 = dff[['JobTitle','Id']].groupby(['JobTitle']).count().reset_index().sort_values('Id',ascending=False)
# dff2.head(5)
data = df.head()
df2 = df[['Prioridad_Negocio_VD','Ocupacion']].groupby(['Ocupacion']).count().reset_index()

fig2 = px.pie(df2, values='Prioridad_Negocio_VD', names='Ocupacion',color_discrete_sequence=px.colors.qualitative.Safe)
fig2.update_layout(

    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor ='rgba(0,0,0,0)',
    margin=dict(
        l=53,
        r=10,
        b=50,
        t=50,
        pad=1
    ),
    title={'text':"<b>Ocupación VS Porque Prioridad_Negocio_VD<b>",
            # 'y':0.928,
            'x':0.48,
                                    'yanchor': 'middle',
                                    'xanchor': 'center'
                                    },
    # legend=dict(    orientation="h",
    #                             yanchor="bottom",
    #                             y=0.93,
    #                             xanchor="right",
    #                             x=1
    #                         ),
    )

fig1 = px.histogram(df, x="Ocupacion",color='Ocupacion')
fig1.update_layout(
    # autosize=False,
    # width=490,
    yaxis_title_text='<b>Recuento<b>',
    xaxis_title_text='<b>Ocupación<b>',
    # height=390,
    # title='Gráfico de Frecuencias',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor ='rgba(0,0,0,0)',
    margin=dict(
        l=53,
        r=10,
        b=50,
        t=50,
        pad=1
    ),
    xaxis={'categoryorder':'total descending'},
    title={'text':"<b>Gráfico de Frecuencias<b>",
            'y':0.928,
            'x':0.48,
                                    'yanchor': 'middle',
                                    'xanchor': 'center'
                                    },
    # legend=dict(    orientation="h",
    #                             yanchor="bottom",
    #                             y=0.93,
    #                             xanchor="right",
    #                             x=1
    #                         ),
    )

fig3 = px.histogram(df, x="Ocupacion",color='Porque_VD',color_discrete_sequence=px.colors.qualitative.T10)
fig3.update_layout(barmode='group')
fig3.update_layout(
    # autosize=False,
    # width=490,
    yaxis_title_text='<b>Recuento<b>',
    xaxis_title_text='<b>Ocupación<b>',
    # height=390,
    # title='Gráfico de Frecuencias',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor ='rgba(0,0,0,0)',
    margin=dict(
        l=53,
        r=10,
        b=50,
        t=50,
        pad=1
    ),
    title={'text':"<b>Ocupación VS Porque VD<b>",
            'y':0.928,
            'x':0.48,
                                    'yanchor': 'middle',
                                    'xanchor': 'center'
                                    },
    # legend=dict(    orientation="h",
    #                             yanchor="bottom",
    #                             y=0.93,
    #                             xanchor="right",
    #                             x=1
    #                         ),
    )

fig4 = px.histogram(dff, x="OtherPay", nbins=50)
fig4.update_layout(
    # autosize=False,
    # width=490,
    yaxis_title_text='<b>Recuento<b>',
    xaxis_title_text='<b>OtherPay<b>',
    # height=390,
    # title='Gráfico de Frecuencias',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor ='rgba(0,0,0,0)',
    margin=dict(
        l=53,
        r=10,
        b=50,
        t=50,
        pad=1
    ),
    title={'text':"<b>Histograma de  OtherPay con 50 bins<b>",
            'y':0.928,
            'x':0.48,
                                    'yanchor': 'middle',
                                    'xanchor': 'center'
                                    },
    # legend=dict(    orientation="h",
    #                             yanchor="bottom",
    #                             y=0.93,
    #                             xanchor="right",
    #                             x=1
    #                         ),
    )
markdown_text5 = '''

```python
# Importamos la data, pero utilizamos 'encoding="latin-1"' debido a que la data contiene caracteres especiales
df = pd.read_csv('Belcorp.csv',sep=';',encoding='latin-1')
# Visualizamos las cabeceras
df.head()

```

'''

markdown_text6 = '''

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8500 entries, 0 to 8499
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype
---  ------                --------------  -----
 0   Codigo                8500 non-null   object
 1   Reclutamiento         8500 non-null   object
 2   Ocupacion             8500 non-null   object
 3   Jefe_Hogar            8500 non-null   object
 4   Prioridad_Negocio_VD  8500 non-null   object
 5   Porque_VD             8500 non-null   object
 6   Tiene_TC              8500 non-null   object
 7   Tiene_Prestamo        8500 non-null   object
 8   Venta_Competencia     8500 non-null   object
 9   email                 8500 non-null   object
 10  telefono_fijo         8500 non-null   object
 11  telefono_movil        8500 non-null   object
 12  Target                8500 non-null   int64
dtypes: int64(1), object(12)
memory usage: 863.4+ KB
```

'''

markdown_text6e = '''

```python
# Visualizamos información de las variables
df.info()
# Vemos que tenemos 12 variables
# Veamos los valores que tiene la variable Ocupación
df.Ocupacion.unique()
```

'''

markdown_text7 = '''

```python
# Importamos la data
dff = pd.read_csv('Salaries.csv', sep =',')
# Agrupamos para hacer un recuento de la variable de interés y ordenamos
dff2 = dff[['JobTitle','Id']].groupby(['JobTitle']).count().reset_index().sort_values('Id',ascending=False)
# Nos quedamos con los 5 valores más altos
top_5 = dff2.head(5)
# Imprimimos
print(top_5)
```

'''
markdown_text7e = '''

```python
      JobTitle     Id
 TRANSIT OPERATOR  2388
 Transit Operator  2269
 Registered Nurse  1788
 Special Nurse     1468
 Police Officer 3  1423
```

'''

markdown_text8 = '''

```python
fig4 = px.histogram(dff, x="OtherPay", nbins=50)
fig4.update_layout(

    yaxis_title_text='<b>Recuento<b>',
    xaxis_title_text='<b>OtherPay<b>',)
fig4.show()
```

'''
layout = html.Div(children=[
  html.H1('Pregunta 5',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
  html.H3("Importe la data 'Belcorp' y muestre las cabeceras"),
  dbc.Row([

        dbc.Col([
            html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
            html.Br(),
            dcc.Markdown(children=markdown_text5)
        ], #width={'size':5, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=11, xl=11
        ),
        dbc.Col([
            html.H4("Cabeceras de la data",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
            # html.P(
            #     "Ingrese una frase",
            #
            # ),
            # dcc.Input(id="input_1",placeholder='Escriba una frase ...',),
            html.Br(),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in data.columns],
                data=data.to_dict('records'),
                )
            # dcc.Markdown("'UNI'"),
            # dcc.Markdown(children=markdown_text4e),
            # dcc.Graph(id='Ind2'),
            # html.Div(id="output"),

        ],# width={'size':5, 'offset':1, 'order':1},
           xs=12, sm=12, md=12, lg=11, xl=11
        ),

    ], no_gutters=False, justify='center'),
    html.Br(),
    html.H1('Pregunta 6',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
    html.H3("De la data 'Belcorp' muestre la información de variables y describa mediante gráficos la variable 'Ocupacion'"),
    dbc.Row([

          dbc.Col([
              html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
              html.Br(),
              dcc.Markdown(children=markdown_text6e)
          ], #width={'size':5, 'offset':0, 'order':2},
             xs=12, sm=12, md=12, lg=5, xl=5
          ),
          dbc.Col([
              html.H4("Información de las variables",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
              # html.P(
              #     "Ingrese una frase",
              #
              # ),
              # dcc.Input(id="input_1",placeholder='Escriba una frase ...',),
              html.Br(),
              dcc.Markdown(children=markdown_text6)
              # dcc.Markdown("'UNI'"),
              # dcc.Markdown(children=markdown_text4e),
              # dcc.Graph(id='Ind2'),
              # html.Div(id="output"),

          ],# width={'size':5, 'offset':1, 'order':1},
             xs=12, sm=12, md=12, lg=5, xl=5
          ),

      ], no_gutters=False, justify='center'),
      dbc.Row(
          [
              dbc.Col(dcc.Graph(id='Indicadores1',figure=fig1),xs=12 ,sm=9, lg=4),
              dbc.Col(dcc.Graph(id='Indicadores2',figure=fig2),xs=12 ,sm=9, lg=4),
              dbc.Col(dcc.Graph(id='Indicadores3',figure=fig3),xs=12 ,sm=9, lg=4),
              # dbc.Col(html.Div([dcc.Loading(id="loading-10",type="cube",children=[html.Div(dcc.Graph(id='Indicadores2',))])]),xs=12 ,sm=9, lg=4),
              # dbc.Col(html.Div([dcc.Loading(id="loading-11",type="cube",children=[html.Div(dcc.Graph(id='Indicadores3',))])]),xs=12 ,sm=9, lg=4),

          ],no_gutters=True,justify="center"
      ),
      html.Br(),
      html.H1('Pregunta 7',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
      html.H3("De la data 'Salaries' indique el top 4 de la variable 'JobTitle' ¿Cuáles son los 5 trabajos más comunes?"),
      dbc.Row([

            dbc.Col([
                html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                html.Br(),
                dcc.Markdown(children=markdown_text7)
            ], #width={'size':5, 'offset':0, 'order':2},
               xs=12, sm=12, md=12, lg=5, xl=5
            ),
            dbc.Col([
                html.H4("Trabajos más comunes",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                # html.P(
                #     "Ingrese una frase",
                #
                # ),
                # dcc.Input(id="input_1",placeholder='Escriba una frase ...',),
                html.Br(),
                dcc.Markdown(children=markdown_text7e)
                # dcc.Markdown("'UNI'"),
                # dcc.Markdown(children=markdown_text4e),
                # dcc.Graph(id='Ind2'),
                # html.Div(id="output"),

            ],# width={'size':5, 'offset':1, 'order':1},
               xs=12, sm=12, md=12, lg=5, xl=5
            ),

        ], no_gutters=False, justify='center'),
        html.Br(),
        html.H1('Pregunta 8',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
        html.H3("De la data 'Salaries' crear un histograma de la variable 'OtherPay' con 50 bins, ademas muestre la línea del histograma de color rojo."),
        dbc.Row([

              dbc.Col([
                  html.H4("Código Python empleado:",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                  html.Br(),
                  dcc.Markdown(children=markdown_text8)
              ], #width={'size':5, 'offset':0, 'order':2},
                 xs=12, sm=12, md=12, lg=5, xl=5
              ),
              dbc.Col([
                  html.H4("Trabajos más comunes",style={"textAlign": "center","font-style":"italic","color":"#B8860B","font-weight":"bold"}),
                  # html.P(
                  #     "Ingrese una frase",
                  #
                  # ),
                  # dcc.Input(id="input_1",placeholder='Escriba una frase ...',),
                  html.Br(),
                  # dcc.Markdown(children=markdown_t    ext7e)
                  # dcc.Markdown("'UNI'"),
                  # dcc.Markdown(children=markdown_text4e),
                  dcc.Graph(id='In',figure= fig4),
                  # html.Div(id="output"),

              ],# width={'size':5, 'offset':1, 'order':1},
                 xs=12, sm=12, md=12, lg=5, xl=5
              ),

          ], no_gutters=False, justify='center'),

])
