import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Salary_Data.csv')
exp = df['YearsExperience']
salary = df['Salary']
np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=salary,
                    y=exp,
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(51,204,153)',
                        symbol = 'pentagon',
                        line= {'width':2}
                    ))]

layout = go.Layout(title='Salary distribution',
xaxis ={'title':'Salary'},
yaxis = dict(title='Year of Experience'),
hovermode = 'closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='scatter.html')