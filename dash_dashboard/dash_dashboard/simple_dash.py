import dash_core_components as dcc
import dash_html_components as html
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
                html.Div([
                    html.Div([
                        'Testing Dashboard'
                    ], className='card-header'),
                    html.Div([
                        dcc.Graph(
                            id='example-graph3',
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                                ],
                                'layout': {
                                    'title': 'Dash Data Visualization'
                                },
                            },
                        ),
                    ], className='card-body'),
                ], className='card')
            ], className='col-md-6'),
        ], className='row')
    ]

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
