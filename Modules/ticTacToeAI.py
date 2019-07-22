from time import *
from random import randint as randi
from random import uniform as randu
import speechRecAI
from textToSpeechAI import speak
import time
from random import randint
import mirror

send = mirror.send

def draw():
	if not win():
		if a[1]!=None and a[2]!=None and a[3]!=None and a[4]!=None and a[5]!=None and a[6]!=None and a[7]!=None and a[8]!=None and a[9]!=None:
			return True
		else:
			return False

def dictionary(x,y,i,chance):
	p=directionx(x[i])
	q=directiony(x[i])
	if q==8:
		if p==-8:
			a[1]=chance
		elif p==0 :
			a[2]=chance
		elif p==8:
			a[3]=chance
	elif q==0:
		if p==-8:
			a[4]=chance
		elif p==0 :
			a[5]=chance
		elif p==8:
			a[6]=chance
	elif q==-8:
		if p==-8:
			a[7]=chance
		elif p==0 :
			a[8]=chance
		elif p==8:
			a[9]=chance

def matrix():
	l = [[0 for x in range(3)] for y in range(3)]
	l[0][0]=a[1]
	l[0][1]=a[2]
	l[0][2]=a[3]
	l[1][0]=a[4]
	l[1][1]=a[5]
	l[1][2]=a[6]
	l[2][0]=a[7]
	l[2][1]=a[8]
	l[2][2]=a[9]
	return l

def win():
	l=matrix()
	if l[0][0]==l[0][1] and l[0][1]==l[0][2] and l[0][0]!=None:
		ctr=1
		return (ctr,l[0][0])
	if l[1][0]==l[1][1] and l[1][1]==l[1][2] and l[1][0]!=None:
		ctr=2
		return (ctr,l[1][0])
	if l[2][0]==l[2][1] and l[2][1]==l[2][2] and l[2][0]!=None:
		ctr=3
		return (ctr,l[2][0])
	if l[0][0]==l[1][0] and l[0][0]==l[2][0] and l[0][0]!=None:
		ctr=4
		return (ctr,l[0][0])
	if l[0][1]==l[1][1] and l[1][1]==l[2][1] and l[0][1]!=None:
		ctr=5
		return (ctr,l[0][1])
	if l[0][2]==l[1][2] and l[0][2]==l[2][2] and l[0][2]!=None:
		ctr=6
		return (ctr,l[1][2])
	if l[0][0]==l[1][1] and l[2][2]==l[1][1] and l[0][0]!=None:
		ctr=7
		return (ctr,l[1][1])
	if l[0][2]==l[1][1] and l[1][1]==l[2][0] and l[0][2]!=None:
		ctr=8
		return (ctr,l[1][1])
	else:
		return 0

def block(xi,yi):
	if xi==-8 and yi==8:
		return 1
	elif xi==0 and yi==8:
		return 2
	elif xi==8 and yi==8:
		return 3
	elif xi==-8 and yi==0:
		return 4
	elif xi==0 and yi==0:
		return 5
	elif xi==8 and yi==0:
		return 6
	elif xi==-8 and yi==-8:
		return 7
	elif xi==0 and yi==-8:
		return 8
	elif xi==8 and yi==-8:
		return 9

def start_game():

	click=(x[len(x)-1],y[len(y)-1])
	return click
	print(x,'\n',y)

def delete(x_):
	for i in range(len(x_)):
		x_.pop(i)

def directionx(turn):
	if "one" in turn or "1" in turn:
		return -8

	elif "two" in turn or "2" in turn:
		return 0

	elif "three" in turn or "3" in turn:
		return 8

	elif "four" in turn or "4" in turn:
		return -8

	elif "five" in turn or "5" in turn:
		return 0

	elif "six" in turn or "6" in turn or "sex" in turn:
		return 8

	elif "seven" in turn or "7" in turn:
		return -8

	elif "eight" in turn or "8" in turn:
		return 0

	elif "nine" in turn or "9" in turn:
		return 8
	else:
		return None

def directiony(turn):

	if "one" in turn or "1" in turn :
		return 8

	elif "two" in turn or "2" in turn :
		return 8

	elif "three" in turn or "3" in turn or "free" in turn:
		return 8

	elif "four" in turn or "4" in turn:
		return 0

	elif "five" in turn or "5" in turn:
		return 0

	elif "six" in turn or "6" in turn or "sex" in turn:
		return 0

	elif "seven" in turn or "7" in turn:
		return -8

	elif "eight" in turn or "8" in turn or "hate" in turn:
		return -8

	elif "nine" in turn or "9" in turn:
		return -8

