import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from speechRecAI import SpeechAI
from textToSpeechAI import speak
import string
from studentEmailDb import dict as emails

import mirror
import time

S = SpeechAI()

def SendMail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('smart.mirrorai@gmail.com', 'smartmirror23')
    Roll = 'default'
    mirror.send({
        "type": "send-mail",
        "recipient": "",
        "subject": "",
        "body": ""
    })

    while Roll not in emails:
        speak("Say the Roll Number of the Recipient")
        record,audio = S.ears()
        Roll = S.recognize(record,audio)
        for i in string.punctuation:
            Roll=Roll.replace(i,"")
        Roll=Roll.replace(" ","")
    Recipient = emails[Roll]["email"]
    speak("Sending a mail to "+ emails[Roll]["name"])

    mirror.send({
        "type": "send-mail",
        "recipient": emails[Roll]["name"] + " " + "<" + emails[Roll]["email"] + ">",
        "subject": "",
        "body": ""
    })

    speak("Say The Subject")
    record,audio = S.ears()
    sub = S.recognize(record,audio)
    print("Subject : "+ sub)

    mirror.send({
        "type": "send-mail",
        "recipient": emails[Roll]["name"] + " " + "<" + emails[Roll]["email"] + ">",
        "subject": sub,
        "body": ""
    })

    speak("Say The Content")
    record,audio = S.ears()
    content = S.recognize(record,audio)
    print("Content : "+ content)

    mirror.send({
        "type": "send-mail",
        "recipient": emails[Roll]["name"] + " " + "<" + emails[Roll]["email"] + ">",
        "subject": sub,
        "body": content
    })

    time.sleep(3)

    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = 'smart.mirrorai@gmail.com'
    msg['To'] = Recipient

    text = MIMEText(content)
    msg.attach(text)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    speak("Mail Sent")
    s.quit()

if __name__=="__main__":
    SendMail()
