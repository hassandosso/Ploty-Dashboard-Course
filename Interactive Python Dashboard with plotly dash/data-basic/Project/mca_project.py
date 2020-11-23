import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
import dash_auth

USERNAME_PASSWORD_PAIRS = [['username','password'],['hassan','12345678']]

app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server

df = pd.read_csv('Data/HR_comma_sep.csv')
#print(df.head())
# GET UNIQUE DEPARTMENT FROM DATASET
options = []
for dept in df['sales'].unique():
    mydict = {}
    mydict['label'] = dept
    mydict['value'] = dept
    options.append(mydict)

# GET PERFORMENCE CRITERIA
criterias = []
for crt in df.columns[:5]:
    mydict = {}
    mydict['label'] = crt
    mydict['value'] = crt
    criterias.append(mydict)

app.layout = html.Div([
            html.H1('Employees Performence Dashboard by department',style={'textAlign':'center'}),
            html.Div([
                html.H3('Select Departments',style={'paddingRight':'30px'}),
                dcc.Dropdown(id='department',
                             options=options,
                             value=['sales'],
                             multi=True)
            ],style={'display':'inline-block','verticalAlign':'top','width':'30%'}),

            html.Div([
                    html.H3('Select Criteria:',style={'paddingRight':'30px'}),
                    dcc.Dropdown(id='criteria',
                                 options=criterias,
                                 value='satisfaction_level')
            ],style={'display':'inline-block'}),

            html.Div([
                    html.Button(id='submit-btn',
                                n_clicks=0,
                                children='submit',
                                style={'fontSize':24,'marginLeft':'30px'})
            ],style={'display':'inline-block'}),

            dcc.Graph(id='my-graph'),

            html.Div([
                    html.H2('BarPlot Dashboard for salary classes')
            ])

])




@app.callback(Output('my-graph','figure'),
              [Input('submit-btn', 'n_clicks')],
              [State('department', 'value'),
              State('criteria','value')])
def graph(n_click,department,criteria):
    traces = []
    for i in department:
        data = pd.DataFrame(df[df['sales']==i][criteria]).reset_index()
        data = data.drop(columns=['index'])
        traces.append({'x':data.index[:30],'y':data[criteria],'name':i})
    figure = {
            'data':traces,
            'layout':{'title':criteria}
    }
    print(data.index)
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
