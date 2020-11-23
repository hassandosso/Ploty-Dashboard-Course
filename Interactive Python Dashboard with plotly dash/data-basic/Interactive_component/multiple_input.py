import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../plotting/Data/mpg.csv')

app = dash.Dash()

#LIST OF FEATURES
features = df.columns

app.layout = html.Div([
            html.Div([
                    dcc.Dropdown(
                        id='xaxis',
                        options=[{'label':i,'value':i} for i in features],
                        value='displacement'
                    )
            ],style={'width':'45%','display':'inline-block'}),
            html.Div([
                    dcc.Dropdown(
                        id='yaxis',
                        options=[{'label':i,'value':i} for i in features],
                        value='mpg'
                    )
            ],style={'width':'45%','display':'inline-block'}),
            dcc.Graph(id='features_graphic')
],style={'padding':'10px'})

@app.callback(Output('features_graphic','figure'),
            [Input('xaxis','value'),
            Input('yaxis','value')])

def update_graph(xaxis_name,yaxis_name):
    return {'data':[go.Scatter(x=df[xaxis_name],
                               y=df[yaxis_name],
                               mode='markers',
                               marker={'size':15,
                                       'opacity':0.7,
                                       'line':{'width':0.5,'color':'red'}
                                       }
                              )
                    ]
    ,'layout':go.Layout(title='Dashboard for MPG',
                        xaxis={'title':xaxis_name},
                        yaxis={'title':yaxis_name},
                        hovermode='closest'
                        )
        }

# if __name__=='__main__':
#     app.run_server(debug=True)
