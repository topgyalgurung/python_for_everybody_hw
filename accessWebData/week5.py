import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_1184333.xml'
print ("Retrieving", url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

results=tree.findall('comments/comment')
sum=0
for r in results:
    sum+=int(r.find('count').text)

print(sum)