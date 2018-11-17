#!/usr/bin/python
# coding=utf-8

from life360 import life360
import datetime
import requests

if __name__ == "__main__":

    # basic authorization hash (base64 if you want to decode it and see the sekrets)
    # this is a googleable or sniffable value. i imagine life360 changes this sometimes.
    authorization_token = "cFJFcXVnYWJSZXRyZTRFc3RldGhlcnVmcmVQdW1hbUV4dWNyRUh1YzptM2ZydXBSZXRSZXN3ZXJFQ2hBUHJFOTZxYWtFZHI0Vg=="

    # your username and password (hope they are secure!)
    username = "your_username"
    password = "your_password"

    #instantiate the API
    api = life360(authorization_token=authorization_token, username=username, password=password)
    if api.authenticate():

        #Grab some circles returns json
        circles =  api.get_circles()

        #grab id
        id = circles[0]['id']

        #Let's get your circle!
        circle = api.get_circle(id)

        #Let's display some goodies

        for m in circle['members']:
            user = m['firstName']
            location = m['location']['latitude'] +", "+ m['location']['longitude']
            battery = m['location']['battery']
            r = requests.post("http://127.0.0.1/gps.php", data={'deviceid': user, 'location': location, 'battlevel': battery})
    else:
        print "Error authenticating"
