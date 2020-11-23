import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

cash_free = 0
def refresh_layout():
    global cash_free
    cash_free +=1
    return html.H1('Cash free for {} refresh'.format(cash_free))

app.layout = refresh_layout


# if __name__ == '__main__':
#      app.run_server(debug=True)
