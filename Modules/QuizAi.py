import requests
from lxml import html
from bs4 import BeautifulSoup
from speechRecAI import SpeechAI
from textToSpeechAI import speak
from random import randint
from wikiAI import wiki
import wikipedia
def quiz():
	appreciation = ["Was it a guess?", "Well Played", "How do you do it?", "Bravo", "Awesome", "Genius", "Teach me master", "You Have a great G K"]
	incorrect = ["oops", "That was tough for me too", "Sorry, wrong answer", "You were close", "So close, Yet so far", "There are a few more to come"]
	S = SpeechAI()
	session_requests = requests.session()
	r = session_requests.get("http://www.knowledgepublisher.com/article-424.html")
	soup = BeautifulSoup(r.content,'lxml')
	data = soup.find_all("table", {'class':"body-text"})
	for i in range(len(data)):
		table = data[i]
		body = table.find_all("tbody")
		database=[]
		for row in body:
			row.find_all("tr")
			question = []
			for field in row:
				field = field.find_all("td")
				for i in field:
					question.append(i.text)
			database.append(question)

	questions=[]
	for i in range(0, len(question)-1, 3):
			questions.append(question[i:i+3])
	total_questions = len(questions)

	score = 0
	incorrect_answer = 0
	current_question = 1
	passed_questions = []
	var = 0
	while incorrect_answer <10:
		if var == 0:
			question_number = randint(0, total_questions-1)
		correct_answer=questions[question_number][2].lower()
		if question_number not in passed_questions:
			speak("question number "+ str(current_question))
			print(questions[question_number][1])
			speak(questions[question_number][1])
			# record,audio = S.ears()
			# answer = S.recognize(record,audio)
			answer = input("answer: ")
			answer = answer.lower()
			answer.replace(" ","")

			if "don'tknow" in answer or "pass" in answer or "nextquestion" in answer or "next" in answer or "dontknow" in answer:
				speak("the score is deducted by 5")
				score-=5
				print("the answer is "+correct_answer)
				speak("the answer is "+correct_answer)
				passed_questions.append(question_number)
				current_question+=1
				var = 0

			elif "score" in answer or "point" in answer:
				print("your score is "+str(score))
				speak("your score is "+str(score))
				var = 1

			elif "cancel" in answer or "abort" in answer:
				print("your score is "+str(score))
				speak("your score is "+str(score))
				speak("thanks for playing")
				break;
			elif "hint" in answer:
				to_speak = wiki(correct_answer)
				if to_speak!="":
					words = correct_answer.split()
					for i in words:
						to_speak = to_speak.replace(i, "*")
					print(to_speak+" ( The secret word has been replaced by '*') ")
					speak(to_speak)
				else:
					try:
						hint = wikipedia.summary(correct_answer, sentences=1)
						words = correct_answer.split()
						for i in words:
							hint = hint.replace(i, "*")
						print(hint+" ( The secret word has been replaced by '*') ")
						speak(hint)
					except:
						speak("sorry no hint available")
				var = 1
			elif "long" in answer or "length" in answer and "answer" in answer:
				speak("the answer has "+str(correct_answer.count(" ")+1)+" words")
				var = 1
			elif "sudo" in answer and "tell" in answer and "answer" in answer:
				print(correct_answer)
				speak("the answer is "+correct_answer)
				var = 1
			elif correct(questions[question_number], answer):
				print("Correct Answer")
				speak(appreciation[randint(0, (len(appreciation)-1))])
				score+=10
				passed_questions.append(question_number)
				current_question+=1
				var = 0
			else:
				print("Incorect Answer")
				speak(incorrect[randint(0, (len(incorrect)-1))])
				print("the answer is "+correct_answer)
				speak("the answer is "+correct_answer)
				incorrect_answer+=1
				passed_questions.append(question_number)
				current_question+=1
				var = 0



	if incorrect_answer==10:
		speak("well played. You scored"+str(score))

def correct(quetion, answer):
	correct_answer = quetion[2].lower()
	correct_answer = correct_answer.replace(" ", "")
	match=0
	not_match = 0
	for i in answer:
		if i in correct_answer:
			match+=1
	for i in correct_answer:
		if i not in answer:
			not_match+=1
	anwser_length = len(correct_answer)
	if match >= not_match:
		return True
	else:
		return False
if __name__=="__main__":
	speak("welcome to trivialis")
	quiz()
