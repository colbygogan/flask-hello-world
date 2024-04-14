import pandas as pd
import panel as pn
import numpy as np
from bokeh.plotting import figure

# Initialize Panel with Bokeh for interactive plots
pn.extension()

# Create data for plotting
data = pd.DataFrame({
    'x': range(50),
    'y': np.random.randn(50).cumsum()
})

# Create a Bokeh plot
plot = figure(title='Interactive Line Plot', x_axis_label='X-Axis', y_axis_label='Y-Axis')
plot.line(data['x'], data['y'], legend_label='Trend')

# Embed plot into Panel
plot_panel = pn.pane.Bokeh(plot)

# Create a data table widget in Panel
table = pn.widgets.DataFrame(data, name='Data Table')

# Arrange plot and table vertically
app_layout = pn.Column("# My Panel App", plot_panel, table)

# Convert the Panel layout into a servable app, setting it to not start a server immediately
app = pn.io.server.get_server(app_layout).app


