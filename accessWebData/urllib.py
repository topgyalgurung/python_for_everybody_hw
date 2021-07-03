# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=int(input('Enter count: '))
pos=int(input('Enter position: '))

# Retrieve all of the anchor tags

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')   
    tags = soup('a')
    count=0
    for tag in tags:
        count=count+1
        if count<pos:
            break
        url=tag.get('href', None)
        print(url)
        name=tag.contents[0]
        print(name)