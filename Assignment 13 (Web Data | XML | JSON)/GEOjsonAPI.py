import urllib.request, urllib.parse, urllib.error
import json
#Might ask for API Keys
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)


# Example Response for the input: Vedayapalem, Nellore
#
# {
#    "results" : [
#       {
#          "address_components" : [
#             {
#                "long_name" : "Vedayapalem",
#                "short_name" : "Vedayapalem",
#                "types" : [ "political", "sublocality", "sublocality_level_1" ]
#             },
#             {
#                "long_name" : "Nellore",
#                "short_name" : "NLR",
#                "types" : [ "locality", "political" ]
#             },
#             {
#                "long_name" : "Nellore",
#                "short_name" : "Nellore",
#                "types" : [ "administrative_area_level_2", "political" ]
#             },
#             {
#                "long_name" : "Andhra Pradesh",
#                "short_name" : "AP",
#                "types" : [ "administrative_area_level_1", "political" ]
#             },
#             {
#                "long_name" : "India",
#                "short_name" : "IN",
#                "types" : [ "country", "political" ]
#             },
#             {
#                "long_name" : "524004",
#                "short_name" : "524004",
#                "types" : [ "postal_code" ]
#             }
#          ],
#          "formatted_address" : "Vedayapalem, Nellore, Andhra Pradesh 524004, India",
#          "geometry" : {
#             "bounds" : {
#                "northeast" : {
#                   "lat" : 14.4223969,
#                   "lng" : 79.964902
#                },
#                "southwest" : {
#                   "lat" : 14.401513,
#                   "lng" : 79.95167409999999
#                }
#             },
#             "location" : {
#                "lat" : 14.4105632,
#                "lng" : 79.95825769999999
#             },
#             "location_type" : "APPROXIMATE",
#             "viewport" : {
#                "northeast" : {
#                   "lat" : 14.4223969,
#                   "lng" : 79.964902
#                },
#                "southwest" : {
#                   "lat" : 14.401513,
#                   "lng" : 79.95167409999999
#                }
#             }
#          },
#          "place_id" : "ChIJ1WqRVeDyTDoR2orjIa9z2wA",
#          "types" : [ "political", "sublocality", "sublocality_level_1" ]
#       }
#    ],
#    "status" : "OK"
# }
