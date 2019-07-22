import requests
import json
from textToSpeechAI import speak
from speechRecAI import SpeechAI
import faceAI
import time
from server import sendToClient

wit_token = "Bearer A5YKQ3WVJPMYBDUA655USHMZ3HHJ4ZQE"

class weather(object):
    def __init__(self,api_token="950951c817661da678abe272ffa9a27f"):
        self.api = api_token

    def getIP(self):
        IP_URL = "http://jsonip.com/"
        r = requests.get(IP_URL)
        ipJSON = json.loads(r.text)
        return ipJSON['ip']

    def getLocation(self):
        locationRequestURL = "http://freegeoip.net/json/%s" % self.getIP()
        r = requests.get(locationRequestURL)
        locationJSON = json.loads(r.text)

        latitude = locationJSON['latitude']
        longitude = locationJSON['longitude']

        locationDict = {'lat':latitude,'long':longitude}
        return locationDict

    def UNIX_to_Time(self,epoch):
        return time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch))

    def get_DifferentLocation(self,location,api="AIzaSyBLZ9n9BB5zlLiqZnz0Q7f8sv8yU8axcoc"):
        locationRequestURL = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(location,api)
        r = requests.get(locationRequestURL)
        locationJSON = json.loads(r.text)

        latitude = locationJSON['results'][0]['geometry']['location']['lat']
        longitude = locationJSON['results'][0]['geometry']['location']['lng']

        locationDict = {'lat':latitude,'long':longitude}
        return locationDict

    def findWeather(self,intent,locationDict):
        latitude = locationDict['lat']
        longitude = locationDict['long']

        weatherRequestURL = "https://api.darksky.net/forecast/%s/%s,%s" % (self.api,latitude,longitude)
        r = requests.get(weatherRequestURL)
        weatherJSON = json.loads(r.text)

        D = {'daily':weatherJSON['daily'],'currently':weatherJSON['currently'],'hourly':weatherJSON['hourly']}
        """
        daily gives for 8 days, things to extract are "summary","humidity","temperatureMin",
        "temperatureMax","icon","windSpeed","pressure","time"
        """

        """
        currently gives the current weather ONLY (thus, 1 forecast). Things to extract are
        "summary","humidity","temperature","icon","windSpeed","pressure","time"
        """

        """
        hourly gives the hourly forecast for 2 days i.e. 48 predictions for 48 hours.
        Things to extract are "temperature","icon","windSpeed","humidity","summary","pressure"
        ,"time"
        """

        """
        clear-day, clear-night
        rain
        snow
        sleet
        wind
        fog
        cloudy
        partly-cloudy-day
        partly-cloudy-night
        """

        def processIcon(icon):
            if icon == "clear-day":
                return "day-sunny"
            elif icon == "clear-night":
                return "night-clear"
            elif icon == "partly-cloudy-day":
                return "day-cloudy"
            elif icon == "partly-cloudy-night":
                return "night-partly-cloudy"
            else:
                return icon

        if intent=="current":
            CW = D['currently']
            temp = round(((int(CW['temperature'])-32)*5)/9, 2)
            # print(CW['summary'],"%.2f" % temp,CW['icon'],CW['humidity'],CW['pressure'],self.UNIX_to_Time(CW['time']))
            return {
                "temperature": temp,
                "humidity": CW['humidity'] * 100,
                "pressure": CW['pressure'],
                "icon": processIcon(CW["icon"])
            }, CW['summary']
        elif intent=="tomorrow":
            CW = D['daily']['data']
            tomData = CW[1]
            tempMin = round(((int(tomData['temperatureMin'])-32)*5)/9, 2)
            tempMax = round(((int(tomData['temperatureMax'])-32)*5)/9, 2)
            # print(tomData['summary'],"%.2f" % tempMin,"%.2f" % tempMax,tomData['icon'],tomData['humidity'],tomData['pressure'],self.UNIX_to_Time(tomData['time']))
            return {
                "summary": tomData["summary"],
                "tempMin": tempMin,
                "tempMax": tempMax,
                "icon": processIcon(tomData["icon"])
            }, tomData["summary"]
        elif intent=="3-day":
            CW = D['daily']['data']
            toReturn = []
            for i in range(0,3):
                tomData = CW[i]
                tempMin = round(((int(tomData['temperatureMin'])-32)*5)/9, 2)
                tempMax = round(((int(tomData['temperatureMax'])-32)*5)/9, 2)
                toReturn.append({
                    "tempMin": tempMin,
                    "tempMax": tempMax,
                    "icon": processIcon(tomData["icon"]),
                    "day": time.strftime("%A", time.localtime(tomData['time']))
                })
                # print(tomData['summary'],"%.2f" % tempMin,"%.2f" % tempMax,tomData['icon'],tomData['humidity'],tomData['pressure'],self.UNIX_to_Time(tomData['time']))
            return toReturn, CW[2]['summary'] + " by " + toReturn[2]["day"]
        elif intent=="7-day":
            CW = D['daily']['data']
            toReturn = []
            for i in range(0,8):
                tomData = CW[i]
                tempMin = round(((int(tomData['temperatureMin'])-32)*5)/9, 2)
                tempMax = round(((int(tomData['temperatureMax'])-32)*5)/9, 2)
                toReturn.append({
                    "tempMin": tempMin,
                    "tempMax": tempMax,
                    "icon": processIcon(tomData["icon"]),
                    "day": time.strftime("%A", time.localtime(tomData['time']))
                })
                # print(tomData['summary'],"%.2f" % tempMin,"%.2f" % tempMax,tomData['icon'],tomData['humidity'],tomData['pressure'],self.UNIX_to_Time(tomData['time']))
            return toReturn,  CW[7]['summary'] + " by " + toReturn[7]["day"]
        elif intent=="hourly":
            CW = D['hourly']['data']
            toReturn = []
            for i in range(0,6):
                hourData = CW[i]
                temp = round(((int(hourData['temperature'])-32)*5)/9, 2)
                toReturn.append({
                    "temp": temp,
                    "hour": time.strftime("%I%p", time.localtime(hourData['time'])).strip("0"),
                    "icon": processIcon(hourData["icon"])
                })
                print(hourData)
                # print(hourData['summary'],"%.2f" % temp,hourData['icon'],hourData['humidity'],hourData['pressure'],self.UNIX_to_Time(hourData['time']))
            return toReturn, CW[5]['summary'] + " by " + toReturn[5]["hour"]

