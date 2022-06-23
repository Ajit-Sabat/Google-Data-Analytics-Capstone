#app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
#             meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])


#app.\
layout=dbc.Container([
    # dbc.Row([dcc.Location(id="url",refresh=True),
    #     dbc.Col([dcc.Link("Daily Dash |",href="/apps/metropolis")]),
    #     dbc.Col([dcc.Link("Monthly dash",href="/apps/MTD_metropolis")]),
    #     dbc.Row(id="page-content",children=[])
    # ]),
    dbc.Row([
        dbc.Col([
            dbc.Row([html.Img(src="/assets/MetroLogo.png",style={'height': '80px',
                            'width': 'auto',
                            'margin-bottom': '25px'})


        ],justify="around",className="mb-2 mt-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Offered",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="Total_offered",children="",style={'textAlign': 'center',
                      'color': '#632626',"fontWeight":"bold","background":"#BF8B67",
                      'fontSize': 21,
                      'margin-top': '5px'}),

                        ])
                    ],style={"backgroundColor":'#BF8B67',"height":"80px"})
                ],width=7)
            ],justify="around",className="mb-3 mt-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Answered",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="Total_Answered", children="", style={'textAlign': 'center',
                      'color': '#632626',"fontWeight":"bold","background":"#BF8B67",
                      'fontSize': 21,
                        "margin-top":"5px"}),

                        ])
                    ],style={"backgroundColor":'#BF8B67',"height":"80px"})
                ], width=7)
            ],justify="around",className="mb-3 mt-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Abandoned",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="abd Percent", children="", style={'textAlign': 'center',
                      'color': '#632626',"fontWeight":"bold","background":"#BF8B67",
                      'fontSize': 21,
                      "margin-top":"5px"}),

                        ])
                    ],style={"backgroundColor":'#BF8B67',"height":"80px"})
                ], width=7)
            ],justify="around", className="mb-3 mt-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("AHT",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="AHT", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"}),

                        ])
                    ],style={"backgroundColor":'#BF8B67',"height":"80px"})
                ], width=7)
            ],justify="around", className="mb-3 mt-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("SL",style={"textAlign":"center","color":"#632626","fontWeight":"bold"}),
                            html.H4(id="SL", children="", style={'textAlign': 'center',"fontWeight":"bold",
                                                                             'color': '#632626',"background":"#BF8B67",
                                                                             'fontSize': 21,
                                                                             "margin-top": "5px"
                                                                             }),

                        ])
                    ],style={"backgroundColor":'#BF8B67',"height":"80px"})
                ], width=7)
            ],justify="around", className="mb-3 mt-1"),
        ],width=3),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.H5("Date :",style={'textAlign': 'center',"fontWeight":"bold",'fontSize': 18,
                                                                             'color': '#BF8B67'})
                ],width=1,className="mt-2"),
                dbc.Col([
                    dcc.Dropdown(id="my-dropdown",
                                 options=filter_df["call_date"].dt.date.tail(1),
                                 value=date.today(),style={"backgroundColor":'white','fontSize': 20,
                                                           "color":"#632626",
                                                           "fontWeight":"bold"})
                ],width=3),
                # dbc.Col([
                #     html.H5("Page 2 :"),
                #     dbc.Row([
                #         dcc.Link("Daily Dash |",href="/apps/metropolis"),
                #         dcc.Link("Monthly dash",href="/apps/MTD_metropolis")
                #          ],className="mt-2"),
                #     dcc.Location(id="url",refresh=False),
                #         dbc.Row(id="page-content",children=[])
                # ],width=1),
                # dbc.Col([
                #     dcc.Dropdown(id="Month",options=data["Month"].unique(),
                #                  value=10,style={"backgroundColor":'white',
                #                                            "color":"#010915",
                #                                            "fontWeight":"bold"})
                # ],width=2)
            ],justify="left",className="mt-1 mb-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            #html.P("My Chart"),
                            dcc.Graph(id="My graph"
                                ),
                        ])
                    ],style={'background':"#632626"})
                ],width=12)
            ],className="mb-1"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            #html.P("Data Table"),
                            dash_table.DataTable(id="Table",
                                columns=[{"id":"start_time","name":"Interval","type":"numeric",
                                          "format":Format()  # formatted using the Format() object
                                                 .scheme(Scheme.fixed)
                                                 .precision(0)
                                                 #.symbol_prefix("$")
                                                 .symbol(Symbol.yes)
                                                 .symbol_suffix(":00")
                                                 .group(Group.yes)
                                          },
                                         {"id":"Offered","name":"Offered","type":"numeric"},
                                         {"id":"Answered_On_Agent","name":"Answered","type":"numeric"},
                                         {"id":"Abandoned","name":"Abandoned","type":"numeric","format":formatted},
                                         {"id":"Service_Level","name":"Service Level","type":"numeric","format":formatted}],
                                   #virtualization=True,
                                   #page_size=6,
                                    data=data.to_dict("records"),
                                   # filterable=True,
                                   #row_selectable=True,
                                   selected_rows=[],
                                   selected_columns=[],
                                   style_data_conditional=[],
                                   page_action="none",
                                   style_table={'height': '220px', 'overflow-Y': 'auto',"padding":"10px"},
                                   style_cell={"textAlign":"left",
                                               "min-width":"130px",
                                               "backgroundColor":'#632626',
                                               "color":"#BF8B67",
                                               "border-bottom":"0.01rem solid white"},
                                   style_header={"backgroundColor":"#632626","color":"#BF8B67","textAlign":"center",
                                                 "fontWeight":"bold",'border': '2px solid #BF8B67','fontSize': 18
                                                 },
                                   style_data={"textOverflow":"hidden","textAlign":"center",'border': '2px solid #BF8B67',
                                               "color":"#BF8B67",'fontSize': 18},
                                   fixed_rows={"headers":True}
                                    ),
                                ]),
                    ],style={'background':"#632626"}),
                ],width=11)
            ])
        ],width=9),

    ]),#,justify="left"),
],fluid=True,style={"background":"#632626"})

