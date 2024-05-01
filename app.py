# **********************************  Connecting to Data  **********************************

# Import packages
# from dash import Dash, html, dash_table
# import pandas as pd

# Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# df = pd.read_csv('Batch_Simulation.csv')

# Initialize the app
# app = Dash(__name__)

# App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10)
# ])

# Run the app
# if __name__ == '__main__':
#     app.run(debug=True)


# **********************************  Visualizing Data  **********************************

# Import packages
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# app = Dash(__name__)

# app.layout = html.Div([
#     html.Div(children='My First App with Data, Graph, and Controls'),
#     html.Hr(),
#     dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=6),
#     dcc.Graph(figure={}, id='controls-and-graph')
# ])

# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#     return fig

# if __name__ == '__main__':
#     app.run(debug=True)


# **********************************  HTML and CSS  **********************************


# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app - incorporate css
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = ['aleph.css']
# app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
# app.layout = html.Div([
#     html.Div(className='row', children='My First App with Data, Graph, and Controls',
#              style={'textAlign': 'center', 'color': 'black', 'fontSize': 30,'fontWeight':'bold'}),

#     html.Div(className='row', children=[
#         dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
#                        value='lifeExp',
#                        inline=True,
#                        id='my-radio-buttons-final')
#     ]),

#     html.Div(className='row', children=[
#         html.Div(className='six columns', children=[
#             dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
#         ]),
#         html.Div(className='six columns', children=[
#             dcc.Graph(figure={}, id='histo-chart-final')
#         ])
#     ])
# ])

# Add controls to build the interaction
# @callback(
#     Output(component_id='histo-chart-final', component_property='figure'),
#     Input(component_id='my-radio-buttons-final', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#     return fig

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)


# **********************************    Dash Design Kit (DDK)  **********************************


# Import packages
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px
# import dash_bootstrap_components as dbc

# # Incorporate data
# # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# df = pd.read_csv('Batch_simulation.csv')

# # Initialize the app - incorporate a Dash Bootstrap theme
# external_stylesheets = [dbc.themes.CERULEAN]
# app = Dash(__name__, external_stylesheets=external_stylesheets)

# # App layout
# app.layout = dbc.Container([
#     dbc.Row([
#         html.Div('Aleph Chemical Plant', className="heading text-center fs-3")
#     ]),

#     dbc.Row([
#         dbc.RadioItems(options=[{"label": x, "value": x} for x in ['Electricity','Water']],
#                        value='Electricity',
#                        inline=True,
#                        id='radio-buttons-final',
#                        className="radioBtn")
#     ]),

#     dbc.Row([
#         dbc.Col([
#             dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
#         ], width=6,className='data-table'),

#         dbc.Col([
#             dcc.Graph(figure={}, id='my-first-graph-final')
#         ], width=6),
#     ]),

# ], fluid=True)

# # Add controls to build the interaction
# @callback(
#     Output(component_id='my-first-graph-final', component_property='figure'),
#     Input(component_id='radio-buttons-final', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='Month', y=col_chosen, histfunc='avg')
#     return fig

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)


# **********************************    Aleph Dashboard    **********************************


import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.graph_objs as go

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# # Create sample data for the chart
x_data = ["Jan", "Feb", "Mar", "Apr", "May", "June"]
x_values = [1, 1, 2, 2, 3, 3, 4, 4]
y_data = [10, 20, 15, 25, 30, 45]
y_data2 = [20, 50, 15, 25, 60, 45]
colors = ["blue", "green", "red", "purple", "orange", "yellow", "gray"]
group_labels = [
    "Group 1",
    "Group 1",
    "Group 2",
    "Group 2",
    "Group 3",
    "Group 3",
    "Group 4",
    "Group 4",
]

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "rgb(21 25 120)",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "16rem",
}

