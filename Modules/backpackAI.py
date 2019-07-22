# -*- coding: utf-8 -*-
import sys
import codecs

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from textToSpeechAI import speak

class login:

    URL = 'https://www.usebackpack.com/welcome'

    character_list = 'abcdefghijklmnopqrstuvwxyz'

    username = []

    password = []

    driver = None

    start_time = None

    found_user = []

    found_password=[]

    def __init__(self):
        self.set_up()
        self.login()

    def set_up(self):
        print ("Setting everything up...")
        self.start_time = datetime.now()

        self.driver = webdriver.PhantomJS()
        print ("Done.")


    def login(self):
        print ("Starting")

        self.driver.get(self.URL)
        button = self.driver.find_element_by_id('loginButton')
        button.click()
        user_field = self.driver.find_element_by_id('user_email')
        user_field.clear()
        user_field.send_keys(email)
        password_field =  self.driver.find_element_by_id('user_password')
        password_field.clear()
        password_field.send_keys(password)
        submit = self.driver.find_element_by_css_selector('fieldset#body input[type=submit]')
        submit.click()

        self.driver.get("https://www.usebackpack.com/home")
        source = BeautifulSoup(self.driver.page_source,'lxml')
        user = source.find_all('span' ,{'class':"hidden-xs"})
        speak("logged in via "+user[0].text+"'s backpack")
        subjects = source.find_all('span', {"class":"course_link"})
        subjectList = {}

        for subject in subjects:
        	text = subject.text.lower()
        	text = text.replace("\n", "")
        	text = text.replace("  ", "")
        	text = text.replace("\t", "")
        	subjectList[text]={}
        	link = subject.find_all(href=True)
        	for i in link:
        		subjectList[text]['link']=i['href']
        		subjectList[text]['code']=str(i['href'])[-6:]

        Backpacklink = "https://www.usebackpack.com"
        flag = 0
        course = ""
        while flag != 1 or len(course)<5:
        	speak ("enter the course")

        	course = input("enter the course: ")
        	course = course.lower()
        	if (course=="cancel" or course=="abort" or course=="leave it"):
        		flag =0
        		speak("thanks for visiting")
        		break
        	if "total" in course or "number" in course or "what" in course or "courses" in course:
        		num = len(subjects)
        		speak("you have registered for "+str(num)+" courses")
        		speak("Here are the courses you have registered for")
        		for i in subjectList:
        			print(i)
        		flag = 0
        	else:
	        	for i in subjectList:
		        	if course in i:
		        		flag = 1
		        		course = i
		        		break
		        	elif course.replace(" ","") == subjectList[i]['code']:
		        		flag = 1
		        		course = i
		        		break
		        	else:
		        		flag = 0
		        if flag == 0:
		        	speak("no subject found with name "+course)
        if flag!=0:
        	speak("you have selected "+course)


        if flag == 1:
        	link = Backpacklink + subjectList[course]['link']
	        listURL = ['info','announcements','deadlines','resources','discussions','students'] #'grades'
	        subjectLinks = [link]
	        flag = 0
	        while flag!=1:
		        for subject in subjectLinks:
		        	speak("input the action you want to perform")
		        	action = input("input the action you want to perform: ")
		        	if (action =="cancel" or action =="abort" or action=="leave it"):
		        		flag = 1
		        		speak("thanks for visiting")
		        		break
		        	action = action.lower()
		        	for i in listURL:
		        		if i in  action or i[:-1] in action :
		        			url = link + '/' + i
				        	self.driver.get(url)
				        	source = BeautifulSoup(self.driver.page_source,'lxml')
				        	if i == 'announcements':
				        		Announcements(source)
				        	elif i == 'deadlines':
				        		Deadlines(source)
				        	elif i == 'resources':
				        		Resources(source)
				        	# elif i == 'grades':
				        	# 	Announcements(source)
				        	elif i == 'discussions':
				        		Discussions(source)
				        	elif i == 'students':
				        		Students(source)
				        	elif i == "info":
				        		Courseinfo(source)
				        	flag = 1
				        	break
				        else:
				        	flag = 0
		        if flag == 0:
		            speak("action cannot be performed.")


        print ("Done.")




    def check_exists_by_css_selector(self, selector):
        try:
            self.driver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return False
        return True