def xo(x):
	if x == None:
		return ""
	else:
		return x.upper()

def computer(name):
	speech = ["Well Played", "That's a nice move", "Woah, you are a Genius", "How good is that move!", "I am impressed", "Are you a pro?", "That's intelligent", "Wait! i'll have to think a bit"]
	count=0
	print("          ",count)
	print("________________________")
	l=matrix()
	for i in range(3):
		print("|   ",end="")
		for j in range(3):
			if l[i][j]==None:
				print(" ",end="   |   ")
			else:
				print(l[i][j],end="   |   ")
		print(end="\n|_______|_______|_______|\n")
	print()
	toSend = []

	for i in range(3):
		for j in range(3):
			toSend.append(xo(l[i][j]))

	send({
		"type": "tic-tac-toe",
		"data": toSend 
	})

	while True:
		if win():
			m=win()
			player=m[1]
			if m[1]=="o":
				text = "Gotcha, I Win"
			else:
				text = "You are a legend. I feel proud that it took such genius to defeat me"
			# reset()
			speak(text)
			break;
		if draw():
			# reset()
			speak("nice playing with you, MATCH DRAWN")
			break;


		string=name['x']+" Say your Move"
		speak(string)
		record, audio = S.ears()
		turn = S.recognize(record,audio)
		#turn = input()
		turn =turn.lower()
		turn =turn.replace(" ","")
		x.append(turn)
		xi=directionx(x[count])
		while xi==None:
			speak("Say a legitimate move")
			record,audio = S.ears()
			turn = S.recognize(record,audio)
			#turn = input()
			turn =turn.lower()
			turn =turn.replace(" ","")
			x[count]=turn
			xi=directionx(turn)

		yi=directiony(x[count])
		current=block(xi,yi)
		while a[block(xi, yi)]=='x' or a[block(xi, yi)]=='o':
			speak("You Can't move at block "+str(block(xi, yi)))
			speak("choose another block")
			record,audio = S.ears()
			turn = S.recognize(record,audio)
			#turn = input()
			turn =turn.lower()
			turn =turn.replace(" ","")
			x[count]=turn
			xi=directionx(turn)
			yi=directiony(turn)
			current=block(xi, yi)

		if a[current]==None:
			dictionary(x,y,count,'x')
			#count+=
		count+=1
		print("          ",count)
		print("________________________")
		l=matrix()
		for i in range(3):
			print("|   ",end="")
			for j in range(3):
				if l[i][j]==None:
					print(" ",end="   |   ")
				else:
					print(l[i][j],end="   |   ")
			print(end="\n|_______|_______|_______|\n")
		print()

		toSend = []

		for i in range(3):
			for j in range(3):
				toSend.append(xo(l[i][j]))

		send({
			"type": "tic-tac-toe",
			"data": toSend 
		})

		if win():

			m=win()
			player=m[1]
			if m[1]=="o":
				text = "Gotcha, I Win"
			else:
				text = "You are a legend. i feel proud that it took such genius to defeat me"
			speak(text)
			# reset()
			break;
		if draw():
			# reset()
	
			speak("nice playing with you, MATCH DRAWN")
			break;

		speak(speech[randint(0, (len(speech)-1))])

		t=computer_turn(count,current)

		xi=t[0]
		yi=t[1]

		a[block(xi,yi)]='o'

		print("          ",count)
		print("________________________")
		l=matrix()
		for i in range(3):
			print("|   ",end="")
			for j in range(3):
				if l[i][j]==None:
					print(" ",end="   |   ")
				else:
					print(l[i][j],end="   |   ")
			print(end="\n|_______|_______|_______|\n")

		toSend = []

		for i in range(3):
			for j in range(3):
				toSend.append(xo(l[i][j]))

		send({
			"type": "tic-tac-toe",
			"data": toSend 
		})

		string = "I move at block "+str(block(xi,yi))
		speak(string)

		if win():
			m=win()
			player=m[1]

			if m[1]=="o":
				text = "Gotcha, I Win"
			else:
				text = "You are a legend. i feel proud that it took such genius to defeat me"
			speak(text)
			break;
		if draw():
			speak("nice playing with you, MATCH DRAWN")
			break;

