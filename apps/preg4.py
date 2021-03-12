import pandas as pd
import dash
import dash_html_components as html
import plotly_express as px
import pandas as pd
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import numpy as np
import pathlib
from app import app



PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("Belcorp.csv"),sep=';',encoding='latin-1')
dff  = pd.read_csv(DATA_PATH.joinpath("Salaries.csv"),sep=',')
df_new = dff.select_dtypes(include=np.number).drop(['Benefits','Notes','Status','Id','Year'],axis=1)



df2 = df[['Target','Codigo']].groupby(['Target']).count().reset_index()
fig2 = px.pie(df2, values='Codigo', names='Target',color_discrete_sequence=px.colors.qualitative.Safe)
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
    title={'text':"<b>Data desbalanceada",
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

fig3 = px.histogram(df, x="Ocupacion",color='Target',color_discrete_sequence=px.colors.qualitative.T10)
fig3.update_layout(barmode='stack')
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
    title={'text':"<b>Ocupación VS Target VD<b>",
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

fig4 = px.histogram(df, x="Jefe_Hogar",color='Target',color_discrete_sequence=px.colors.qualitative.Set1)
fig4.update_layout(barmode='group')
fig4.update_layout(
    # autosize=False,
    # width=490,
    yaxis_title_text='<b>Recuento<b>',
    xaxis_title_text='<b>Jefe_Hogar<b>',
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
    title={'text':"<b>Jefe_Hogar VS Target<b>",
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

fig5 = px.histogram(df, x="Tiene_Prestamo",color='Target',color_discrete_sequence=px.colors.qualitative.Bold)
fig5.update_layout(barmode='group')
fig5.update_layout(
    # autosize=False,
    # width=490,
    yaxis_title_text='<b>Recuento<b>',
    xaxis_title_text='<b>Tiene_Prestamo<b>',
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
    title={'text':"<b>Tiene_Prestamo VS Target<b>",
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

fig6 = px.histogram(df, x="Reclutamiento",color='Target',color_discrete_sequence=px.colors.qualitative.Dark2)
fig6.update_layout(barmode='group')
fig6.update_layout(
    # autosize=False,
    # width=490,
    yaxis_title_text='<b>Recuento<b>',
    xaxis_title_text='<b>Reclutamiento<b>',
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
    title={'text':"<b>Reclutamiento VS Target<b>",
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

layout = html.Div(children=[
  html.H1('Pregunta 12',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
  html.H3('De la data "Salaries" hacer un diagrama de correlaciones con las variables numéricas'),
  # html.H1("Scatter Matrix of USA Social Capital Project", style={'textAlign':'center'}),
    dbc.Label("Variable cuantitativa"),
    dcc.Dropdown(
        id='my-dropdown',
        options=[{'label': s, 'value': s} for s in df_new.columns],
        value=["BasePay",
               "OvertimePay","OtherPay"
               ],
        multi=True
    ),
    html.Br(),
    dcc.Loading(id="loading-5",type="cube",children=[dcc.Graph(id="my-chart", figure={})],),
    html.Br(),
    html.H1('Pregunta 13',style={"textAlign": "center","font-style":"italic","color":"#00008B","font-weight":"bold"}),
    html.H3('Analizar la data Belcorp, hacer un análisis descriptivo de las variables, identificar nulos, ejecutar un modelo de regresión'),
    dbc.Row(html.Br())
    ,
    dbc.Row(
        [
            dbc.Col(html.Div([dcc.Loading(id="loading-9",type="cube",children=[html.Div(dcc.Graph(id='Indicadores1',figure=fig2))])]),xs=12 ,sm=9, lg=4),
            dbc.Col(html.Div([dcc.Loading(id="loading-10",type="cube",children=[html.Div(dcc.Graph(id='Indicadores2',figure=fig3))])]),xs=12 ,sm=9, lg=4),
            dbc.Col(html.Div([dcc.Loading(id="loading-11",type="cube",children=[html.Div(dcc.Graph(id='Indicadores3',figure=fig4))])]),xs=12 ,sm=9, lg=4),

        ],no_gutters=True,justify="center"
    ),
    dbc.Row(html.Br()),
    dbc.Row(
    [
        dbc.Col(html.Div([dcc.Loading(id="loading-12",type="cube",children=[html.Div(dcc.Graph(id='Indicadores4',figure=fig5))])]),xs=12 ,sm=9, lg=5),
        dbc.Col(html.Div([dcc.Loading(id="loading-13",type="cube",children=[html.Div(dcc.Graph(id='Indicadores5',figure=fig6))])]),xs=12 ,sm=9, lg=5),
        # dbc.Col(html.Div([dcc.Loading(id="loading-14",type="cube",children=[html.Div(dcc.Graph(id='Indicadores6',))])]),xs=12 ,sm=9, lg=4),

    ],no_gutters=True,justify="center"

    )
    # html.H1("Scatter Matrix of USA Social Capital Project", style={'textAlign':'center'}),

      # dcc.Dropdown(
      #     id='my-dropdown',
      #     options=[{'label': s, 'value': s} for s in df_new.columns],
      #     value=["BasePay",
      #            "OvertimePay","OtherPay"
      #            ],
      #     multi=True
      # ),
      # html.Br(),
      # dcc.Graph(id="my-chart", figure={}),

])


@app.callback(
      Output(component_id='my-chart', component_property='figure'),
     Input(component_id='my-dropdown', component_property='value')
)
def update_graph(dpdn_val):
    if len(dpdn_val) > 0:
        fig = px.scatter_matrix(df_new, dimensions=dpdn_val, #color='TotalPay',
                                )
        fig.update_traces(diagonal_visible=False, showupperhalf=True, showlowerhalf=True)
        # fig.update_layout(yaxis1={'title':{'font':{'size':3}}}, yaxis2={'title':{'font':{'size':3}}},
        #                   yaxis3={'title':{'font':{'size':3}}}, yaxis4={'title':{'font':{'size':3}}},
        #                   yaxis5={'title':{'font':{'size':3}}}, yaxis6={'title':{'font':{'size':3}}},
        #                   yaxis7={'title':{'font':{'size':3}}}, yaxis8={'title':{'font':{'size':3}}}
        #                   )
        # fig.update_layout(xaxis1={'title':{'font':{'size':3}}}, xaxis2={'title':{'font':{'size':3}}},
        #                   xaxis3={'title':{'font':{'size':3}}}, xaxis4={'title':{'font':{'size':3}}},
        #                   xaxis5={'title':{'font':{'size':3}}}, xaxis6={'title':{'font':{'size':3}}},
        #                   xaxis7={'title':{'font':{'size':3}}}, xaxis8={'title':{'font':{'size':3}}}
                          # )
        fig.update_layout(

        # plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor ='rgba(0,0,0,0)',
        autosize=False,
        height = 700
        )
        return fig

    if len(dpdn_val)==0:
        return dash.no_update
