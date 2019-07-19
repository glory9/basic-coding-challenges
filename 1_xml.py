#This code prompts the user for a URL, extracts an XML file from the given address, parses the file using a python library, and prints out...
#...the sum of all 'count' values in the file

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
exp = tree.findall('comments/comment')
#test link: http://py4e-data.dr-chuck.net/comments_175325.xml
x = 0
for item in exp:
    roo = int(item.find('count').text)
    x = x + roo
print('Total Sum is', x)
