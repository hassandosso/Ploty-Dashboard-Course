import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import os
import pandas as pd

nasdaq = pd.read_csv('Data/NASDAQcompanylist.csv')
nasdaq.set_index('Symbol',inplace=True)
options = []
for tic in nasdaq.index:
    mydict = {}
    mydict['label'] = str(nasdaq.loc[tic]['Name'])+' '+tic
    mydict['value'] = tic
    options.append(mydict)

# f = web.DataReader('TSLA', 'iex-tops')
# print(f[:10])
# IEX API TOKEN
iexKey = 'pk_bd5ea27dbf6e4cc49c47c076d2e40e7b'
iexKeySe= 'sk_2bcb5b3bb6b14c6b97fb4ecfab4e969a'
app = dash.Dash()

app.layout = html.Div([
                       html.H1('Stock Ticker Dashboard', style={'textAlign':'center'}),
                       html.Div([
                                html.H3('Enter a stock symbol:',style={'paddingRight':'30px'}),
                                dcc.Dropdown(id='my_stock_picker',
                                          options=options,
                                          value=['TSLA'],
                                          multi=True)
                       ],style={'display':'inline-block','verticalAlign':'top','width':'30%'}),

                       html.Div([
                                html.H3('Select a start and end date:'),
                                dcc.DatePickerRange(id='my_date_picker',
                                                     min_date_allowed=datetime(2015,1,1),
                                                     max_date_allowed=datetime.today(),
                                                     start_date=datetime(2018,1,1),
                                                     end_date=datetime.today())
                       ],style={'display':'inline-block'}),
                        html.Div([
                                html.Button(id='submit_btn',
                                            n_clicks=0,
                                            children='submit',
                                            style={'fontSize':24,'marginLeft':'30px'})
                        ],style={'display':'inline-block'}),
                        dcc.Graph(id='my_graph',
                                  figure={
                                          'data':[
                                                {'x':[1,2],'y':[3,1]}
                                          ],
                                          'layout':{'title':'Default title'}

                                  }
                                 )
])

@app.callback(Output('my_graph','figure'),
              [Input('submit_btn','n_clicks')],
              [State('my_stock_picker','value'),
               State('my_date_picker','start_date'),
               State('my_date_picker','end_date')])
def update_graph(n_clicks,stock_ticker,start_date,end_date):
    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end = datetime.strptime(end_date[:10],'%Y-%m-%d')
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic,'iex',start,end,api_key=iexKeySe)
        traces.append({'x':df.index,'y':df['close'],'name':tic})
    figure = {
            'data':traces,
            'layout':{'title':stock_ticker}
    }
    return figure


# if __name__=='__main__':
#     app.run_server(debug=True)
