import dash
import dash_html_components as html

app = dash.Dash()

app.layout= html.Div(['parent Division',
                        html.Div(['This is inner division'],style={'color':'brown','backgroundColor':'black'}),
                        html.Div(['Another inner division'],style={'backgroundColor':'red','color':'white','border':'3px black solide'})],
style={'color':'green','textAlign':'center','border':'2px red solid'})

# if __name__=='__main__':
#     app.run_server(debug=True)
