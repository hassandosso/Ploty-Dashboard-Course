import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Data/mpg.csv')

data = [go.Scatter(x=df['displacement'],
                    y=df['acceleration'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(size=df['weight']/200,
                                color=df['cylinders'],
                                showscale=True)
                    )]
layout = go.Layout(title='Bubble charts',hovermode='closest')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)