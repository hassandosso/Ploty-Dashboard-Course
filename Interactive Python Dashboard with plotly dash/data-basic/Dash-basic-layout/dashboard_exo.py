import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

#Create data
df = pd.read_csv('../plotting/Data/OldFaithful.csv')

app.layout= html.Div([dcc.Graph(id='Old_Faithful',
                                figure={'data':[
                                        go.Scatter(x=df['X'],y=df['Y'],mode='markers')
                                        ],
                                        'layout':go.Layout(title='Old Faithful eruption interval vs Duration',
                                                            xaxis={'title':'duration in minute'},
                                                            yaxis={'title':'Intervals in minute'})
                                        }
                                )
])

# if __name__=='__main__':
#     app.run_server(debug=True)
