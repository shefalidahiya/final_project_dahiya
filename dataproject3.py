# What has the wind speed been like on Christmas in NYC from 2000-2015?
# import csv and request modules
import csv
import requests

# set up URL for request
endpoint = 'https://api.darksky.net/forecast/'
api_key = 'da5d52438b53e27259e8e2bdc2f7c51f'
lat = '40.7128'
lon= '-73.9352'

# open file in write mode
csvfile= open('dataproject3.csv', 'w')

# create the csv writer
csvwriter= csv.writer(csvfile, delimiter= ',')
csvwriter.writerow(['year', 'wind'])

# create for loop
for y in range(2000,2015):
    time = '%d-12-25T12:00:00' % y
    
    # url for request
    url = endpoint + api_key + '/' + lat + ',' + lon + ',' + time
    
    # make request
    r = requests.get(url)
    # convert to json
    weather = r.json()
    # accessing data
    temp = weather['daily']['data'][0]['windSpeed']
    print(temp)
    csvwriter.writerow([y, temp])

# close csv file
csvfile.close()