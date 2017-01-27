# What has the  temp been like on Christmas in NYC from 2000-2015?
# import csv and request modules
import csv
import requests

# set up URL for request
endpoint = 'https://api.darksky.net/forecast/'
api_key = 'da5d52438b53e27259e8e2bdc2f7c51f'
lat = '40.7128'
lon= '-73.9352'

# open file in write mode
csvfile= open('dataproject2.csv', 'w')

# create the csv writer
csvwriter= csv.writer(csvfile, delimiter= ',')
csvwriter.writerow(['year', 'temp'])

for y in range(2000,2015):
    time = '%d-12-25T12:00:00' % y
    
    # url for request
    url = endpoint + api_key + '/' + lat + ',' + lon + ',' + time
    
    # make request
    r = requests.get(url)
    weather = r.json()
    temp = weather['hourly']['data'][0]['temperature']
    print(temp)
    csvwriter.writerow([y, temp])
    
csvfile.close()
