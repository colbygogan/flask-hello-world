import pandas as pd
import panel as pn
import numpy as np
from bokeh.plotting import figure

pn.extension()

# Create some data
data = pd.DataFrame({
    'x': range(50),
    'y': np.random.randn(50).cumsum()
})

# Create a Bokeh plot
plot = figure(title='Line plot!', x_axis_label='X-Axis', y_axis_label='Y-Axis')
plot.line(data['x'], data['y'], legend_label='Trend')

# Create a Panel pane for the Bokeh plot
plot_panel = pn.pane.Bokeh(plot)

# Create a data table
table = pn.widgets.DataFrame(data, name='Data Tablee')

# Create a Panel layout and display it
app = pn.Column("# My Panel App", plot_panel, table)

# Make the app servable and expose as a WSGI application
servable_app = app.servable()

def app(environ, start_response):
    """Simple WSGI application to serve the Panel app."""
    if not hasattr(servable_app, 'server'):
        servable_app.server = pn.io.server.get_server(servable_app)
    return servable_app.server.app(environ, start_response)

