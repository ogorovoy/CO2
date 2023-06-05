import urllib.request
import json
import pandas as pd

#start_date= input('Enter start date: ')
#last_date= input('Enter last date: ')

print('Correct date FORMAT y-> YYYY,m->MM, d->DD')
y=input('Enter year: ')
m= input('Enter mounth : ')
start_d=input('Enter start day period: ')
end_d=input('Enter end day period: ')
check_date = (y+'-'+m+'-'+start_d+'T00:00Z', y+'-'+m+'-'+end_d + 'T00:00Z')
#check_date = (start_date+'T00:00Z', last_date + 'T00:00Z')

url = 'https://api.carbonintensity.org.uk/intensity/%s/%s'
url = url % check_date
print(url)

response = urllib.request.urlopen(url)
data = json.loads(response.read())['data']


qulity_co2 = pd.DataFrame()
qulity_co2['timestamp'] = [pd.to_datetime(d['from']) for d in data]
qulity_co2['intensity'] = [d['intensity']['actual'] for d in data]
qulity_co2['classification'] = [d['intensity']['index'] for d in data]
qulity_co2.set_index('timestamp', inplace=True)

result = qulity_co2.groupby(by='classification').min()



print(result)






