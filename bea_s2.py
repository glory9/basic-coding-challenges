#This code prompts the user for a URL, loops through links at that URL, extracts an HTML file, parses the file using the beautiful soup
# library, and prints out the value at a preset location in the file

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the library
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

for i in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    val, lav = [], []
    
    for tag in tags:
        lav.append(tag.contents[0])
        val.append(tag.get('href', None))
    url = val[17]
    
print(lav[17])
