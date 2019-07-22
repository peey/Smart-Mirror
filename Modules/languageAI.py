import random
import datetime

from mirror import send

class naturalLanguageAI(object):
    def __init__(self,userName=None):
        if userName is None:
            self.userName = ""
        else:
            self.userName = userName
        random.seed(datetime.datetime.now())

    def timeOfDay(self,date):
        phrase = ""

        if date.hour < 11:
            phrase = "morning"
        elif (date.hour >= 11) and (date.hour < 18):
            phrase = "afternoon"
        elif date.hour >= 18:
            phrase = "evening"

        return phrase

    def acknowledge(self):

        personal = [
            "What can I do for you, %s" % self.userName,
            "How can I help you today, %s" % self.userName,
            "Hi %s, what can I do for you?" % self.userName,
            "Hey %s, what can I do for you?" % self.userName,
            "How can I help you, %s" % self.userName
        ]

        simple = [
            "Yes ?",
            "What can I Do for you ?",
            "How can I help you today ?"
        ]

        selection = -1

        if len(self.userName) > 0:
            selection = random.randint(0,2)
        else:
            selection = random.randint(0,1)

        phrase = ""

        if selection == 0:
            phrase = random.choice(simple)
        elif selection == 1:
            phrase = "Good %s, What can I do for you?" % self.timeOfDay(datetime.datetime.now())
        else:
            phrase = random.choice(personal)

        return phrase

    def user_compliment(self,category="positive",property=None):
        phrase=""

        positive = [
            "good",
            "nice",
            "great",
            "fresh",
            "beautiful",
            "perfect",
            "cool"
        ]

        negative = [
            "bad",
            "terrible"
        ]

        neutral = [
            "okay",
            "alright"
        ]

        selection = positive
        if category == 'negative':
            selection = negative
        elif category == 'neutral':
            selection = neutral

        if property == "general":
            phrase = "You look %s" %(random.choice(selection))
        elif property == "clothes":
            verb = "look"
            item = random.choice(["clothes","outfit"])
            if item == "outfit":
                verb = verb + "s"
            phrase = "Your %s %s %s" %(item,verb,random.choice(selection))
        elif property == "hair":
            item = random.choice(["hair","hairstyle","up do"])
            phrase = "Your %s looks %s" %(item,random.choice(selection))
        return phrase

    def interaction(self,property=None):

        casualGreetings = [
            "Hi",
            "Hey",
            "Hello"
        ]

        funnyGreetings = [
            "what's up?",
            "howdy",
            "what's crackin'?",
        ]

        positive = [
            "I'm doing well",
            "Great, thanks for asking",
            "I'm doing great"
        ]

        negative = [
            "I'm not doing well",
            "I'm feeling terrible",
            "I'm not doing well today",
            "I could be much better"
        ]

        neutral = [
            "I'm doing alright",
            "I'm okay",
            "I could be better",
            "I'm alright"
        ]

        apprec = [
            "No problem!",
            "Any time",
            "You are welcome",
            "You're welcome",
            "Sure, no problem",
            "Of course",
            "Don't mention it",
            "Don't worry about it"
        ]

        phrase = ""
        if property == "greeting":
            selection = random.randint(0,4);
            if(selection==1 or selection==4):
                phrase = "Good %s" %(self.timeOfDay(datetime.datetime.now()))
                if len(self.userName) > 0:
                    if(random.randint(0,1)==1):
                        phrase = phrase + self.userName
            elif (selection == 0 or selection == 3):
                phrase = random.choice(casualGreetings)
                if len(self.userName) > 0:
                    if(random.randint(0,1)==1):
                        phrase = phrase + self.userName
            elif (selection==2):
                phrase = random.choice(funnyGreetings)
            return phrase

        elif property == "personalStatus":
            i = random.randint(0,2)
            category = "neutral"
            if i == 0:
                category = "positive"
            elif i==1:
                category = "negative"
            else:
                category = "neutral"

            if category == 'negative':
                return random.choice(negative)
            elif category == 'neutral':
                return random.choice(neutral)

            return random.choice(positive)

        elif property == "appreciation":
            return random.choice(apprec)

        elif property == "face":
            """
            @Peeyush, Send face.gif here to UI
            """
            send({
                "type": "image",
                "src": "face.gif" 
            })
