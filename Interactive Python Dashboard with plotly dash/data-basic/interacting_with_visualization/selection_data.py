import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64

app = dash.Dash()

df = pd.read_csv('../plotting/Data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
                    html.Div(
                            dcc.Graph(id='wheels_plot',
                                        figure={
                                                'data':[go.Scatter(x=df['color'],
                                                                   y=df['wheels'],
                                                                   dy=1,
                                                                   mode='markers',
                                                                   marker={'size':15}
                                                                   )
                                                        ],
                                                'layout':go.Layout(title='Test',hovermode='closest')
                                                }
                                        ),style={'width':'30%','float':'left'}
                    ),
                    html.Div([
                                html.Pre(id='selection',style={'paddingTop':25})
                            ],style={'width':'30%','display':'inline-block','verticalAlign':'top'})
])

@app.callback(Output('selection','children'),
              [Input('wheels_plot','selectedData')])
              #selectedData, clickData, hoverData: properties of dcc.Graph
def callback_image(Data):
    return json.dumps(Data,indent=2)

# if __name__=='__main__':
#     app.run_server(debug=True)
