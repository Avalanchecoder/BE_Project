import urllib.request as urllib2
robot=1
x=10
y=20
f = urllib2.urlopen("https://api.thingspeak.com/update?api_key=KCZZLN4R5459ZABJ&field1="+str(robot)+"&field2="+str(x)+"&field3="+str(y))

