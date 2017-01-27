# import pandas module
import pandas as pd

# import Scatter, out_file, and save
from bokeh.charts import Scatter, output_file, save

# name "temp" as the results from the csv file
temp = pd.read_csv('dataproject2.csv')

# create scatterplot
s= Scatter(temp, title= 'Temperatures on Christmas')
output_file('Scatterplot.html') 

# save plot
save(s)