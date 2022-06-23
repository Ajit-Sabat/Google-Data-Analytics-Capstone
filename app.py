from logging import PlaceHolder
from turtle import width
import pandas as pd
import numpy as np
import json
import os
import re
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import State, Input, Output
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
from amortization.schedule import amortization_schedule
from pyparsing import col
from tabulate import tabulate

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
             meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])


app.layout=dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.H1("Loan Calculator:")
                ])
            ],justify="around",className="mb-3 mt-1"),
            dbc.Row([
                dbc.Col([
                    html.H4("Principal:",style={"textAlign":"center","color":"#632626","fontWeight":"bold"})
                ]),
                dbc.Col([
                    dcc.Input(id='Principal', type='number', min=1, max=100000000,placeholder="")
                ],width=2),
                dbc.Col([
                    html.H4("Interest:",style={"textAlign":"center","color":"#632626","fontWeight":"bold"})
                ]),
                dbc.Col([
                    dcc.Input(id='Interest', type='number', min=1, max=25,placeholder="")
                ],width=2),
                dbc.Col([
                    html.H4("Tenor:",style={"textAlign":"center","color":"#632626","fontWeight":"bold"})
                ]),
                dbc.Col([
                    dcc.Input(id='Tenor', type='number', min=1, max=240,placeholder="")
                ],width=2)

            ],justify="around",className="mb-3 mt-1"),
            dbc.Row([

            ]),
            dbc.Row([
                dbc.Button(id="submit", n_clicks=0, children= 'submit',style={"textAlign":"center","color":"#632626","fontWeight":"bold","width":"200px"})
            ],justify="center",className="mb-3 mt-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("EMI",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="EMI", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"})

                        ])
                    ])
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                           html.H5("Overall Amount",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="overall_amt", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"}) 
                        ])
                    ])
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Flat",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="flat", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"})
                        ])
                    ])
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Extra",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="extra", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"})
                        ])
                    ])
                ],width=3),
            ],justify="around",className="mb-3 mt-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Extra/Year",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="ext/yr", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"})
                        ])
                    ])
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Extra/Month",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="ext/mon", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"})
                        ])
                    ])
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Extra/Day",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="ext/day", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"})
                        ])
                    ])
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Monthly%",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="monthly%", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"})
                        ])
                    ])
                ],width=3),
            ],justify="around",className="mb-3 mt-1")

        ])
    ])   
])


###-----------------------------------------------------------------------------------------------

@app.callback(
    [Output("EMI","children"),
     Output("overall_amt","children"),
     Output("flat","children"),
     Output("extra","children"),
     Output("ext/yr","children"),
     Output("ext/mon","children"),
     Output("ext/day","children"),
     Output("monthly%","children")],
     [Input("submit", "n_clicks")],
     [State("Principle","value"),
     State("Interest","value"),
     State("Tenor","value")
     ]
    )

def update_cards(n_clicks,Principal,Interest,Tenor):
    # p=Principle
    # r=Interest
    # n=Tenor
    int_rate=Interest/100
    EMI=(int_rate/12) * (1/(1-(1+int_rate/12)**(-Tenor)))*Principle
    # overall_amt= EMI * tenor
    # flat=((((EMI*Tenor)-Principle)*12/Tenor)/Principle)*100
    # extra=Principle+(EMI*Tenor)-Principle-Principle
    # extPeryr = extra/Tenor
    # extPermon = Extra_per_month*12
    # extPerday= Extra_per_month/30

    return EMI,overall_amt,flat,extra,extPeryr,extPermon,extPerday





if __name__ == "__main__":
      app.run_server(debug=True,port=8555)