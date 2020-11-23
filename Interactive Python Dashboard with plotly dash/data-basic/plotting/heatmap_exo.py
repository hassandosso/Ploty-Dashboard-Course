import plotly.offline as pyo
import plotly.graph_objs as go
#from plotly import subplots
import pandas as pd

df = pd.read_csv('Data/flights.csv')

trace = go.Heatmap(x=df['year'],y=df['month'],
                    z=df['passengers'],
                    colorscale='Jet')
fig = go.Figure([trace])
fig['layout'].update(title='flights passengers')
pyo.plot(fig)
