import urllib2
y = raw_input("dwse to gewgrafiko platos(apo -90 ews 90): ")
x = raw_input("dwse to gewgrafiko mikos(apo -180 ews 180: ")
dedomena = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?lat="+y+"&lon="+x+"&appid=44db6a862fba0b067b1930da0d769e98")
html = dedomena.read()
data = html.strip()
data = html.split(",")
data1 = str(data[7])  
temperature = data1.split(":")
if (temperature[2]) > "293.15" : print "nice..." 	#293.15 kelvin isountai me 20 bathmous kelsiou#
if (temperature[2]) < "278.15" : print "brr..." 	#278.15 kelvin isountai me 5 bathmous kelsiou#
rain = str(data[3]) 
rain = rain.split(":") 
if rain[1]=="\"Rain\"" : print "im singing in the rain!"
		
	





