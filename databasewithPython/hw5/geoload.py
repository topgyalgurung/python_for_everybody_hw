'''edit where.data to add an address nearby where you live
run the geoload.py to lookup all of the entries in where.data (including the new one) and produce the geodata.sqlite
run geodump.py to read the database and produce where.js
open where.html to visualize the map
'''

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import sys
import ssl 

api_key=False

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
# If you have a Google Places API key, enter it here
else:
    api_key='AIzaSyAUIjnGJ8Ro4cYePWBUaPA6c4I2YWNKxD8'
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn=sqlite3.connect('geodata.sqlite')
cur=conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh=open("where.data")
count=0
for line in fh:
    if count>20:
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address=line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")