import speech_recognition as speechAI
import time

class SpeechAI(object):
    def __init__(self,threshold=0.30,lex=False,phrase="hello"):
        self.phrase = phrase
        self.lex = lex
        self.threshold = threshold

    def recognize(self,recognize,audio):
        spoken = None
        transcript=""
        try:
            if(self.lex==False):
                min_conf = 1
                spoken = recognize.recognize_google(audio,key="AIzaSyAcalCzUvPmmJ7CZBFOEWx2Z1ZSn4Vs1gg",language = "en-IN",show_all=True)
                print(spoken)
                if spoken != []:
                    for i in spoken['alternative']:
                        if 'confidence' not in list(i.keys()):
                            transcript = spoken['alternative'][0]['transcript']
                            print("YOU SAID "+i['transcript'])
                            return transcript
                        elif i['confidence']<=min_conf and i['confidence']>=self.threshold:
                            min_conf = i['confidence']
                    for i in spoken['alternative']:
                        if i['confidence']==min_conf:
                            transcript = i['transcript']
                            print("YOU SAID "+i['transcript'])
                            break
                else:
                    print("Couldn't Understand")
            else:
                min_conf = 1
                spoken = recognize.recognize_google(audio,key="AIzaSyAcalCzUvPmmJ7CZBFOEWx2Z1ZSn4Vs1gg",language = "en-IN",show_all=True)
                print(spoken)
                outcomes = []
                if spoken != []:
                    for i in spoken['alternative']:
                        if 'confidence' not in list(i.keys()):
                            transcript = spoken['alternative'][0]['transcript']
                            print("YOU SAID "+i['transcript'])
                            return transcript
                        elif i['confidence']<=min_conf and i['confidence']>=self.threshold:
                            min_conf = i['confidence']
                    for i in spoken['alternative']:
                        if i['confidence']==min_conf:
                            outcomes.append(i['transcript'])
                    outcomes.sort()
                    print(outcomes)
                    transcript = outcomes[0]
                    print("YOU SAID "+transcript)
                            # transcript = i['transcript']
                            # print("YOU SAID "+i['transcript'])
                            # break
                else:
                    print("Couldn't Understand")
        except speechAI.UnknownValueError:
            print("Couldn't Understand")
        except speechAI.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return transcript

    def ears(self):
        micro_source = speechAI.Microphone()
        record = speechAI.Recognizer()
        with micro_source as source:
            record.adjust_for_ambient_noise(source,duration=1)
            record.dynamic_energy_threshold = True
            print("I am all Ears!")
            audio = record.listen(source)
        return record,audio

if __name__=="__main__":
    S = SpeechAI(0.30,"okay mirror")
    start = time.time()
    record,audio = S.ears()
    end = time.time()
    print("Time to record is %s" %(end-start))
    s = time.time()
    x = S.recognize(record,audio)
    e = time.time()
    print("Time to recognize is %s" %(e-s))
    if x==S.phrase:
        while True:
                record,audio = S.ears()
                S.recognize(record,audio)
    else:
        print("Say The Launching Phrase")
