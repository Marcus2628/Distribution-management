import requests
api = "https://routes.googleapis.com/directions/v2:computeRoutes?"
key="AIzaSyBB4vzhrmhO8Xj1rlvYLwYWPBW4-ftKZjA"

print('Please enter origin street address:')
o = str(input())
origins = o.replace(" ","%")
print('Please enter destination street address:')
d= str(input())
destinations = d.replace(" ","%")
url = api + "origins=" + origins + "&destinations=" + destinations + "&key=" + key

print(url)