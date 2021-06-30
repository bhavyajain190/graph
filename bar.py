import pandas as pd
import plotly_express  as px
df = pd.read_csv("coviddata.csv")
fig = px.bar(df,x = "date",y = "cases")
fig.show()