def computer_turn(count,current):
	#print("current "+str(current))
	#print("count "+str(count))
	corner=[1,3,7,9]
	edge=[2,4,6,8]
	middle=[5]
	place=0
	if count==1:
		if current in (corner+(edge)):
			place=5
			a[5]='o'
			return coordinate(place)
		if not place :
			a[1]='o'
			return coordinate(1)

	if a[1]==a[9] and a[5]=='o' and a[1]=='x' and count==2:
		a[6]='o'
		return(coordinate(6))
	elif a[3]==a[7] and a[5]=='o' and a[3]=='x' and count==2:
		a[6]='o'
		return(coordinate(6))
	elif a[1]==a[8] and a[5]=='o' and a[1]=='x' and count==2:
		a[7]='o'
		return(coordinate(7))
	elif a[1]==a[6] and a[5]=='o' and a[1]=='x' and count==2:
		a[3]='o'
		return(coordinate(3))
	elif a[3]==a[8] and a[5]=='o' and a[3]=='x' and count==2:
		a[9]='o'
		return(coordinate(9))
	elif a[3]==a[4] and a[5]=='o' and a[3]=='x' and count==2:
		a[1]='o'
		return(coordinate(1))
	elif a[9]==a[2] and a[5]=='o' and a[2]=='x' and count==2:
		a[3]='o'
		return(coordinate(3))
	elif a[9]==a[4] and a[5]=='o' and a[4]=='x' and count==2:
		a[8]='o'
		return(coordinate(8))
	elif a[7]==a[2] and a[5]=='o' and a[2]=='x' and count==2:
		a[1]='o'
		return(coordinate(1))
	elif a[7]==a[6] and a[5]=='o' and a[6]=='x' and count==2:
		a[9]='o'
		return(coordinate(9))
	else:
		if a[1]==a[2] and a[1]=='o' and a[3]==None:
			a[3]='o'
			return(coordinate(3))
		elif a[1]==a[3] and a[1]=='o' and a[2]==None:
			a[2]='o'
			return(coordinate(2))
		elif a[2]==a[3] and a[2]=='o' and a[1]==None:
			a[1]='o'
			return(coordinate(1))
		elif a[4]==a[5] and a[4]=='o' and a[6]==None:
			a[6]='o'
			return(coordinate(6))
		elif a[4]==a[6] and a[6]=='o' and a[5]==None:
			a[5]='o'
			return(coordinate(5))
		elif a[5]==a[6] and a[6]=='o' and a[4]==None:
			a[4]='o'
			return(coordinate(4))
		elif a[7]==a[8] and a[7]=='o' and a[9]==None:
			a[9]='o'
			return(coordinate(9))
		elif a[7]==a[9] and a[9]=='o' and a[8]==None:
			a[8]='o'
			return(coordinate(8))
		elif a[8]==a[9] and a[9]=='o' and a[7]==None:
			a[7]='o'
			return(-8,-8)


		elif a[1]==a[4] and a[1]=='o' and a[7]==None:
			a[7]='o'
			return(-8,-8)
		elif a[1]==a[7] and a[1]=='o' and a[4]==None:
			a[4]='o'
			return(coordinate(4))
		elif a[4]==a[7] and a[4]=='o' and a[1]==None:
			a[1]='o'
			return(coordinate(1))
		elif a[2]==a[5] and a[5]=='o' and a[8]==None:
			a[8]='o'
			return(coordinate(8))
		elif a[2]==a[8] and a[2]=='o' and a[5]==None:
			a[5]='o'
			return(coordinate(5))
		elif a[5]==a[8] and a[5]=='o' and a[2]==None:
			a[2]='o'
			return(coordinate(2))
		elif a[3]==a[6] and a[3]=='o' and a[9]==None:
			a[9]='o'
			return(coordinate(9))
		elif a[3]==a[9] and a[9]=='o' and a[6]==None:
			a[6]='o'
			return(coordinate(6))
		elif a[6]==a[9] and a[9]=='o' and a[3]==None:
			a[3]='o'
			return(coordinate(3))


		elif a[1]==a[5] and a[5]=='o' and a[9]==None:
			a[9]='o'
			return(coordinate(9))
		elif a[1]==a[9] and a[1]=='o' and a[5]==None:
			a[5]='o'
			return(coordinate(5))
		elif a[5]==a[9] and a[5]=='o' and a[1]==None:
			a[1]='o'
			return(coordinate(1))


		elif a[3]==a[5] and a[5]=='o' and a[7]==None:
			a[7]='o'
			return(-8,-8)
		elif a[3]==a[7] and a[7]=='o' and a[5]==None:
			a[5]='o'
			return(coordinate(5))
		elif a[5]==a[7] and a[5]=='o' and a[3]==None:
			a[3]='o'
			return(coordinate(3))



		elif a[1]==a[2] and a[1]=='x' and a[3]==None:
			a[3]='o'
			return(coordinate(3))
		elif a[1]==a[3] and a[1]=='x' and a[2]==None:
			a[2]='o'
			return(coordinate(2))
		elif a[2]==a[3] and a[2]=='x' and a[1]==None:
			a[1]='o'
			return(coordinate(1))
		elif a[4]==a[5] and a[4]=='x' and a[6]==None:
			a[6]='o'
			return(coordinate(6))
		elif a[4]==a[6] and a[6]=='x' and a[5]==None:
			a[5]='o'
			return(coordinate(5))
		elif a[5]==a[6] and a[6]=='x' and a[4]==None:
			a[4]='o'
			return(coordinate(4))
		elif a[7]==a[8] and a[7]=='x' and a[9]==None:
			a[9]='o'
			return(coordinate(9))
		elif a[7]==a[9] and a[9]=='x' and a[8]==None:
			a[8]='o'
			return(coordinate(8))
		elif a[8]==a[9] and a[9]=='x' and a[7]==None:
			a[7]='o'
			return(-8,-8)


		elif a[1]==a[4] and a[1]=='x' and a[7]==None:
			a[7]='o'
			return(-8,-8)
		elif a[1]==a[7] and a[1]=='x' and a[4]==None:
			a[4]='o'
			return(coordinate(4))
		elif a[4]==a[7] and a[4]=='x' and a[1]==None:
			a[1]='o'
			return(coordinate(1))
		elif a[2]==a[5] and a[5]=='x' and a[8]==None:
			a[8]='o'
			return(coordinate(8))
		elif a[2]==a[8] and a[2]=='x' and a[5]==None:
			a[5]='o'
			return(coordinate(5))
		elif a[5]==a[8] and a[5]=='x' and a[2]==None:
			a[2]='o'
			return(coordinate(2))
		elif a[3]==a[6] and a[3]=='x' and a[9]==None:
			a[9]='o'
			return(coordinate(9))
		elif a[3]==a[9] and a[9]=='x' and a[6]==None:
			a[6]='o'
			return(coordinate(6))
		elif a[6]==a[9] and a[9]=='x' and a[3]==None:
			a[3]='o'
			return(coordinate(3))


		elif a[1]==a[5] and a[5]=='x' and a[9]==None:
			a[9]='o'
			return(coordinate(9))
		elif a[1]==a[9] and a[1]=='x' and a[5]==None:
			a[5]='o'
			return(coordinate(5))
		elif a[5]==a[9] and a[5]=='x' and a[1]==None:
			a[1]='o'
			return(coordinate(1))


		elif a[3]==a[5] and a[5]=='x' and a[7]==None:
			return(-8,-8)
			a[7]='o'
		elif a[3]==a[7] and a[7]=='x' and a[5]==None:
			return(coordinate(5))
			a[5]='o'
		elif a[5]==a[7] and a[5]=='x' and a[3]==None:
			return(coordinate(3))
			a[3]='o'
		else:
			for i in (middle + corner+edge):
				if a[i]==None:
					return coordinate(i)
					a[i]='o'
					break


def coordinate(block):
	if block==1:
		return (-8,8)
	elif block==2:
		return(0,8)
	elif block==3:
		return(8,8)
	elif block==4:
		return(-8,0)
	elif block==5:
		return(0,0)
	elif block==6:
		return(8,0)
	elif block==7:
		return(-8,-8)
	elif block==8:
		return(0,-8)
	elif block==9:
		return(8,-8)
#

#____________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________
S = speechRecAI.SpeechAI(0.55,True)
N = speechRecAI.SpeechAI(0.30)
def game() :
	name={'x': "Player",'o':"I"}
	string = "Player plays with  X"
	speak(string)
	speak("I play with O")
	computer(name)


#____________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________

x=[]
y=[]
a={1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None}
player=0

def reset():
	global x, y, a, player
	x=[]
	y=[]
	a={1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None}
	player=0

if __name__ == '__main__':
	game()
	reset()
	