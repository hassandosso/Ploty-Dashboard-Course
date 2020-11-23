import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('Data/abalone.csv')
#print(df.head())
rings1 = np.random.choice(df['rings'],40,replace=False)
rings2 = np.random.choice(df['rings'],60,replace=False)
data = [go.Box(y=rings1, name='Sample 1'),
            go.Box(y=rings2,name='Sample 2')]
layout = go.Layout(title='Comparison of 2 random rings data')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)