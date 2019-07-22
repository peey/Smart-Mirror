import schedule
from textToSpeechAI import speak
import datetime
import time

def reminder(task):
    task_date=task[0]
    task_time=task[1]
    task_event=task[2]

    while True:
        present_day = str(datetime.datetime.now().day)
        present_month = str(datetime.datetime.now().month)
        present_year = str(datetime.datetime.now().year)
        present_hour = str(datetime.datetime.now().hour)
        present_minute = str(datetime.datetime.now().minute)
        present_date = present_day+" "+present_month+" "+present_year
        present_time= present_hour+"."+present_minute

        # print()
        # print(present_date, present_time)
        # print(task_date==present_date and task_time==present_time)
        # print(task_date, task_time)
        # print()

        if(task_date==present_date and task_time==present_time):
            display(task)
            speak("ALERT, you have a reminder for the event "+(task_event))
            break
        time.sleep(30)
        print("present date: "+present_date+"\t present time: "+present_time)

    remove_task(task_date, task_time, confirmation=True)

    set_reminder()

def display(task):
    task_date=task[0]
    task_time=task[1]
    task_event=task[2]

    print(task_date)
    print(task_time)
    print(task_event)

def remove_task(task_date=None, task_time=None, confirmation=False):
    file = open("reminder.txt", 'r')
    l = []
    for line in file:
        line = line.replace("\n","")
        line = line.replace("\r","")
        l.append(line)

    file.close()

    task_list = []
    parameters=3
    for i in range(0, len(l), parameters):
        task=[]
        for j in range(i, i+parameters):
            task.append(l[j])
        task_list.append(task)

    shortlist=[]

    if(task_date==None and task_time==None):
        speak("say the date of the reminder you want to remove")
        day = input("day: ")
        month = input("month: ")
        year = input("year: ")
        date = day+" "+month+" "+year

        print("remove date: ",date)
        for task in task_list:
            print("task: ", task)
            if(task[0]==date):
                shortlist.append(task)

        print("short listed: ",shortlist)
        if(len(shortlist)>1):
            for task in shortlist:
                display(task)
            speak("there are more than 1 reminders set for this date. Do you want to delete all of them?")
            choice=input("choice: ")


            if(choice=="no"):
                speak("say the time of the reminder you want to delete")
                hour = input("hour: ")
                minute = input("minute: ")
                # while not (minute<"61" and minute>="0") or (hour<="24" and hour>="0"):
                #     speak("sorry, couldn't understand, speak again")
                #     hour = input("hour: ")
                #     minute = input("minute: ")
                time = hour+"."+minute
                shortlist_time=[]

                for task in shortlist:
                    if(task[1]==time):
                        shortlist_time.append(task)


                if(len(shortlist_time)>1):
                    for task in shortlist_time:
                        display(task)
                    speak("there are more than 1 reminders set for this date and time. Do you want to delete all of them?")
                    choice2=input("choice: ")


                    if(choice2=="no"):
                        speak("say the event number you want to delete")
                        event_number = input("event number: ")
                        while not (event_number>="1" and event_number<=str(len(shortlist_time))):
                            speak("No event with this numberr exists. speak the number again")
                            event_number = input("event number: ")
                        event_number = int(event_number)
                        # print(list(shortlist_time[event_number-1]))
                        remove(task_list , list(shortlist_time[event_number-1]))
                else:
                    remove(task_list, shortlist_time)
        else:
            remove(task_list, shortlist)

    else:
            for task in task_list:
                if(task[0]==task_date and task[1]==task_time):
                    shortlist.append(task)
            if(confirmation==True):
                remove(task_list, shortlist)
            else:
                if (len(shortlist)>1):
                    speak("there are more than 1 reminders set for this date and time. Do you want to delete all of them?")
                    choice2=input("choice: ")
                    if(choice2=="no"):
                        speak("say the event number you want to delete")
                        event_number = input("event number: ")
                        while not (event_number>="1" and event_number<=len(shortlist_time)):
                            speak("No event with this numberr exists. speak the number again")
                            event_number = input("event number: ")
                        event_number = int(event_number)
                        print(shortlist[event_number-1])
                        remove(task_list , [shortlist[event_number-1]])
                else:
                    remove(task_list, list(shortlist))


def remove(task_list, delete_l):
    # print("task list: ", task_list)
    # print("to delete: ", delete_l)
    file = open("reminder.txt", 'w')
    count=0
    for task in task_list:
        b = False
        for delete_task in delete_l:
            print(task[0],delete_task[0])
            print(task[1],delete_task[1])
            print(task[2],delete_task[2])
            if(task[0]==delete_task[0] and task[1]==delete_task[1] and task[2]==delete_task[2]):
                print("deleted: ", delete_task)
                b=True
                break
        if(b==False):
            file.write(task[0]+"\n"+task[1]+"\n"+task[2]+"\n")
    file.close()


def set_reminder():
    file = open("reminder.txt", 'r')
    l = []
    for line in file:
        line = line.replace("\n","")
        line = line.replace("\r","")
        l.append(line)

    file.close()
    parameters = 3
    if len(l)>=parameters:
        task_list = []
        for i in range(0, len(l), parameters):
            task=[]
            for j in range(i, i+parameters):
                task.append(l[j])
            task_list.append(task)

        most_recent = task_list[0]
        for i in range(1, len(task_list)):
            if(most_recent[0]>task_list[i][0]):
                most_recent = task_list[i]

        same_date=[]
        for task in task_list:
            if task[0]==most_recent[0]:
                same_date.append(task)
        print("same date: ", same_date)

        highest_priority = same_date[0]
        for i in range(1, len(same_date)):
            if(highest_priority[1]>same_date[i][1]):
                highest_priority=same_date[i]

        print("highest priority: ",highest_priority)
        speak("next reminder set for the event"+ highest_priority[2])

        reminder(highest_priority)

def create_reminder(event=None, time=None, date = None):
    if(event==None):
        print('say the event')
        # speak("say the event")
        event=input("event: ")

    if (date==None):
        print('say the date')
        # speak("say the date")
        day = input("day: ")
        month = input("month: ")
        year = input("year: ")
        date = day+" "+month+" "+year

    if(time==None):
        print('say the time')
        # speak("say the time")
        hour = input("hour: ")
        minute = input("minute: ")
        print((minute<="60" and minute>="0") and (hour<="24" and hour>="0"))
        while not (minute<="60" and minute>="0") and (hour<="24" and hour>="0"):
            speak("sorry, couldn't understand, speak again")
            hour = input("hour: ")
            minute = input("minute: ")
        time = hour+"."+minute

    file = open("reminder.txt", 'a+')
    file.write(date+"\n"+time+"\n"+event+"\n")
    file.close()

    speak("reminder created to remind you of the event "+event)
    print("reminder created to remind you of the event "+event)

    set_reminder()

if __name__=="__main__":
    create_reminder()
    # remove_task()
    # speak("removed")
