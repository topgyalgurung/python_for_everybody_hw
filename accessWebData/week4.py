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

'''
The program will use urllib to read the HTML from the data files below, 
extract the href= vaues from the anchor tags, scan for a tag that is in a 
particular position relative to the first name in the list, follow that link and 
repeat the process a number of times and report the last name you find.
'''

url = input('Enter - ')
#url='http://py4e-data.dr-chuck.net/known_by_Hajirah.html'

# Retrieve all of the anchor tags
for i in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count=0
    for tag in tags:
        count=count+1

        if count>18:
            break
        url=tag.get('href', None)
        name=tag.contents[0]
        
print(name)
