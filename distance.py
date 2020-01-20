#!/usr/local/bin/python3
import geopy
import json
import requests
import geopy.distance
key = 'AIzaSyDTQN6reKANgO5y3pgtK-vxO_bLDYm1ojk'
add1 = input("Startpunkt :")
add2 = input("Zielpunkt :")
# Geocoordinaten holen (geopy Modul) (nutzt intern die Google Maps Geocoding API)
gc = geopy.geocoders.GoogleV3(api_key = key)
add1coords = gc.geocode(add1)
add2coords = gc.geocode(add2)
print(add1coords.address + ': ' + str(add1coords.latitude) + ', ' + str(add1coords.longitude))
print(add2coords.address + ': ' + str(add2coords.latitude) + ', ' + str(add2coords.longitude))
# Die Luftdistanz mithilfe der Vincenty Formel und dem Koordinaten Format WGS84 in Meter holen (geopy Modul)
point1 = (add1coords.latitude, add1coords.longitude)
point2 = (add2coords.latitude, add2coords.longitude)
entfernung = round(geopy.distance.vincenty(point1, point2).km, 3)
print ('Luftlinie : ' + str(entfernung) + 'km')
# Wie lange dauert es mit dem Auto? Die Google Maps Distance API hilft
coords1 = str(add1coords.latitude) + ',' + str(add1coords.longitude)
coords2 = str(add2coords.latitude) + ',' + str(add2coords.longitude)
type = 'driving'
targeturl = 'https://maps.googleapis.com/maps/api/distancematrix/json?key=' + key + '&origins=' + coords1 + '&destinations=' + coords2 + '&mode=' + type
mydata = requests.get(targeturl)
erg = json.loads(mydata.text)
print('Mit dem Auto ' + str(erg['rows'][0]['elements'][0]['distance']['text']) + ': ' + str(erg['rows'][0]['elements'][0]['duration']['text']))
type = 'bicycling'
targeturl = 'https://maps.googleapis.com/maps/api/distancematrix/json?key=' + key + '&origins=' + coords1 + '&destinations=' + coords2 + '&mode=' + type
mydata = requests.get(targeturl)
erg = json.loads(mydata.text)
print('Mit dem Rad ' + str(erg['rows'][0]['elements'][0]['distance']['text']) + ': ' + str(erg['rows'][0]['elements'][0]['duration']['text']))