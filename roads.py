import requests
api = "https://roads.googleapis.com/v1/nearestRoads?"
key="AIzaSyBB4vzhrmhO8Xj1rlvYLwYWPBW4-ftKZjA"

print('Please enter origin street coordinates(lat):')
l1 = str(input())
l11 = l1.replace(" ","%")
print('Please enter origin street coordinates(long):')
l2 = str(input())
l22 = l2.replace(" ","%")
print('Please enter destination street coordinates(lat):')
l3 = str(input())
l33 = l3.replace(" ","%")
print('Please enter destination street coordinates(long):')
l4 = str(input())
l44 = l4.replace(" ","%")
url = api + "origin=" + l11 + "%" + l22 + "&destination=" + "%" + l33 + "%" + l44+ "&key=" + key

print(url)
