#This piece of code prompts the user for a brisk/approx. description of a location and then prints out a genrated 'place_id' for that location...
#...using an API similiar to Google's geocoding API. The 'place_id' is contained python dictionary extracted from a json file
#recovered from the internet.
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address' : address, 'key' : 42})

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

result = json.loads(data)
print(result['results'][0]['place_id'])
