#!/usr/bin/python
#
# Richard Lopez
# Google Maps API
#
##################

import sys
from sys import argv
import os
import json
import requests

client = requests.Session()
client.verify = False
jsontype = {'content-type': 'application/json'}

# Process input string from STIN
# user_address_input = str(argv)

# Process input from User
user_address_input = raw_input('Enter US Mailing Address: ')

query_args = { 'address': user_address_input }
url="https://maps.googleapis.com/maps/api/geocode/json"

client = requests.Session()
response = client.get(url, params = query_args)

# Confirm url encoding
# print (response.url)

gcode_data = json.loads(response.content)
user_coordinates = gcode_data['results'][0]['geometry']['location']

print 'Latitude: ' + str(user_coordinates['lat'])
print 'Longitude: ' + str(user_coordinates['lng'])
