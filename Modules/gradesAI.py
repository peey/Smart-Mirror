import requests
from lxml import html
from bs4 import BeautifulSoup
from speechRecAI import SpeechAI
from textToSpeechAI import speak

import mirror

def grade(userid, passwd):
    payload = {
        'appUser.userId':userid,
        'appUser.passwd':passwd,
    }

    session_requests = requests.session()

    login_url = "https://erp.iiitd.edu.in/login.action"
    result = session_requests.get(login_url)


    result = session_requests.post(
    	login_url,
    	data = payload,
    	headers = dict(referer=login_url)
    )
    r = session_requests.get("https://erp.iiitd.edu.in/termwiseGradeDetailsStudentPortal.action")
    soup = BeautifulSoup(r.content,'lxml')

    data = soup.find_all("table", {'class':"table table-bordered"})

    table_heading=[] # collection of headings of each table
    table_data=[] # contains data of all the tables

    for i in range(len(data)):
    	table = data[i]
    	individual_heading=[] #heading of each table
    	individual_data =  [] #contains data for the particular table
    	heading = table.find_all("thead")
    	body = table.find_all("tbody")
    	for field in heading:
    		field = field.find_all("th")
    		for x in field:
    			individual_heading.append(x.text)
    	table_heading.append(individual_heading)

    	for field in body:
    		row = field.find_all("tr")
    		individual_row=[]
    		for cell in row:
    			cell = cell.find_all("td")
    			indiviual_cell=[]
    			for x in cell:
    				indiviual_cell.append(x.text)
    			individual_row.append(indiviual_cell)
    		individual_data.append(individual_row)
    	table_data.append(individual_data)
    return [table_heading, table_data]

def gradesAI():
    a={}
    table = grade("madhur16053@iiitd.ac.in","ngyuxana23")
    LEL = 0
    total_courses = 0
    for i in range (len(table[1])):
        table_data = table[1][i]
        for j in table_data:
            for k in j:
                if len(k)>=4:
                    course = k[1]
                    g = str(k[4])
                    g = g.replace('-',' minus')
                    g = g.replace('+',' plus')
                    if not (g=="" and k[5]=='\xa0') :
                        a[course]={'GPA':k[5], 'grade':g}
                        LEL+=int(k[5])
                        total_courses+=1
                    else:
                        if 'not graded' not in a.keys():
                            a['not graded'] = []
                            a['not graded'].append(course)
                        else:
                            a['not graded'].append(course)
    print(a)
    mirror.send({
        "type": "grades",
        "grades": a
    })

    speak("your CGPA is "+str(LEL/total_courses))

if __name__=="__main__":
    gradesAI()
