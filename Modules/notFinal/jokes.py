import requests
from lxml import html
from bs4 import BeautifulSoup
from speechRecAI import SpeechAI
from textToSpeechAI import speak
from random import randint

S = SpeechAI()
def jokes():
    random_number = randint(1, 307)
    num = str(random_number)
    session_requests = requests.session()
    url="http://onelinefun.com/"+num+"/"
    # print(url)
    r = session_requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    print("done")
    data = soup.find_all("div", {'class':"oneliner"})
    print("done")
    jokes=[]
    for i in range(len(data)):
        joke=data[i].find_all("p")
        for i in joke:
            j=i.text
            jokes.append(j)
    length = len(jokes)
    x = randint(0, length-1)
    print(jokes[x])
    speak(jokes[x])

if __name__=="__main__":
    jokes()
