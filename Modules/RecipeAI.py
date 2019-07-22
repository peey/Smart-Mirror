import requests
from bs4 import BeautifulSoup
import json

def recipe(item):
	
	session_requests = requests.session()
	item = item.replace(" ", "_")
	url = "http://food2fork.com/api/search?key=d93362eb59371ccdff0acc2a91882f5a&q="+item
	print(url)
	r = session_requests.get(url)
	recipes=r.json()
	number_of_recipes = recipes['count']
	all_recipes = recipes['recipes']
	for i in range(number_of_recipes):
		recipe = all_recipes[i]
		title = recipe['title']
		x = ingredients(recipe['f2f_url'])
		x = list(x)
		ingredient = x[0]
		nutrition = x[1] 
		ingredient = ingredient[6:]
		print(title, ingredient, nutrition)
		
	# soup = BeautifulSoup(r.content,'lxml')
	# data = soup.find_all("p")
	# for all_recipes in data:
	# 	print(all_recipes.text)

def ingredients(url):
	# print(url)
	session_requests = requests.session()
	r = session_requests.get(url)
	soup = BeautifulSoup(r.content,'lxml')
	ingredient = []
	data = soup.find_all("li")
	for i in data:
		ingredient.append(i.text)
	data = soup.find_all("table", {'class':'nutrition'})
	nutrition = {}
	for i in data:
		i = i.find_all("td")
		for j in i:
			t = ""
			ty = j.find_all("strong")
			for k in ty:
				t = k.text
			value = j
			value = value.text
			value = value.replace(t, "")
			value = value.replace(" ", "")

			nutrition[t] = value
			nutrition.pop('',None)
	return (ingredient, nutrition)	

if __name__=="__main__":
	item = input()
	recipe(item)