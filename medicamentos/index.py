import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output



df = pd.read_csv('medicamentos\data\medicamentos.csv')
#Preparando la Data

df1 = df.drop(['principio_activo','factoresprecio','numerofactor'],axis=1)
df2 = df1.drop(df[df['nombre_comercial'] == 'Suspension De Hidroxido De Aluminio Y Magnesio + Simeticona'].index)
df3 = df.drop(df[df['cant_modificada'] >= 20].index)
df4 = df3.drop(df[df['cant_modificada'] <= 1].index)

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
        html.H1('Pharma.Pa'),
        html.Img(src='assets/medicamento.png'),
    ], className = 'banner'),

    html.Div([
        html.Div([
            html.P('Selecciona por que quieres filtar', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'medicamento-radio-item', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Nombre Del Producto', 'value' : 'nombre_producto'},
                                {'label' : 'Fabricante', 'value' : 'fabricante'}
                            ], value = 'nombre_producto',
                            style = {'text-aling':'center', 'color':'black'}, className = 'dcc_compon'),
        ], className = 'create_container2 five columns', style = {'margin-bottom': '20px'}),
    ], className = 'row flex-display'),

    html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),

        html.Div([
            dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'create_container2 five columns'),

        html.Div([
            dcc.Graph(id = 'my_grafico', figure = {})
        ], className = 'create_container3 eight columns')

    ], className = 'row flex-display'),


], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})


@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('medicamento-radio-item', component_property='value')])

def update_graph(value):

    if value == 'nombre_producto':
        fig = px.bar(
            data_frame = df4,
            x = 'nombre_comercial',
            y = 'cant_modificada')
    else:
        fig = px.bar(
            data_frame= df4,
            x = 'fabricante',
            y = 'cant_modificada')
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('medicamento-radio-item', component_property='value')])

def update_graph_pie(value):

    if value == 'nombre_producto':
        fig2 = px.pie(
            data_frame = df4,
            names = 'nombre_comercial',
            values = 'cant_modificada')
    else:
        fig2 = px.pie(
            data_frame = df4,
            names = 'fabricante',
            values = 'cant_modificada'
        )
    return fig2


@app.callback(
    Output('my_grafico', component_property='figure'),
    [Input('medicamento-radio-item', component_property='value')])

def update_graph(value):

    if value == 'nombre_producto':
        fig3 = px.bar(
            data_frame = df4,
            x = 'unidad_base',
            y = 'cant_modificada')
    else:
        fig3 = px.bar(
            data_frame= df4,
            x = 'unidad_base',
            y = 'can_modificada')
    return fig3


if __name__ == ('__main__'):
    app.run_server(debug=True)