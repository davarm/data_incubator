from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure


longitude  = [44.990961]
latitude = [41.552164]

source = ColumnDataSource(data=dict(longitude=longitude, latitude=latitude))

p = figure(plot_width=400, plot_height=400)
p.circle(x='longitude', y='latitude', source=source)
show(p)
