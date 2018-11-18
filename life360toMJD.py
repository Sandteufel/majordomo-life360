#!/usr/bin/python
# coding=utf-8

from life360 import life360
import datetime
import requests

#Make test that user is online and his phone sending geodata
def testdate( d):
    diff = datetime.datetime.now() - d
    s = diff.seconds
    if s < 3600:
        return '1'
    else:
        return '0'

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
            speed = m['location']['speed']
            charge = m['location']['charge']
            accuracy = m['location']['accuracy']
            user_status = testdate(datetime.datetime.fromtimestamp(int(m['location']['timestamp'])))
            if user_status == "1":
                r = requests.post("http://localhost/gps.php", data={'deviceid': user, 'location': location, 'accuracy': accuracy, 'speed': speed, 'battlevel': battery, 'charging': charge})
    else:
        print "Error authenticating"
