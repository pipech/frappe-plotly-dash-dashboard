import dash_core_components as dcc
import dash_html_components as html
import frappe

from dash.dependencies import Input, Output

from dash_integration.dash_application import dash_app


layout = [
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    'Testing Dashboard'
                ], className='card-header'),
                html.Div([
                    dcc.Input(id='aaa', value='initial value', type='text'),
                    html.Div(id='bbb')
                ], className='card-body'),
            ], className='card')
        ], className='col-md-12')
    ], className='row')
]


@dash_app.callback(
    Output(component_id='bbb', component_property='children'),
    [Input(component_id='aaa', component_property='value')]
)
def update_output_div(input_value):
    print('=====================')
    print('callback', frappe.db.get_value('User', 'Administrator', 'user_type'))
    print('=====================')
    return 'You\'ve entered "{}"'.format(input_value)
