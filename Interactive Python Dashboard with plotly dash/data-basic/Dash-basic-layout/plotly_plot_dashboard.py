import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

#Create data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app.layout= html.Div([dcc.Graph(id='scatterPlot',
                                figure={'data':[
                                        go.Scatter(x=random_x,y=random_y,mode='markers',
                                                    marker={'size':12,
                                                            'color':'rgb(51,204,153)',
                                                            'symbol':'pentagon',
                                                            'line':{'width':2}
                                                            }
                                                    )
                                ],
                                        'layout':go.Layout(title='My Scatter Plot',
                                                            xaxis={'title':'X title'})}
                                ),
                dcc.Graph(id='scatterPlot2',
                                                figure={'data':[
                                                        go.Scatter(x=random_x,y=random_y,mode='markers',
                                                                    marker={'size':12,
                                                                            'color':'rgb(51,100,142)',
                                                                            'symbol':'circle',
                                                                            'line':{'width':2}
                                                                            }
                                                                    )
                                                ],
                                                        'layout':go.Layout(title='My Scatter Plot',
                                                                            xaxis={'title':'X title'})}
                                                )
])

# if __name__=='__main__':
#     app.run_server(debug=True)
