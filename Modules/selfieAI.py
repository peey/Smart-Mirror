import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import speechRecAI
import time
import string
from cv2 import *
from studentEmailDb import dict as emails
import mirror
import config

respond = mirror.respond
send = mirror.send

S = speechRecAI.SpeechAI(0.55)

def SendMail(ImgFileName, theft=False):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('smart.mirrorai@gmail.com', 'smartmirror23')
    if theft == False:
        Roll = 'default'
        while Roll not in emails or Roll.lower() != "cancel":
            if Roll.lower() == "cancel":
                return
            respond("Say your Roll Number", False)
            record, audio = S.ears()
            Roll = S.recognize(record,audio)
            for i in string.punctuation:
                Roll=Roll.replace(i,"")
            Roll=Roll.replace(" ","")
        Recipient = emails[Roll]["email"]

        msg = MIMEMultipart()
        msg['Subject'] = 'Your Sexy Picture!'
        msg['From'] = 'smart.mirrorai@gmail.com'
        msg['To'] = Recipient

        text = MIMEText('Hi Sexy!')
        msg.attach(text)
        if ImgFileName!=None:
            img_data = open(ImgFileName, 'rb').read()
            image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
            msg.attach(image)
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        else:
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Mail Sent")
        s.quit()
    else:
        msg = MIMEMultipart()
        msg['Subject'] = 'Thief at Home!'
        msg['From'] = 'smart.mirrorai@gmail.com'
        msg['To'] = 'madhur16053@iiitd.ac.in'

        text = MIMEText('Please be alert and call Police')
        msg.attach(text)
        if ImgFileName!=None:
            img_data = open(ImgFileName, 'rb').read()
            image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
            msg.attach(image)
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        else:
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Mail Sent")
        s.quit()

"""
def getImageName():
    base = "../client/selfies/"
    try:
        file = open(base + "counter.txt", "r+")
        counter = int(file.readline())
        counter += 1
        file.seek(0)
        file.write(str(counter))
        file.truncate()
        file.close()
    except FileNotFoundError:
        file = open(base + "counter.txt", "w+")
        file.write("0")
        file.close()
        counter = 0
    return base + str(counter) + ".jpg" # like 1.jpg, etc
"""


def capture(theft=False):
    base = "../client/selfies/"
    if theft == False:
        for i in range(3,0,-1):
            respond(str(i))
        respond("Say cheese!")
        time.sleep(0.5)
        cam = VideoCapture(config.camera)
        s, img = cam.read()
        if s:
            namedWindow("cam-test")
            imshow("cam-test",img)
            # waitKey(5000)
            """
            @Peeyush, Send filename.jpg to UI here
            for 5 seconds.
            Also, send a text saying "Mail Sent" to UI
            """
            destroyWindow("cam-test")
            imwrite(base+'filename.jpg',img)
    else:
        cam = VideoCapture(config.camera)
        s, img = cam.read()
        if s:
            namedWindow("cam-test")
            imshow("cam-test", img)
            destroyWindow("cam-test")
            imwrite(base + 'filename.jpg', img)

if __name__=="__main__":
    base = "../client/selfies/"
    capture()
    SendMail(base+'filename.jpg')
