# import pandas module
import pandas as pd

# import Histogram, out_file, and save
from bokeh.charts import Histogram, output_file, save

# name "wind" as the results from the csv file
wind = pd.read_csv('dataproject3.csv')

# create histogram
h = Histogram(wind, title= "Wind Speeds")
output_file('Histogram.html')

# save histogram
save(h)