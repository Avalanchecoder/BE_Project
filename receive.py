import urllib.request as urllib2
import json
f = urllib2.urlopen("https://api.thingspeak.com/channels/810361/feeds.json?api_key=14N1BTAJPTEFBA95&results=2")
response = f.read()
data=json.loads(response)
y = json.dumps(data)
field1 = data["feeds"][-1]["field1"]
field2 = data["feeds"][-1]["field2"]
field3 = data["feeds"][-1]["field3"]
field1=int(field1)
if field1== 1 :
    print("Inoformation recived")

print(field1)
print(field2)
print(field3)