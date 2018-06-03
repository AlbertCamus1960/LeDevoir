#coding utf-8

import requests, csv
from bs4 import BeautifulSoup

ledevoir =  "ledevoir.csv"

entetes = {
	"User-Agent":"Philippe Léger",
	"From":"philippe.asselinleger@gmail.com"
}

for z in range(400000,525000):
	url1 = "http://m.ledevoir.com/article-{}".format(z)
	req = requests.get(url1, headers=entetes)
	page1 = BeautifulSoup(req.text,"html.parser")
	# cherche = page1.find_all("a")
	if req.status_code == 200:
		# print(url1, z)
		infos = page1.find("header", class_="text-dark").find_all("h1")

		for info in infos:
			try:
				titre = info.find("div", class_="col-xs-14 col-sm-11").h1.text

		autreinfos = page1.find("header", class_="text-dark").find_all("li")

		for autreinfo in autreinfos
			try:
				section = autreinfo.find("a").text
				soussection = autreinfo.find("a").text

		dauteurs = page1.find("div", class_="sans-photo").find_all(h3)

		for dauteur in dauteurs
			try:
				date = dauteur.find("a").text
				auteur = dauteur.find("time").text

		print(z, url1, section, soussection, date, auteur, titre)


# 	date = "div", class_="col-xs-14 col-md-10 col-md-offset-4".h3.text
# auteur = "div", class_="col-xs-14 col-md-10 col-md-offset-4".h3.text
# print(url1, cherche.find("div", class_="col-xs-14 col-md-10 col-md-offset-4".h3.text)

# print(cherche)
# print(z, url1)
	
# for c in cherche:
# 	a = c["href"]
# 	print(a)


# for z in range(400000,525000):
# 	url1 = "http://m.ledevoir.com/article-{}".format(z)
# 	req = requests.get(url1, headers=entetes)
# 	page1 = BeautifulSoup(req.text,"html.parser")
# 	cherche = page1.find_all(a)
# 	print(cherche)

# for z in range(400000,525000):
# 	url1 = "m.ledevoir.com/article-{}".format(z)
# 	req = requests.get(url1, headers=entetes)
# 	page1 = BeautifulSoup(req.text,"html.parser")
# 	cherche = page1.find_all()


# import json
# import requests
# entetes = {
# 	"User-Agent":"Philippe Léger",
# 	"From":"philippe.asselinleger@gmail.com"
