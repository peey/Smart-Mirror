import requests
import json
from textToSpeechAI import speak
from speechRecAI import SpeechAI
import faceAI
import time

wit_token = "Bearer A5YKQ3WVJPMYBDUA655USHMZ3HHJ4ZQE"

class maps(object):
    def __init__(self,api_token="AIzaSyDnOPEB0gow2PJU1NFcU9Fjj_EWkRj2HCo"):
        self.api = api_token

    def getLocation(self,location,api="AIzaSyBLZ9n9BB5zlLiqZnz0Q7f8sv8yU8axcoc"):
        locationRequestURL = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(location,api)
        r = requests.get(locationRequestURL)
        locationJSON = json.loads(r.text)

        latitude = locationJSON['results'][0]['geometry']['location']['lat']
        longitude = locationJSON['results'][0]['geometry']['location']['lng']

        locationDict = {'lat':latitude,'long':longitude}
        return locationDict

    def findMap(self,intent,location):

        locationDict = self.getLocation(location)
        latitude = locationDict['lat']
        longitude = locationDict['long']
        locationString = str(latitude)+","+str(longitude)

        if intent == "satellite":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=16&scale=false&size=1200x600&maptype=satellite&format=png&key=%s" % (locationString,self.api)
        elif intent == "terrain":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=16&scale=false&size=1200x600&maptype=terrain&format=png&key=%s" % (locationString,self.api)
        elif intent == "hybrid":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=16&scale=false&size=1200x600&maptype=hybrid&format=png&key=%s" % (locationString,self.api)
        elif intent == "roadmap":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=16&scale=false&size=1200x600&maptype=roadmap&format=png&key=%s" % (locationString,self.api)

if __name__ == "__main__":
    M = maps()
    F = faceAI.faceAI(camera=0)
    S = SpeechAI(0.30)
    while True:
        if F.detect_face():
            print("Found Face")
            record,audio = S.ears()
            map_phrase = S.recognize(record,audio)
            if map_phrase is not None:
                r = requests.get('https://api.wit.ai/message?v=20170303&q=%s' % map_phrase,
                                         headers={"Authorization": wit_token})
                print(r.text)
                response = json.loads(r.text)
                if "entities" in response and "maps" in response['entities'] and "location" in response['entities']:
                    entities = response['entities']
                    intent = response['entities']['maps'][0]["value"]
                    maxConf = 0
                    location = response['entities']['location'][0]["value"]
                    for i in response['entities']['location']:
                        if i["confidence"] > maxConf:
                            maxConf = i["confidence"]
                            location = i["value"]
                    print(intent)
                    print(location)
                    if location is not None and intent is not None:
                        LJ = M.getLocation(location)
                        print(M.findMap(intent,location))
                    else:
                        print("Couldn't Understand")