# 222741
@app.callback(
    Output("Table","data"),
    Input("my-dropdown","value")
)

def update_table(date_dd):
    new_table=data[data["call_date"]==date_dd]
    return new_table.to_dict("records")

@app.callback(

     [Output("My graph","figure"),
      Output('My graph','clickData')],
    Input("my-dropdown","value"),
)

def update_graph_table(date_value):
    graph_data = data[data["call_date"].isin([date_value])]

    fig=make_subplots(specs=[[{"secondary_y":True}]])
    fig.add_trace(go.Bar(x=graph_data["start_time"],
                             y=graph_data["Answered_On_Agent"],name="Answered",marker_color="#FF6361",
                             yaxis="y1",marker_line_width=0,
                             ), secondary_y=False)
    fig.add_trace(go.Bar(x=graph_data["start_time"],
                             y=graph_data["Offered"],name="Offered",marker_color="#BC5090",
                           yaxis="y2",marker_line_width=0,
                             ), secondary_y=False,)
    fig.add_trace(go.Scatter(x=graph_data[graph_data["call_date"]==date_value]["start_time"],
                             y=graph_data[graph_data["call_date"]==date_value]["Call_Abandoned"],
                             name="Abandoned",yaxis="y3",mode="lines",line=dict(color="#FFA600")),secondary_y=True)
    fig.update_xaxes(tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                          tickformat="H%:M%",
                     title_text="Time in Hrs.")
    fig.update_yaxes(
        title_text="Call_Abandoned",rangemode="tozero",#scaleanchor='y3', scaleratio=1, constraintoward='bottom',
        secondary_y=True)
    fig.update_yaxes(
        title_text="Offered"+"/"+"Answered",rangemode="tozero",#scaleanchor='y1', scaleratio=1, constraintoward='bottom',
        secondary_y=False)
    # fig.update_yaxes(
    #     title_text="Answered",
    #     secondary_y=False)
    fig.update_layout(height=280,plot_bgcolor="#632626",paper_bgcolor="#632626",showlegend=False,clickmode="event+select",barmode="group",
                      # legend=dict(orientation="h",
                      #             yanchor="bottom",
                      #             y=1.2,
                      #             xanchor="left",
                      #             x=.05,
                      #             font=dict(size=18,color="white")),
                      hovermode="x unified",
                      hoverlabel=dict(
                                bgcolor="#BF8B67",
                                font_size=16,
                                #font_family="Rockwell"
                                    ),
                      font=dict(family='sans-serif',
                      color='#632626',
                      size=16),
                      xaxis=dict(title='<b>Interval</b>',
                                 color='#BF8B67',
                                 showline=True,
                                 showgrid=False,
                                 showticklabels=True,
                                 linecolor='#BF8B67',
                                 linewidth=1,
                                 ticks='outside',
                                 tickfont=dict(
                                    # family='Aerial',
                                     color='#BF8B67',
                                     size=16
                                 )),
                      yaxis=dict(title="Offered / Answered",
                                 color='#BF8B67',
                                 showline=True,
                                 showgrid=False,
                                 showticklabels=True,
                                 linecolor='#BF8B67',
                                 linewidth=1,
                                 ticks='outside',
                                 tickfont=dict(
                                     #family='Aerial',
                                     color='#BF8B67',
                                     size=16
                                 )
                                 ),
                      yaxis2=dict(title="Abandoned",
                          color='#BF8B67',
                          showline=True,
                          showgrid=False,
                          showticklabels=True,
                          linecolor='#BF8B67',
                          linewidth=1,
                          ticks='outside',
                          tickfont=dict(
                             # family='Aerial',
                              color='#BF8B67',
                              size=16,
                              # anchor="free",
                              # overlaying="y",
                              # side="left",
                              # position=0.15
                          )))
    return fig,None


