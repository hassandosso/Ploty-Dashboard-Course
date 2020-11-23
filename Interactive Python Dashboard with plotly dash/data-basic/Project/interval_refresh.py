import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
            html.H1(id='Live-update-text'),
            dcc.Interval(id='interval-component',
                         interval=2000,
                         n_intervals=0)
])

@app.callback(Output('Live-update-text','children'),
              [Input('interval-component','n_intervals')])
def update_layout(n):
    return html.H1('Cash free for {} refresh'.format(n))

# if __name__ == '__main__':
#     app.run_server(debug=True)
