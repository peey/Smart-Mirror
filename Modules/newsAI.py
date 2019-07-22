import requests
import json
import random
from textToSpeechAI import speak
from speechRecAI import SpeechAI
from server import sendToClient

wit_token = "Bearer A5YKQ3WVJPMYBDUA655USHMZ3HHJ4ZQE"

sources={'general':["bbc-news","bloomberg","business-insider","cnbc","cnn","daily-mail","google-news","mirror","time","the-huffington-post",
                           "the-telegraph","the-washington-post"]
        ,'india':["the-hindu","the-times-of-india"]
        ,'tech':["engadget","hacker-news","mashable","recode","techcrunch","techradar","the-next-web","the-verge"]}

class news(object):
    def __init__(self,api_token="eb684db927dc458f8907a8c5afa2b857"):
        self.api = api_token

    def findNews(self,intent):
        newsList = []
        for i in range(0,5):
            x = random.choice(sources[intent])
            print(x)
            newsRequestURL = "https://newsapi.org/v1/articles?source=%s&apiKey=%s" % (x,self.api)
            r = requests.get(newsRequestURL)
            newsJSON = json.loads(r.text)
            newsD = {"title":newsJSON['articles'][i]['title'],"image":newsJSON['articles'][i]['urlToImage'],"description":newsJSON['articles'][i]['description']}
            newsList.append(newsD)
        return newsList

if __name__=="__main__":
    N = news()
    S = SpeechAI(0.30)
    record,audio = S.ears()
    news_phrase = S.recognize(record,audio)
    if news_phrase is not None:
        r = requests.get('https://api.wit.ai/message?v=20170303&q=%s' % news_phrase,
                                 headers={"Authorization": wit_token})
        print (r.text)
        response = json.loads(r.text)
        if "entities" in response and "news" in response['entities']:
            entities = response['entities']
            intent = response['entities']['news'][0]["value"]
            print(intent)
            N.findNews(intent)
        else:
            print("Couldn't Understand")
