import dash
import dash_bootstrap_components as dbc
from dash import dcc,Input,Output
import plotly.express as px
import pandas as pd

# Loading Data 
def load_data():
    pass
    # df=pd.read_csv("assets/healthcare.csv")
    # data["Billing Amount"]=pd.to_numeric(data["Billing Amount"],errors='coerce')
    # data["Data of Admission"]=pd.to_datetime(data["Data of Admission"])
    # data["YearMonth"]=data["Data of Admission"].dt.to_period("M")
    # return data

data=load_data()
# creating a Web App
app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout and Design
app.layout=dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Healthcare Dashboard"),width=15,className="text-center my-5")
    ])
])

if __name__=="__main__":
    app.run_server(debug=True)