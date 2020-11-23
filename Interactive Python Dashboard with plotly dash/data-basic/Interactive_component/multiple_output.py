import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd
import base64

df = pd.read_csv('../plotting/Data/wheels.csv')

app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return '../plotting/Data:Images/jpg;base64,{}'.format(encoded.decode())

app.layout = html.Div([
            dcc.RadioItems(id='wheels',
                            options=[{'label':i,'value':i} for i in df['wheels'].unique()],
                            value=1),
            html.Div(id='wheels_output'),
            html.Hr(),
            dcc.RadioItems(id='colors',
                            options=[{'label':i,'value':i} for i in df['color'].unique()],
                            value='blue'),
            html.Div(id='colors_output'),
            html.Img(id='display-image',src='children',height=300)
],style={'fontFamily':'helvetica','fontSize':18})

@app.callback(Output('wheels_output','children'),
             [Input('wheels','value')])
def callback_a(wheel_value):
    return "You choose {}".format(wheel_value)

@app.callback(Output('colors_output','children'),
               [Input('colors','value')])
def callback_b(color_value):
    return "You choose {}".format(color_value)

@app.callback(Output('display-image','src'),
              [Input('wheels','value'),
              Input('colors','value')])
def callback_image(wheel,color):
    path = '../plotting/Data/Images'
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'])

# if __name__=='__main__':
#     app.run_server(debug=True)
