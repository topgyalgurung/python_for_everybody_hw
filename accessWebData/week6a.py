'''
Extracting data from Json
'''

import urllib.request,urllib.response,urllib.error
from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

'''The program will prompt for a URL, 
read the JSON data from that URL using urllib and 
then parse and extract the comment counts from the JSON data, 
compute the sum of the numbers in the file 

'''

url = input('Enter - ')
data = urlopen(url, context=ctx).read()

info=json.loads(data)
print('Retrieved', len(data), 'characters')

count=0
for item in info['comments']:
    count+=item['count']

print(count)
