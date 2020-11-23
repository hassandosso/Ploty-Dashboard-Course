import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Data/2010YumaAZ.txt')
#print(df.head())
days = df['DAY'].unique()
#print(days)

data = [go.Scatter(x=df['LST_TIME'],
                    y=df[df['DAY']==day]['T_HR_AVG'],
                    mode='lines',name=day) for day in days]
layout = go.Layout(title='Daily temperature')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)