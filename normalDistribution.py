# IMPORT LIBRARIES
import csv 
import plotly.figure_factory as ff
import pandas as pd

# READ THE CSV FILE
df = pd.read_csv('data.csv')

# CREATE THE GRAPH AND PLOT IT
fig = ff.create_distplot([df["Avg Rating"]],["MOBILE BRAND AVG RATING"],show_hist=False)
fig.show()