if __name__ == "__main__":
    W = weather()
    F = faceAI.faceAI(camera=0)
    S = SpeechAI(0.30)
    while True:
        if F.detect_face():
            print("Found Face")
            record,audio = S.ears()
            weather_phrase = S.recognize(record,audio)
            if weather_phrase is not None:
                r = requests.get('https://api.wit.ai/message?v=20170303&q=%s' % weather_phrase,
                                         headers={"Authorization": wit_token})
                print(r.text)
                response = json.loads(r.text)
                if "entities" in response and "weather" in response['entities'] and "location" in response['entities']:
                    entities = response['entities']
                    intent = response['entities']['weather'][0]["value"]
                    maxConf = 0
                    location = response['entities']['location'][0]["value"]
                    for i in response['entities']['location']:
                        if i["confidence"] > maxConf:
                            maxConf = i["confidence"]
                            location = i["value"]
                    print(intent)
                    print(location)
                    if location is not None:
                        LJ = W.get_DifferentLocation(location)
                        W.findWeather(intent,LJ)
                elif "entities" in response and "weather" in response['entities']:
                    entities = response['entities']
                    intent = response['entities']['weather'][0]["value"]
                    print(intent)
                    LJ = W.getLocation()
                    W.findWeather(intent,LJ)
                else:
                    print("Couldn't Understand")
