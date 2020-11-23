import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Data/mocksurvey.txt',sep=',',index_col=0)
#print(df.index)

#data =[go.Bar(x=df.index, y=df[response],
                #name=response) for response in df.columns]

# horizontal bar
data = [go.Bar(x=df[response],y=df.index,name=response,orientation='h') for response in df.columns]

layout = go.Layout(title='Mock survey',barmode='stack')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)