#--------------------------------------------------KPI Call-backs----------------------------------------------

@app.callback(
    [Output("Total_offered","children"),
    Output("Total_Answered", "children"),
    Output("abd Percent", "children"),
    Output("SL", "children")],
    Input("my-dropdown", "value")
)

def kpi_update(selected_date):

    offered=filter_df.groupby(["call_date","start_time"])["Offered"].sum().reset_index()
    total_offered=offered[(offered.call_date == selected_date)]["Offered"].sum()
    offered_format=f"{total_offered:}"

    ans=filter_df.groupby(["call_date","start_time"])["Answered_On_Agent"].sum().reset_index()
    total_answered=ans[(ans.call_date==selected_date)]["Answered_On_Agent"].sum()
    ans_format=f"{total_answered:}"

    df_new = filter_df[(filter_df.call_date == selected_date)]
    abandoned_percent = round(
        ((df_new["Call_Abandoned"] - df_new["Abandoned_10_Sec"]).sum() / df_new["Offered"].sum()) * 100, 2)
    aband_format = f"{abandoned_percent}%"

    df_new = filter_df[(filter_df.call_date == selected_date)]
    SL_percent = round((df_new["With_In_SL_Calls"].sum() / df_new["Offered-10_sec"].sum()) * 100, 2)
    SL_format = f"{SL_percent}%"


    return offered_format,ans_format,aband_format,SL_format

@app.callback(
    Output("AHT", "children"),
    Input("my-dropdown", "value"),)

def update_kpi(dd_date):
    df_aht=filter_df[(filter_df.call_date ==dd_date)]
    AHT_1=round((df_aht["T+H+W_time"].sum()//df_aht["Answered_On_Agent"].sum()))

    m=AHT_1//60
    AHT_1 %= 60
    second = AHT_1
    AHT_2= pd.to_timedelta(AHT_1, unit="s")
    # AHT_str = AT_2.astype("str")
    # AHT_time = AHT_2.str.replace("0 days ", "")
    AHT = f"{m}:{second}"
    return AHT
#------------------------------------Page Navigation Call-back---------------------------------

# @app.callback(
#     Output("page-content","children"),
#     Input("url","pathname"),
# )
#
# def display_page(pathname):
#     if pathname=="/metropolis":
#         return app.layout
#     if pathname=="/apps/MTD_metropolis":
#         return MTD_metropolis.layout
#     else:
#         return app.layout


# #--------------------------------------------------------------------------------------------------------------------
# @app.callback(Output('Table', 'data'),
#              [Input('my-dropdown','value'),
#               Input('My graph', 'clickData')])
#
# def load_selected_data(dropdown_value,clicked_data):
#     dff=data[data['call_date']==dropdown_value]
#     if clicked_data is not None:
#         row_ids = hl_tab_rows(clicked_data)
#         if len(row_ids) > 0:
#             return get_table_subset(row_ids).to_dict('records')
#         else:
#             return dff.to_dict('records')
#     else:
#         return dff.to_dict('records')
#
# def hl_tab_rows(clicked_data):
#     row_ids = []
#     if clicked_data is not None:
#         for p in clicked_data['points']:
#             row_ids.append(p["pointIndex"])
#     return row_ids
#
# def get_table_subset(row_ids):
#     return data[data[["start_time"]].isin(row_ids)]

# if __name__ == "__main__":
#      app.run_server(debug=False,port=8005)
