import requests
from lxml import html
from bs4 import BeautifulSoup
from speechRecAI import SpeechAI
from textToSpeechAI import speak
from random import randint

S = SpeechAI()
def Quotes():
    random_number = randint(2, 50)
    num = str(random_number)
    session_requests = requests.session()
    url="http://www.quotery.com/lists/top-500-greatest-quotes-of-all-time/"+num+"/"
    r = session_requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    print("done")
    data = soup.find_all("div", {'class':"blog-quote"})
    print("done")
    quotes=[]
    for i in range(len(data)):
        # print(data[i])
        # print()
        # print()
        # print()
        # print()
        quote = data[i].find_all("div", {'class':"blog-quote__content"})
        person = data[i].find_all("div", {'class':"blog-quote__author"})
        y = min(len(quote),len(person))
        for i in range(y):
            content = quote[i].text
            author = person[i].text
            array=[content, author]
            quotes.append(array)
    length = len(quotes)
    x = randint(0, length-1)
    print(quotes[x][0])
    print(quotes[x][1])
    speak(quotes[x][0])
    speak("said by "+quotes[x][1])


if __name__=="__main__":
    Quotes()
