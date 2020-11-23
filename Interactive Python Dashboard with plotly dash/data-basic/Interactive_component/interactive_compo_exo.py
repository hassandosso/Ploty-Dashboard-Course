import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
                        html.Label('Slider'),
                        dcc.RangeSlider(id='slider',
                                    min=-6,
                                    max=6,
                                    step=1,
                                    value=[-1,1],
                                    marks={i:i for i in range(-5,7)}
                                    ),
                        html.H1(id='slider_result',style={'textAlign':'Center','marginTop':'25px'})
])

@app.callback(Output('slider_result','children'),
                [Input('slider','value')])
def slider_result(slider_value):
    return slider_value[0]*slider_value[1]

# if __name__=='__main__':
#     app.run_server(debug=True)
