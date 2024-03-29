from dash_dashboard.dash_dashboard import simple_dash
from dash_dashboard.dash_dashboard import simple_dash2


def dashboard_route(dash_route):
    def route_wrapper(*args, **kwargs):
        dashboard = args[0]
        if dashboard == 'Testing 1':
            return simple_dash.get_layout()
        elif dashboard == 'Testing 2':
            return simple_dash2.layout
        else:
            return dash_route(*args, **kwargs)
    return route_wrapper


def dashboard_callback(dash_callback):
    def callback_wrapper(*args, **kwargs):
        simple_dash.update_pie_graph
        return dash_callback(*args, *kwargs)
    return callback_wrapper
