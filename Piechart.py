# import pandas module
import pandas as pd

# import Donut, out_file, and save
from bokeh.charts import Donut, output_file, save

# name "icon" as the results from the csv file
icon = pd.read_csv('dataproject.csv')

# create pie chart
p = Donut(icon, label = "precipitation")
output_file('piechart.html') 

# save chart
save(p)