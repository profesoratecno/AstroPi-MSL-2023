import pandas as pd
import plotly.express as px
import csv

data = pd.read_csv('datamap.csv', delimiter=';')
fig = px.scatter_geo(data, lat="Lat", lon="Lng", hover_name="id")

fig.show()


