import requests
api = "https://maps.googleapis.com/maps/api/directions/json?"
key="AIzaSyBB4vzhrmhO8Xj1rlvYLwYWPBW4-ftKZjA"

print('Please enter origin street address:')
o = str(input())
origin = o.replace(" ","%")
print('Please enter destination street address:')
f = str(input())
destination = f.replace(" ","%")
url = api + "origin=" + origin + "&destination=" + destination + "&key=" + key

r = requests.get(url)
#d = r.json()["rows"][0]["elements"][0]["distance"]["text"]
#t = r.json()["rows"][0]["elements"][0]["duration"]["text"]
#print(f"The distance between your origin and destination is "+d)
#print(f"Travel duration will be "+t)
rout = r.json()["routes"][0]['legs'][0]['distance']['text']
time = r.json()["routes"][0]['legs'][0]['duration']['text']
print(rout)
print(time)
print(url)