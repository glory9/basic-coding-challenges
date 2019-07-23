import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
#test url - http://py4e-data.dr-chuck.net/comments_175326.json
jjj = urllib.request.urlopen(url, context=ctx).read()
fi = json.loads(jjj)
x = 0
for le in fi['comments']:
    s = int((le['count']))
    x = x + s
print('Sum is', x)