sidebar = html.Div(
    [
        html.Img(src="/assets/images/aleph_logo.png", className="sidebar-logo"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("Operations", href="/page-1", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(
            # main div element
            className="main",
            children=[
                html.Div(
                    className="navbar",
                    children=[
                        html.H2("Godrej Plant Dashboard"),
                    ],
                ),
                # all chart shows here
                html.Div(
                    className="charts",
                    children=[
                        # Pie chart
                        html.Div(
                            className="chart",
                            children=[
                                html.H2("Electricity Usage 2023"),
                                dcc.Graph(
                                    id="example-graph",
                                    figure={
                                        "data": [go.Pie(labels=x_data, values=y_data)],
                                        "layout": go.Layout(title="Pie Chart"),
                                    },
                                ),
                            ],
                        ),
                        # Scatter graph
                        html.Div(
                            className="chart",
                            children=[
                                html.H2("Electricity Usage 2023"),
                                dcc.Graph(
                                    id="example-graph",
                                    figure={
                                        "data": [
                                            go.Scatter(
                                                x=x_data,
                                                y=y_data,
                                                mode="markers",
                                                marker=dict(
                                                    color=colors,
                                                    size=12,
                                                    showscale=True,
                                                ),
                                            )
                                        ],
                                        "layout": go.Layout(
                                            title="Scatter Plot with Color",
                                            xaxis=dict(title="X-axis"),
                                            yaxis=dict(title="Y-axis"),
                                        ),
                                    },
                                ),
                            ],
                        ),
                        # Stacked histogram
                        html.Div(
                            className="chart",
                            children=[
                                html.H2("Electricity Usage 2023"),
                                dcc.Graph(
                                    id="example-graph",
                                    figure={
                                        "data": [
                                            go.Histogram(
                                                x=x_values,
                                                marker=dict(color=colors),
                                                name=group,
                                                opacity=0.75,
                                                showlegend=True if i == 0 else False,
                                            )
                                            for i, group in enumerate(set(group_labels))
                                        ],
                                        "layout": go.Layout(
                                            title="Stacked Histogram",
                                            xaxis=dict(title="X-axis"),
                                            yaxis=dict(title="Frequency"),
                                            barmode="stack",
                                        ),
                                    },
                                ),
                            ],
                        ),
                        # Bar chart
                        html.Div(
                            className="chart",
                            children=[
                                html.H2("Electricity Usage 2023"),
                                dcc.Graph(
                                    id="example-graph",
                                    figure={
                                        "data": [
                                            {
                                                "x": x_data,
                                                "y": y_data,
                                                "type": "bar",
                                                "name": "Data",
                                            }
                                        ],
                                        "layout": {"title": "2023"},
                                    },
                                ),
                            ],
                        ),
                        # stcked bar chart
                        html.Div(
                            className="chart",
                            children=[
                                html.H2("Carbon Emmission"),
                                dcc.Graph(
                                    id="example-graph",
                                    figure={
                                        "data": [
                                            go.Bar(x=x_data, y=y_data, name="Value 1"),
                                            go.Bar(x=x_data, y=y_data2, name="Value 2"),
                                        ],
                                        "layout": go.Layout(
                                            title="Stacked Bar Chart", barmode="stack"
                                        ),
                                    },
                                ),
                            ],
                        ),
                        # Line chart
                        html.Div(
                            className="chart",
                            children=[
                                html.H2("Electricity Usage 2023"),
                                dcc.Graph(
                                    id="example-graph",
                                    figure={
                                        "data": [
                                            {
                                                "x": x_data,
                                                "y": y_data,
                                                "type": "line",
                                                "name": "Data",
                                            }
                                        ],
                                        "layout": {"title": "2023"},
                                    },
                                ),
                            ],
                        ),
                        # Stcked line chart
                        html.Div(
                            className="chart",
                            children=[
                                html.H2("Carbon Emmission"),
                                dcc.Graph(
                                    id="example-graph",
                                    figure={
                                        "data": [
                                            go.Scatter(
                                                x=x_data,
                                                y=y_data,
                                                mode="lines",
                                                name="Value 1",
                                                fill="tozeroy",
                                            ),
                                            go.Scatter(
                                                x=x_data,
                                                y=y_data2,
                                                mode="lines",
                                                name="Value 2",
                                                fill="tonexty",
                                            ),
                                        ],
                                        "layout": go.Layout(
                                            title="Stacked Line Chart", barmode="stack"
                                        ),
                                    },
                                ),
                            ],
                        ),
                    ],
                    style={"padding": "20px"},
                ),
            ],
        )
    elif pathname == "/page-1":
        return html.H1("Oh cool, this is page 2!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8888)


# *********************************************************************************
# *********************************************************************************


# import dash
# import dash_html_components as html
# import dash_core_components as dcc
# import dash_bootstrap_components as dbc
# import plotly.graph_objs as go

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Create sample data for the chart
# x_data = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# y_data = [10, 20, 15, 25, 30]


# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# # the style arguments for the sidebar. We use position:fixed and a fixed width
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }

# # the styles for the main content position it to the right of the sidebar and
# # add some padding.
# CONTENT_STYLE = {
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
# }


# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "A simple sidebar layout with navigation links", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Dashboard", href="/", active="exact"),
#                 dbc.NavLink("Operations", href="/page-1", active="exact")
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )


# # Define the layout of the app
# app.layout = html.Div(
#     # main div element
#     className="main",
#     children=[
#         html.Div(
#             className="navbar",
#             children=[
#              html.H2("Godrej Plant Dashboard"),
#             ]
#         ),
#         # all chart shows here
#         html.Div(
#              className="charts",
#             children=[
#                 # //bar chart
#                 html.Div(
#                     className="chart",
#                     children=[
#                         html.H2("Electricity Usage 2023"),
#                         dcc.Graph(
#                             id='example-graph',
#                             figure={
#                                 'data': [
#                                     {'x': x_data, 'y': y_data, 'type': 'bar', 'name': 'Data'}
#                                 ],
#                                 'layout': {
#                                     'title': '2023'
#                                 }
#                             }
#                         )
#                     ],
#                 ),
#                 # Line chart
#                 html.Div(
#                     className="chart",
#                     children=[
#                         html.H2("Carbon Emmission"),
#                         dcc.Graph(
#                             id='example-graph',
#                             figure={
#                                 'data': [
#                                     {'x': x_data, 'y': y_data, 'type': 'line', 'name': 'Data'}
#                                 ],
#                                 'layout': {
#                                     'title': '2023'
#                                 }
#                             }
#                         )
#                     ],
#                 )
#             ],
#             style={'border': '2px solid green', 'padding': '20px'}
#         )
#     ],
# )

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)
