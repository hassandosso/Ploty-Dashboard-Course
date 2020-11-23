import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#df = pd.read_csv('Data/2010SantaBarbaraCA.csv')
#print(df.columns)
df = pd.read_csv('Data/2010YumaAZ.txt')
data = [go.Heatmap(x=df['DAY'],y=df['LST_TIME'],
                    z=df['T_HR_AVG'].values.tolist(),
                    colorscale='Jet')]
layout = go.Layout(title='SB CA Temperature')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
