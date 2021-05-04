# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:41:10 2021

@author: dimpl
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# data
np.random.seed(4)
Y = np.random.randint(low=-1, high=2, size=1).tolist()
X = np.random.randint(low=-1, high=2, size=1).tolist()
df = pd.DataFrame({"X": X, "Y": Y}, columns=["X", "Y"])
df.iloc[0] = 0

# plotly app
app = JupyterDash(__name__)
app.layout = html.Div(
    [
        html.H1("Random stumble"),
        dcc.Interval(id="interval-component", interval=1 * 100,),  # in milliseconds
        dcc.Graph(id="graph"),
    ]
)

# Define callback to update graph
@app.callback(Output("graph", "figure"), [Input("interval-component", "n_intervals")])
# def sum_int(self):
#     fig = go.Figure(data=go.Scatter(x=df["X"], y=df["Y"]))
#     fig.update_layout(
#         title=dict(text="x =" + str(X) + ", y =" + str(Y) + ", len = " + str(len(df)))
#     )
#     return fig


def streamFig1(value):

    global df

    Y = np.random.randint(low=-4, high=4, size=1).tolist()
    X = np.random.randint(low=-6, high=6, size=1).tolist()
    df2 = pd.DataFrame({"X": X, "Y": Y}, columns=["X", "Y"])
    df = df.append(df2, ignore_index=True)  # .reset_index()
    df3 = df.copy()
    df3 = df3.cumsum()
    fig = go.Figure(data=go.Scatter(x=df3["X"], y=df3["Y"]))
    fig.update_layout(
        title=dict(text="x =" + str(X) + ", y =" + str(Y) + ", len = " + str(len(df)))
    )
    # fig.update_layout(xaxis=dict(range=[-10, 10]))
    # fig.update_layout(yaxis=dict(range=[-10, 10]))
    return fig


app.run_server(
    mode="external",
    port=8017,
    dev_tools_ui=True,
    debug=True,
    dev_tools_hot_reload=True,
    threaded=False,
)
