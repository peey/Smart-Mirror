import requests
from lxml import html
from bs4 import BeautifulSoup
from speechRecAI import SpeechAI
from textToSpeechAI import speak
from random import randint

import mirror

S = SpeechAI()
def Quotes():
    random_number = randint(2, 50)
    num = str(random_number)
    session_requests = requests.session()
    url="http://www.quotery.com/lists/top-500-greatest-quotes-of-all-time/"+num+"/"
    r = session_requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    # print("done")
    data = soup.find_all("div", {'class':"blog-quote"})
    # print("done")
    quotes=[]
    for i in range(len(data)):
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

    quote = " ".join(quotes[x][0].replace("\n","").split(" "))
    author = " ".join(quotes[x][1].replace("\n","").split(" "))

    return quote + ". " + author, {
        "type": "quote",
        "quote": quote,
        "author": author
    }

if __name__=="__main__":
    Quotes()