def strip(source, start_tag, end_tag):
	start_index = source.find(start_tag)
	len_start_tag = len(start_tag)
	len_end_tag = len(end_tag)
	text = []
	while start_index != -1:
		start_index += len_start_tag
		end_index = source.find(end_tag, start_index+1)
		string = source[start_index:end_index+1]
		text.append(string)
		start_index = source.find(start_tag, end_index+1)
	return text


def Announcements(source):
	print("ANNOUNCEMENTS")
	heading =[]
	body = []
	time = []
	announcements = source.find_all('div', {'class':'box'})
	for individual_announcement in announcements:
		h = individual_announcement.find_all("h4")
		for i in h:
			text = i.text.replace("\n","")
			text = text.replace("  ","")
			heading.append(text)
		t = individual_announcement.find_all('abbr', {'class':"timeago"})
		for i in t:
			time.append(i.text)
		b = individual_announcement.find_all("p")
		for i in range(len(b)):
			if i == 1:
				text = b[i].text.replace(u'\xa0',u' ' )
				body.append(b[i].text)


	count = 1
	announcement = {}
	for i in range(len(heading)):
		announcement[count]={}
		announcement[count]['heading']=heading[i]
		announcement[count]['time']=time[i]
		announcement[count]['body']=body[i]
		count+=1

	count = 0
	for i in announcement:
		if "New" in announcement[i]['heading'][-4:]:
			announcement[i]['heading'] = announcement[i]['heading'][:-3]
			count+=1

	if count == 0:
		speak("you do not have any new announcement")
		speak("Do you want to view the top 5 announcements")
	elif count == 1:
		speak("you have "+str(count)+" new announcement")
		speak("Do you want to view the announcement")
	else:
		speak("you have "+str(count)+" new announcements")
		speak("Do you want to view the announcements")

	choice = input("enter choice: ")
	if choice == "yes" and count!=0:
		for i in range(1, count+1):
			print(announcement[i])
	elif choice == "yes" and count==0:
		for i in range(1, 6):
			print(announcement[i])
	else:
		speak("thanks for visiting")

def Deadlines(source):
	print("DEADLINES")
	heading =[]
	body = []
	time = {}
	time['from']= []
	time['to']= []
	deadlines= source.find_all('div', {'class':'box'})
	for individual_deadlines in deadlines:
		# uprint(individual_deadlines)
		h = individual_deadlines.find_all("h4")
		for i in h:
			text = i.text.replace("\n","")
			text = text.replace("  ","")
			heading.append(text)
		t = individual_deadlines.find_all('abbr', {'class':"timeago"})
		for i in t:
			time['from'].append(i.text)

		# t = individual_deadlines.find_all('br')
		# for i  in t:
		# 	time['to'].append(i.text)
		b = individual_deadlines.find_all('p')
		for i in range(len(b)):
			if i == 1:
				text = b[i].text.replace(u'\xa0',u' ' )
				body.append(b[i].text)
			elif i == 0:
				# uprint(b[0].text)
				index = b[0].text.find("Due:")
				text = b[0].text[index:]
				text = text.replace("\n","")
				text = text.replace("  ","")
				time['to'].append(text)

	# uprint(heading)
	# print()
	# uprint(time)
	# print()
	# uprint(body)
	# print()

	count = 1
	deadline = {}
	# print(len(heading))
	# print(len(time))
	# print(len(body))
	for i in range(len(heading)):
		deadline[count]={}
		deadline[count]['heading']=heading[i]
		deadline[count]['time-from']=time['from'][i]
		deadline[count]['time-to']=time['to'][i]
		deadline[count]['body']=body[i]
		count+=1
	# for i in deadline:
	# 	print(i, deadline[i])

	count = 0
	for i in deadline:
		if "New" in deadline[i]['heading'][-4:]:
			deadline[i]['heading'] = deadline[i]['heading'][:-3]
			count+=1

	if count == 0:
		speak("you do not have any new deadline")
		speak("Do you want to view the top 5 deadlines")
	elif count == 1:
		speak("you have "+str(count)+" new deadline")
		speak("Do you want to view the deadline")
	else:
		speak("you have "+str(count)+" new deadlines")
		speak("Do you want to view the deadlines")

	choice = input("enter choice: ")
	if choice == "yes" and count!=0:
		for i in range(1, count+1):
			print(deadline[i])
	elif choice == "yes" and count==0:
		for i in range(1, 6):
			print(deadline[i])
	else:
		speak("thanks for visiting")


