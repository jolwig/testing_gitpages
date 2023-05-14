import plotly.express as px
import pandas as pd

df = pd.read_csv("Wine_RegionColor.csv")

#histogram for quality column
hist = px.histogram(df, x='quality')

hist.write_html("docs/histogram.html")

# CREATE BOX PLOT

quality_avgs_df = df.groupby(by=["quality"], as_index=False).mean()



