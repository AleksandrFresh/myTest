import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': input(str('Enter the start_time yyyy-mm-dd: ')),
    'endtime': input(str('Enter the end_time yyyy-mm-dd: ')),
    'latitude': input(str('Enter the latitude: ')),
    'longitude': input(str('Enter the longitude: ')),
    'maxradiuskm': input(str('Enter the max_radius_km: ')),
    'minmagnitude': input(str('Enter the min_magnitude: '))

})

data = response.json()
num = 1
for i in data['features']:
    try:
        print(str(num) + '.' + ' Place: ' + i['properties']['place']
              + '.', 'Magnitude: ' + str(i['properties']['mag']))
    except TypeError:
        print(str(num) + '.' + ' ' + 'Unspecified location')
    num += 1
