import requests
import json
from speechRecAI import SpeechAI
from textToSpeechAI import speak

class mandi(object):
    def __init__(self,api_token,commodity,state):
        self.api=api_token
        self.commodity = commodity
        self.state = state

    def find_price(self):
        mandi_req_url = "https://data.gov.in/api/datastore/resource.json?resource_id=9ef84268-d588-465a-a308-a864a43d0070&api-key=%s" % (self.api)
        r = requests.get(mandi_req_url)
        mandi_json = json.loads(r.text)
        commodity = self.commodity
        state = self.state
        flag=0
        for i in mandi_json['records']:
            if state in i['state'] and commodity=="" :
                modalPrice = i['modal_price']
                market = i['market']
                district = i['district']
                State = i['state']
                Commodity=i['commodity']
                print("Today's price for %s is %s available from %s market, %s in %s" %(Commodity,modalPrice,market,district,State))
                flag = 1

            elif state=="" and commodity not in i['commodity'] :
                modalPrice = i['modal_price']
                market = i['market']
                district = i['district']
                State = i['state']
                print("Today's price for %s is %s available from %s market, %s in %s" %(commodity,modalPrice,market,district,State))
                flag = 3

            elif commodity in i['commodity'] and state in i['state']: #and state in i['state']:
                modalPrice = i['modal_price']
                market = i['market']
                district = i['district']
                State = i['state']
                print("Today's price for commodity %s is %s available from %s market, %s in %s" %(commodity,modalPrice,market,district,State))
                flag=2

        if(flag==0):
            print("Prices for commodity %s could not be found"%(commodity))

if __name__=="__main__":
    # S = SpeechAI()
    # record,audio = S.ears()
    # commodity = S.recognize(record,audio)
    # char = commodity[0]
    # commodity = char.upper()+commodity[1:].lower()
    # state = S.recognize(record,audio)
    # char = state[0]
    # commodity = char.upper()+state[1:].lower()
    state = input()
    commodity = input()
    if state == "none":
        state = ""
    if commodity == "none":
        commodity = ""
    m = mandi('d610ebfac70d277eed44f38a594dbb96',commodity, state)
    m.find_price()
