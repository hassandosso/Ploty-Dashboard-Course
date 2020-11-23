import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../plotting/Data/gapminderDataFiveYear.csv')
#print(df.head())
#print(df.columns)
app = dash.Dash()

year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})

app.layout = html.Div([
            html.Div([
                    dcc.Graph(id='graph')
            ],style={'width':'60%'}),
            html.Div([
                    dcc.Dropdown(id='year_picker',options=year_options,value=df['year'].min())
            ])
])

@app.callback(Output('graph','figure'),
                [Input('year_picker','value')])

def update_figure(selected_year):
    #DATA ONLY FOR SELECTED YEAR
    fileterd_df = df[df['year']==selected_year]

    # CREATE SCATTER PLOT FOR EACH CONTINENT OF SELECTED YEAR
    traces = []
    for continent in fileterd_df['continent'].unique():
        continent_df = fileterd_df[fileterd_df['continent']==continent]
        traces.append(go.Scatter(x=continent_df['gdpPercap'],y=continent_df['lifeExp'],
                        mode='markers',opacity=0.7,marker={'size':15},name=continent))

    return {'data':traces,'layout':go.Layout(title='GDP and Life expectancy',
                                            xaxis={'title':'GDP per Cap','type':'log'},
                                            yaxis={'title':'Life expectancy'})}

# if __name__=='__main__':
#     app.run_server(debug=True)
