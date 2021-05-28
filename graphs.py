import csv
import pandas as pd
from pandas.tseries.offsets import Day
import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.scatter(df,x="date",y="cases",color="country")
fig.show()
