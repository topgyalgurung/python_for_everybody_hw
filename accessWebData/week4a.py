# Scraping HTML Data with BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

'''
The program will use urllib to read the HTML from the data files below, and
 parse the data, extracting numbers and compute the sum of the numbers in the file.
'''

url='http://py4e-data.dr-chuck.net/comments_1184331.html'
html=urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,"html.parser")

tags=soup('span')
sum=0

for tag in tags:
    sum+=int(tag.contents[0])

print(sum) 

