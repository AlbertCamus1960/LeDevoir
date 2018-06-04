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
	print(url1) ### Ajout
	req = requests.get(url1, headers=entetes)
	page1 = BeautifulSoup(req.text,"html.parser")
	print(req.status_code)
	# cherche = page1.find_all("a")
	if req.status_code == 200:
		# print(url1, z)
		# infos = page1.find("header", class_="text-dark").find_all("h1") ### find_all non nécessaire pcq un seul «h1»

		titre = page1.find("header", class_="text-dark").find("h1").text.strip() ### façon plus directe de trouver titre
		print(titre)

		### Autre méthode

		titre2 = page1.find("meta", attrs={"property":"og:title"})["content"]
		print(titre2)

		# for info in infos:
		# 	try:
		# 		titre = info.find("div", class_="col-xs-14 col-sm-11").h1.text
		# 	except: ### Ajout
		# 		titre = "Titre inconnu"

		autreinfos = page1.find("header", class_="text-dark").find_all("li") ### Ne fonctionne pas...
		# print(autreinfos)

		### Pour trouver section

		section = page1.find("div", class_="header-articles-carousel").find("span").text.strip()
		print(section)

		### Pour trouver sous-section

		soussection = page1.find("nav", class_="category-nav").text.strip()
		print(soussection)

		# for autreinfo in autreinfos: ### Manquait «:»
		# 	try:
		# 		section = autreinfo.find("a").text
		# 		soussection = autreinfo.find("a").text
		# 	except: ### Ajout
		# 		section = "Section inconnue"
		# 		soussection = "Sous-section inconnue"

		# dauteurs = page1.find("div", class_="sans-photo").find_all("h3") ### Manquait guillemets autour de h3
		dauteurs = page1.find("div", class_="author-offset").find_all("h3") ### Classe author-offset + pertinente
		# print(dauteurs)

		auteur = page1.find("div", class_="author-offset").find("h3").text.strip()
		print(auteur)

		date = page1.find("div", class_="author-offset").find("time").text.strip()
		print(date)

		# for dauteur in dauteurs: ### Manquait «:»
		# 	try:
		# 		date = dauteur.find("a").text
		# 		auteur = dauteur.find("time").text
		# 	except: ### Ajout
		# 		date = "Date inconnue"
		# 		auteur = "Auteur.e inconnu.e"

		url_reel = page1.find("meta", attrs={"property":"og:url"})["content"]
		print(url_reel)

		print(z, url_reel, section, soussection, date, auteur, titre)
		print("&"*50)

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
