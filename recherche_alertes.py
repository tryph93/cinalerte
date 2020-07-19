#!/usr/bin/python
# -*- coding: latin-1 -*-

import urllib3
import bs4
from bs4 import BeautifulSoup
import lxml
import re
import os
import importlib

def recherche():
	manager = urllib3.PoolManager()
	profil = 'jackson'

	import liste_films
	liste_1 = liste_films.liste
	
	import liste_personnes
	liste_2 = liste_personnes.liste
		
	interroge = 'www.allocine.fr/'

	id_film=list()
	noms_film=list()
			
	for u in range(len(liste_1)):
		id_film_u = liste_1[u][0]
		id_film.append(id_film_u)
		noms_film.append(liste_1[u][1])
		
	for v in range(len(liste_2)):
		id_personne=liste_2[v][0]
		m_personne = __import__(id_personne) 
		liste_3 = m_personne.liste
		for w in range(len(liste_3)):
			id_film_w = liste_3[w][0]
			if id_film_w not in id_film:
				id_film.append(id_film_w)
				noms_film.append(liste_3[w][1])

	z=0
	y=0
	
	print('Parmi les '+str(len(id_film))+' films de votre sélection, nous avons trouvé les séances suivantes : \n')

	for m in id_film :	
		try:
			existence_séance = 'seance/film-'+m+'/pres-de-115755/'

			url_interrogation = interroge+existence_séance

			ressource = manager.request('GET', url_interrogation)
			contenu = ressource.data
			soupe = BeautifulSoup(contenu, 'html.parser')
			unité = soupe.find_all('div', {'class' :'theater hred'})
			if len(unité)==0:
				y +=1
			for n in unité:
				nom_cinéma_html = n.find_all('a')
				nom_cinéma = nom_cinéma_html[0].text
				adresse_cinéma_html = n.find_all('address', {'class' :'address'})
				adresse_cinéma = adresse_cinéma_html[0].text
				positif = 'Des séances de '+noms_film[z]+' sont programmées au'+nom_cinéma+', situé '+adresse_cinéma+' !\n'
				print(positif)
		except:
			y +=1
		z +=1
	if len(id_film)==y:
		print('Aucune séance disponible pour votre sélection de films. Essayez d\'ajouter d\'autres films, d\'autres réalisateurs, ou encore d\'autres acteurs !')

if __name__=='__main__':
	recherche()
	fermeture = input('Appuyez sur Entrée pour fermer la fenêtre.')