import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
            html.Label('Dropdown'),
            dcc.Dropdown(options=[
                                {'label':'New York City','value':'NYC'},
                                {'label':'San Francisco','value':'SF'}
            ],value='SF'),
            html.Label('Silider'),
            dcc.Slider(min=-10,max=10,step=0.5,value=0,
                        marks={i:i for i in range(-10,11)}
                        ),
            html.P(html.Label('Some Radio Button')),
            dcc.RadioItems(options=[
                                {'label':'New York City','value':'NYC'},
                                {'label':'San Francisco','value':'SF'}
            ],value='SF')
])
# if __name__=='__main__':
#     app.run_server(debug=True)
