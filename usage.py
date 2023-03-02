import dash
from dash.dependencies import Input, Output
from dash import html
import dash_pivottable


from .data import df, df_with_dummies

app = dash.Dash(__name__)
app.title = "Useful Skills"

app.layout = html.Div([
    dash_pivottable.PivotTable(
    id='table',
    data=df,
    rows=['role'],
    rowOrder="key_a_to_z",
    rendererName=

    )
])