def Resources(source):
	print("RESOURCES")
	LIST = ['Tutorial_new', "Lecture_new", "Other_new", "Lab_new", "Homework_new", "Solution_new", "Project_new"]
	Resource = {}
	for ID in LIST:
		Resource[ID]={}
		heading =[]
		time = []
		s = source.find_all('div', {'id':ID})
		uprint("s",s)
		for source in s:
			resources = source.find_all('div', {'class':'box'})
			uprint(resources)
			for individual_resource in resources:
				h = individual_resource.find_all("h4")
				for i in h:
					text = i.text.replace("\n","")
					text = text.replace("  ","")
					heading.append(text)
				t = individual_resource.find_all('abbr', {'class':"timeago"})
				for i in t:
					time.append(i.text)
		Resource[ID]['heading']=heading
		Resource[ID]['time'] = time
	print(Resource)

def Courseinfo(source):
	print("COURSE INFO")
	heading =[]
	body = []
	courseinfo= source.find_all('div', {'class':'box'})
	for individual_courseinfo in courseinfo:
		# uprint(individual_deadlines)
		h = individual_courseinfo.find_all("h4")
		for i in h:
			text = i.text.replace("\n","")
			text = text.replace("  ","")
			heading.append(text)

		b = individual_courseinfo.find_all('p')
		for i in range(len(b)):
			if i == 0:
				text = b[i].text.replace(u"\xa0", u" ")
				body.append(b[i].text)

	info = {}
	for i in range(len(heading)):
		if len(body[i])!=1:
			info[heading[i]] = body[i]
	print(info)

def Discussions(source):
	# link = subject.find_all(href=True)
	#         	for i in link:
	#         		subjectList[text]['link']=i['href']
	#         		subjectList[text]['code']=str(i['href'])[-6:]
	print("DISCUSSIONS")
	discussion = {}

	table = source.find_all('table', {'class':"table table-striped"})
	for d in table:
		name = d.find_all('img', {'class':'img-circle'})
		count = 1
		for i in name:
			discussion[count] = {}
			discussion[count]['name'] = i['title']
			count+=1

		count=1
		questions = dfind_all('td', {'class':"table-question"})
		for i in questions:
			question = i.text.replace("  ", "")
			question = question.replace("\n", "")
			question = question.replace("\t", "")
			discussion[count]['question'] = question
			count+=1

		count=1
		responses = d.find_all('td', {'class':"table-activity"})
		for i in responses:
			discussion[count]['response'] = i.text
			count+=1

		count=1
		time = d.find_all('abbr', {'class':"timeago"})
		for i in time:
			discussion[count]['time'] = i.text
			count+=1
	count = 0
	for i in discussion:
		if "New" in discussion[i]['question'][-4:]:
			discussion[i]['question'] = discussion[i]['question'][:-3]
			count+=1

	if count == 0:
		speak("you do not have any new discussion")
		speak("Do you want to view the top 5 discussions")
	elif count == 1:
		speak("you have "+str(count)+" new discussion")
		speak("Do you want to view the discussion")
	else:
		speak("you have "+str(count)+" new discussions")
		speak("Do you want to view the discussions")

	choice = input("enter choice: ")
	if choice == "yes" and count!=0:
		for i in range(1, count+1):
			print(discussion[i])
	elif choice == "yes" and count==0:
		for i in range(1, 6):
			print(discussion[i])
	else:
		speak("thanks for visiting")



def Students(source):
	print("STUDENTS")
	students = source.find_all("h4")
	number = students[0].text
	speak("There are "+number)

email = 'madhur16053@iiitd.ac.in'
password = 'ngyuxana23'

# email = 'mudit16057@iiitd.ac.in'
# password = 'muditGarg@112'


if __name__=="__main__":
	login()
