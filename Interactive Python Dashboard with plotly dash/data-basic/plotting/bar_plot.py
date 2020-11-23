import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Data/HR_comma_sep.csv')
#print(df.head())
dept = pd.DataFrame(df.groupby('sales')['number_project'].sum())
#print(dept.index)
df2 = df[['sales','salary']]
df_salary = pd.get_dummies(df2,columns=['salary'])
#print(df_salary.head())
plot =pd.DataFrame(df_salary.groupby('sales')['salary_high','salary_medium','salary_low'].sum())

trace1 = go.Bar(x=plot.index, y=plot['salary_high'],
                name='High',marker={'color':'#191970'})

trace2 = go.Bar(x=plot.index,y=plot['salary_medium'],
                name='Medium',marker={'color':'#DAA520'})

trace3 = go.Bar(x=plot.index,y=plot['salary_low'],
                name='Low',marker={'color':'#FF0000'})

data= [trace1,trace2,trace3]
layout = go.Layout(title='Salary Classes Distribution',barmode='stack')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
