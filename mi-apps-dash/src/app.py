from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='¡Hola, Dash!'),

    html.Div(children='''
        Esta es una aplicación de ejemplo utilizando Dash.
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)