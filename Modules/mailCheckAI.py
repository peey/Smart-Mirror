import email
import imaplib
from speechRecAI import SpeechAI
from textToSpeechAI import speak

import mirror

mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
userName = "madhur16053@iiitd.ac.in"
passWord = "ngyuxana23"
mail.login(userName,passWord)

def checkMail():
    mail.select("INBOX")
    maxShow = 5
    (retCode, messages) = mail.search(None, '(UNSEEN)')
    if retCode == 'OK':
        unreadCount = len(messages[0].split())
        if unreadCount > 0:
            speak("You have some unread emails")
            speak("Here are some of them!")
        latestMail = unreadCount-1
        toSend = []
        while(maxShow > 0):
            mailType, data = mail.fetch(messages[0].split()[latestMail],'(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    actualMail = email.message_from_bytes(response_part[1])
                    toSend.append({
                        "from": actualMail['From'],
                        "subject": actualMail['Subject']
                    })
                mailType, data = mail.store(messages[0].split()[latestMail],'-FLAGS','\\Seen')
            maxShow -= 1
            latestMail -= 1
        
        mirror.send({
            "type": "check-mail",
            "mails": toSend
        })

