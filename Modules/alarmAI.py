from datetime import datetime
from textToSpeechAI import speak
import time
import faceAI
import speechRecAI

F = F = faceAI.faceAI(camera=0)
S = speechRecAI.SpeechAI(0.30,phrase="okay mirror")
# record,audio = S.ears()
# x = S.recognize(record,audio)

def alarm(alarm_hour, alarm_minute, alarm_weekday, repeat=False):

    stop = False
    while(True):
        minute=datetime.today().minute
        hour=datetime.today().hour
        day = datetime.today().weekday()
        if(alarm_weekday == "everyday"):
            if alarm_minute==minute and alarm_hour==hour and stop==False:
                while not F.detect_face():
                    speak("wake up")
                if F.detect_face():
                    stop=True

        else:
            if alarm_weekday==day and alarm_minute==minute and alarm_hour==hour and stop==False:
                while not F.detect_face():
                    speak("wake up")
                if F.detect_face():
                    stop=True
                    break

    while(repeat):
        time.sleep(61)
        while(True):
            minute=datetime.today().minute
            hour=datetime.today().hour
            day = datetime.today().weekday()

            if alarm_weekday==day and alarm_minute==minute and alarm_hour==hour:
                speak("wake up")
                break

def Create_Alarm(alarm_hour=None, alarm_minute=None, alarm_weekday=None, evening= None, repeat=None):
        minute = datetime.today().minute
        hour = datetime.today().hour
        weekday = datetime.now().weekday()


        if(alarm_hour==None and alarm_minute==None):
            speak("at what time do you want to set the alarm")
            # alarm_hour=eval(input("hour: "))
            print("hour: ")
            record,audio = S.ears()
            alarm_hour = S.recognize(record,audio)
            alarm_hour=int(alarm_hour)
            # alarm_minute=eval(input("minute: "))
            print("minute: ")
            record,audio = S.ears()
            alarm_minute = S.recognize(record,audio)
            alarm_minute=int(alarm_minute)
        if(alarm_weekday==None):
            speak("which day of the week do you want the alarm to ring")
            # alarm_weekday=input("day of the week: ")
            print("day of the week: ")
            record,audio = S.ears()
            alarm_weekday = S.recognize(record,audio)
            alarm_weekday = str(alarm_weekday)
            b=False
            while(b==False):
                if "everyday" in alarm_weekday or (("whole" in alarm_weekday or "complete" in alarm_weekday) and "week" in alarm_weekday):
                    alarm_weekday="everyday"
                    b=True
                elif ("0"<=alarm_weekday and "6">=alarm_weekday):
                    alarm_weekday = int(alarm_weekday)
                    b=True
                elif "day after tomorrow" in alarm_weekday:
                    alarm_weekday = weekday+2
                    b=True
                elif "tomorrow" in alarm_weekday:
                    alarm_weekday = weekday+1
                    b=True
                elif "monday" in alarm_weekday:
                    alarm_weekday=0
                    b=True
                elif "tuesday" in alarm_weekday:
                    alarm_weekday=1
                    b=True
                elif "wednesday" in alarm_weekday:
                    alarm_weekday=2
                    b=True
                elif "Thursday" in alarm_weekday:
                    alarm_weekday=3
                    b=True
                elif "friday" in alarm_weekday:
                    alarm_weekday=4
                    b=True
                elif "saturday" in alarm_weekday:
                    alarm_weekday=5
                    b=True
                elif "sunday" in alarm_weekday:
                    alarm_weekday=6
                    b=True
                elif "today" in alarm_weekday:
                    alarm_weekday=weekday
                    b=True
                else:
                    speak("sorry, could not understand")
                    speak("which day of the week do you want the alarm to ring")
                    # alarm_weekday=input("day of the week: ")
                    print("day of the week: ")
                    record,audio = S.ears()
                    alarm_weekday = S.recognize(record,audio)

        if(repeat==None):
            speak("do you want the alarm to repeat")
            # repeat=input("repeat(y/n): ")
            print("repeat(y/n): ")
            record,audio = S.ears()
            repeat = S.recognize(record,audio)
            if("yes" in repeat):
                repeat=True
            else:
                repeat = False

        if evening==None:
            if(alarm_hour<12):
                speak("do you want to set the alarm for morning or evening")
                # choice=input()
                record,audio = S.ears()
                choice = S.recognize(record,audio)
                if "evening" in choice:
                    alarm_hour+=12

        if alarm_weekday!="everyday":

            total_time = weekday*24*60+hour*60+minute
            alarm_total_time = alarm_weekday*24*60+alarm_hour*60+alarm_minute

            if total_time>alarm_total_time:
                interval = 7*24*60-(total_time-alarm_total_time)
            else:
                interval = -(total_time-alarm_total_time)
            interval_days = int(interval/(24*60))
            interval = int(interval)%(24*60)
            interval_hour = int(interval/60)
            interval_minute= interval%60


            print(interval_days)
            print(interval_hour)
            print(interval_minute)
            present_day=datetime.now().weekday()
            ring_day=present_day+interval_days
            string=""
            string+=("alarm set to ring ")
            if(interval_days>0):
                if interval_days==1:
                    string+=("after "+str(interval_days)+" day")
                else:
                    string+=("after "+str(interval_days)+" days")

                if interval_hour>0:
                    if interval_hour==1:
                        string+=(str(interval_hour)+" hour")
                    else:
                        string+=(str(interval_hour)+" hours")

                    if interval_minute>0:
                        if interval_minute==1:
                            string+=("and "+ str(interval_minute)+"minute" )
                        else:
                            string+=("and "+ str(interval_minute)+"minutes" )

                else:
                    if interval_minute>0:
                        if(interval_minute==1):
                            string+=("and "+ str(interval_minute)+"minute" )
                        else:
                            string+=("and "+ str(interval_minute)+"minutes" )

            elif interval_hour>0:
                if interval_hour==1:
                    string+=("after "+ str(interval_hour)+" hour")
                else:
                    string+=("after "+ str(interval_hour)+" hours")

                if interval_minute>0:
                    if interval_minute==1:
                        string+=("and "+ str(interval_minute)+"minute" )
                    else:
                        string+=("and "+ str(interval_minute)+"minutes" )
            elif interval_minute>0:
                if interval_minute==1:
                    string+=("after "+ str(interval_minute)+"minute" )
                else:
                    string+=("after "+ str(interval_minute)+"minutes" )

            speak(string)
        else:
            minute = datetime.today().minute
            hour = datetime.today().hour
            weekday = datetime.now().weekday()

            if hour > alarm_hour or minute > alarm_minute:
                x = weekday + 1
            else:
                x = weekday
            print("weekday: ", weekday)
            print("x: ",x)
            total_time = weekday*24*60+hour*60+minute
            alarm_total_time = x*24*60+alarm_hour*60+alarm_minute

            if total_time>alarm_total_time:
                interval = 7*24*60-(total_time-alarm_total_time)
            else:
                interval = -(total_time-alarm_total_time)
            interval_days = int(interval/(24*60))
            interval = int(interval)%(24*60)
            interval_hour = int(interval/60)
            interval_minute= interval%60


            print(interval_days)
            print(interval_hour)
            print(interval_minute)
            present_day=datetime.now().weekday()
            ring_day=present_day+interval_days
            string=""
            string+=("alarm set to ring ")
            if(interval_days>0):
                if interval_days==1:
                    string+=("after "+str(interval_days)+" day")
                else:
                    string+=("after "+str(interval_days)+" days")

                if interval_hour>0:
                    if interval_hour==1:
                        string+=(str(interval_hour)+" hour")
                    else:
                        string+=(str(interval_hour)+" hours")

                    if interval_minute>0:
                        if interval_minute==1:
                            string+=("and "+ str(interval_minute)+"minute" )
                        else:
                            string+=("and "+ str(interval_minute)+"minutes" )

                else:
                    if interval_minute>0:
                        if(interval_minute==1):
                            string+=("and "+ str(interval_minute)+"minute" )
                        else:
                            string+=("and "+ str(interval_minute)+"minutes" )

            elif interval_hour>0:
                if interval_hour==1:
                    string+=("after "+ str(interval_hour)+" hour")
                else:
                    string+=("after "+ str(interval_hour)+" hours")

                if interval_minute>0:
                    if interval_minute==1:
                        string+=("and "+ str(interval_minute)+"minute" )
                    else:
                        string+=("and "+ str(interval_minute)+"minutes" )
            elif interval_minute>0:
                if interval_minute==1:
                    string+=("after "+ str(interval_minute)+"minute" )
                else:
                    string+=("after "+ str(interval_minute)+"minutes" )

            speak(string)


        if (alarm_weekday!="everyday"):
            alarm_weekday=int(alarm_weekday)
        alarm(alarm_hour, alarm_minute, alarm_weekday, repeat)


if __name__=="__main__":
    Create_Alarm()
