import dash_core_components as dcc
import dash_html_components as html
import dash_table
import frappe
import pandas as pd
import plotly.graph_objs as go

from dash.dependencies import Input, Output

from dash_integration.dash_application import dash_app


def get_layout():
    print('=====================')
    print(frappe.db.get_value('User', 'Administrator', 'user_type'))
    print('=====================')

    layout = [
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            'Sales'
                        ], className='card-header narrow'),
                        html.Div([
                            html.Div([
                                html.Div([
                                    '93k'
                                ], className='text-value'),
                                html.Div([
                                    'Total'
                                ], className='text-uppercase text-muted small'),
                            ]),
                            html.Div([
                                html.Div([
                                    '2.2m'
                                ], className='text-value'),
                                html.Div([
                                    'Total (USD)'
                                ], className='text-uppercase text-muted small'),
                            ]),
                        ], className='brand-card-body'),
                    ])
                ], className='brand-card'),
            ], className='col-md-3'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            'Purchase'
                        ], className='card-header narrow'),
                        html.Div([
                            html.Div([
                                html.Div([
                                    '93k'
                                ], className='text-value'),
                                html.Div([
                                    'Total'
                                ], className='text-uppercase text-muted small'),
                            ]),
                            html.Div([
                                html.Div([
                                    '2.2m'
                                ], className='text-value'),
                                html.Div([
                                    'Total (USD)'
                                ], className='text-uppercase text-muted small'),
                            ]),
                        ], className='brand-card-body'),
                    ])
                ], className='brand-card'),
            ], className='col-md-3'),
        ], className='row'),
        html.Div([
            html.Div([
                pie_bar_chart(),
            ], className='col-md-6'),
            html.Div([
                html.Div([
                    html.Div([
                        'Testing Dashboard'
                    ], className='card-header'),
                    html.Div([
                        dcc.Graph(
                            id='example-graph2',
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                                ],
                                'layout': {
                                    # 'title': 'Dash Data Visualization'
                                },
                            },
                        ),
                    ], className='card-body'),
                ], className='card')
            ], className='col-md-6')
        ], className='row'),
        html.Div([
            html.Div([
                line_chart(),
            ], className='col-md-12'),
        ], className='row'),
        html.Div([
            html.Div([
                get_dash_table(),
            ], className='col-md-12'),
        ], className='row'),
    ]

    return layout


def get_dash_table():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

    layout = html.Div([
        html.Div([
            'Example table'
        ], className='card-header'),
        html.Div([
            dash_table.DataTable(
                id='table',
                columns=[{'name': i, 'id': i} for i in df.columns],
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'State'},
                        'textAlign': 'left'
                    }
                ],
                style_cell={
                    'padding': '5px',
                },
                data=df.to_dict('records'),
            ),
        ], className='card-body'),
    ], className='card')

    return layout


def line_chart():
    layout = html.Div([
        html.Div([
            'US Export of Plastic Scrap'
        ], className='card-header'),
        html.Div([
            dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=[
                                1995, 1996, 1997, 1998, 1999,
                                2000, 2001, 2002, 2003, 2004,
                                2005, 2006, 2007, 2008, 2009,
                                2010, 2011, 2012,
                            ],
                            y=[
                                219, 146, 112, 127, 124, 180,
                                236, 207, 236, 263, 350, 430,
                                474, 526, 488, 537, 500, 439
                            ],
                            name='Rest of world',
                            marker=go.bar.Marker(
                                color='rgb(55, 83, 109)'
                            )
                        ),
                        go.Bar(
                            x=[
                                1995, 1996, 1997, 1998, 1999,
                                2000, 2001, 2002, 2003, 2004,
                                2005, 2006, 2007, 2008, 2009,
                                2010, 2011, 2012
                            ],
                            y=[
                                16, 13, 10, 11, 28, 37, 43,
                                55, 56, 88, 105, 156, 270,
                                299, 340, 403, 549, 499
                            ],
                            name='China',
                            marker=go.bar.Marker(
                                color='rgb(26, 118, 255)'
                            )
                        )
                    ],
                    layout=go.Layout(
                        showlegend=True,
                        legend=go.layout.Legend(
                            x=0,
                            y=1.0
                        ),
                        margin=go.layout.Margin(
                            l=40, r=0, t=40, b=30
                        ),
                    )
                ),
                style={'height': 300},
                id='my-bar-graph'
            ),
        ], className='card-body'),
    ], className='card')

    return layout


def pie_bar_chart():
    layout = html.Div([
        html.Div([
            'Ebola Cases Reported in Africa - 2014'
        ], className='card-header'),
        html.Div([
            dcc.Graph(id='my-pie-graph'),
            html.Div(
                [dcc.Slider(
                    id='month-selected',
                    min=3, max=12, value=8,
                    marks={
                        3: 'Mar', 4: 'Apr', 5: 'May',
                        6: 'Jun', 7: 'Jul', 8: 'Aug',
                        9: 'Sep', 10: 'Oct', 11: 'Nov',
                        12: 'Dec',
                    },
                )],
                style={
                    'textAlign': 'center', 'margin': '30px',
                    'padding': '10px', 'width': '90%',
                    'margin-left': 'auto', 'margin-right': 'auto'
                },
            ),
        ], className='card-body'),
    ], className='card')

    return layout


@dash_app.callback(
    Output('my-pie-graph', 'figure'),
    [Input('month-selected', 'value')]
)
def update_pie_graph(selected):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv')
    df = df.dropna(axis=0)
    return {
        'data': [
            go.Pie(
                labels=df['Country'].unique().tolist(),
                values=df[df['Month'] == selected]['Value'].tolist(),
                marker={
                    'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']
                },
                textinfo='label',
            )
        ],
        'layout': go.Layout(
            # title='Cases Reported Monthly',
        ),
    }
