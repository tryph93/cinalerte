#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lib_cinalertes.py
#  
#  Copyright 2019 Martin <Martin@DESKTOP-BE8BRBJ>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


#  
#  Menu imports
#  Notes : j'ai séparé l'ajout de personnes d'une part et l'ajout de films d'autre part, ça rend les choses plus claires
# Je sais plus vraiment ce qui marche et ce qui marche pas :') Je regarderai mieux ce week-end

# fct globales

# I-1 : fbool
def fbool(question, strvar='var'): #éval pertinence de garder la seconde variable de la fct / de garder la structure dict avec global dictbool
	global dictbool
	dictbool = dict()
	while True:
		var = input(question)
		var = var.replace(' ','')
		var = var.replace('Non','N')
		var = var.replace('non','N')
		var = var.replace('n','N')
		var = var.replace('Oui','O')
		var = var.replace('oui','O')
		var = var.replace('o','O')
		var = var.replace('0','O')
		if var=='O':
			dictbool[strvar] = 1
			break
		elif var=='N':
			dictbool[strvar] = 0
			break
		else:
			print('Veuillez répondre par oui (O) ou par non (N).\n')
	return dictbool[strvar]
	
# I-2 : usascii

def usascii(s):
	s = s.lower()
	s = s.replace(' ','+')
	s = s.replace('ç','c')
	s = s.replace('é','e')
	s = s.replace('ê','e')
	s = s.replace('è','e')
	s = s.replace('à','a')
	s = s.replace('â','a')
	s = s.replace('ã','a')
	s = s.replace('ô','o')
	s = s.replace('î','i')
	s = s.replace('ì','i')
	s = s.replace('ò','o')
	s = s.replace('õ','o')
	s = s.replace('ù','u')
	s = s.replace('û','u')
	s = s.replace('ä','a')
	s = s.replace('ë','e')
	s = s.replace('ï','i')
	s = s.replace('ö','o')
	s = s.replace('ü','u')
	s = s.replace('ÿ','y')
	s = s.replace('á','a')
	s = s.replace('í','i')
	s = s.replace('ó','o')
	s = s.replace('ú','u')
	s = s.replace('œ','oe')
	s = s.replace('æ','ae')
	return s
	
# I-3 : rreplace

def rreplace(s, old, new, occurrence):
	li = s.rsplit(old, occurrence)
	return new.join(li)
	
# I-4 : normlist

def normlist():
	
	import liste_films
	liste_1 = liste_films.liste
	
	import liste_personnes
	liste_2 = liste_personnes.liste

	nouvelle_liste = '''#!/usr/bin/python
# -*- coding: latin-1 -*-

liste = '''
	
	for i in range(len(liste_2)) :
		personne = liste_2[i][0]
		liste_3 = importlib.import_module(personne).liste
		liste_3_nouvelle = open(personne+'.py','w')
		
		for j in range(len(liste_3)) :
			try:
				liste_3[j].pop(3)
				liste_3[j].pop(2)
			except:
				continue
	
		liste_3_nouvelle.write(nouvelle_liste+str(liste_3))
		liste_3_nouvelle.close()
		
			
	for k in range(len(liste_1)) :
		try:
			liste_1[j].pop(3)
			liste_1[j].pop(2)
		except:
			continue
		
	liste_1_nouvelle = open('liste_films.py','w')
	liste_1_nouvelle.write(nouvelle_liste+str(liste_1))
	liste_1_nouvelle.close()
	
# fct menu

#II-1 consultation

def consultation(profil=None):
	import urllib3
	import lxml
	from bs4 import BeautifulSoup
		
	manager = urllib3.PoolManager()
	
	try:
		if profil==None:
			profil = input('Nom du profil ? : ')
	except:
		profil = input('Nom du profil ? : ')
		
	import liste_films
	liste_1 = liste_films.liste
	
	import liste_personnes
	liste_2 = liste_personnes.liste

	print('Consultation des films que vous avez dans votre base de donnée.')
	
	a=1
	for i in range(len(liste_2)) :
		print('\nFilms de/avec '+liste_2[i][1]+' :')
		liste_3 = importlib.import_module(liste_2[i][0]).liste
		for j in range(len(liste_3)) :
			print(str(a)+' - '+liste_3[j][1])
			a+=1
	
	print('\nAutres films :')
	for k in range(len(liste_1)) :
		print('\n'+str(a)+' - '+liste_1[k][1])
		a+=1
		
	print('\nNous sommes arrivés au bout de vos '+str(a-1)+' films. Quelle collection !')
	

# II-2 configuration globale
def configuration():

	import urllib3
	import bs4
	from bs4 import BeautifulSoup
	import lxml
	import re
	import os
	import importlib

	manager = urllib3.PoolManager()

	s_liste_films_personne = '''#!/usr/bin/python
# -*- coding: latin-1 -*-
liste=[]'''

	try:
		if profil==None:
			profil = input('Nom du profil ? : ')
	except:
		profil = input('Nom du profil ? : ')
	
	while True:
		while True:
			query = usascii(input('Recherche titre, réalisateur, acteur... : '))
			
			url = 'http://www.allocine.fr/recherche/?q='+query
			ressource = manager.request('GET', url)
			contenu = ressource.data
			soupe = BeautifulSoup(contenu, 'html.parser')
			page = soupe.find_all('div', {'style':'margin-top:-5px;'})
			
			if len(page)!=0:
				break
			else:
				print('Aucun résultat.\n')
				
		a = 0
		c = 0 #un peu inutile en fait... puisque c'est la même condition que else juste au dessus
		
		for unité in page:
		
			c+=1
			str_unité = str(unité)
			lien_film = re.findall('\/film\/.+?\.html',str_unité)
			lien_personne = re.findall('\/personne\/.+?\.html',str_unité)
			
			if len(lien_film)==0:
				if len(lien_personne)==0:
					continue
					
				else:
					type_lien=2
					type_lien_s = 'PERSONNE -'
					lien=lien_personne[0]
			else:
				type_lien=1
				type_lien_s = 'FILM -'
				lien=lien_film[0]
				
			id_lien = re.findall('\d+',lien)[0]
			
			info_film = unité.text
			info_film = info_film.replace('\n\n\n\n\n',' ') #à améliorer?
			info_film = info_film.replace('\n\n\n\n',' ')
			info_film = info_film.replace('\n\n\n',' ')
			info_film = info_film.replace('\n\n',' ')
			info_film = info_film.replace('\n',' ')
			info_film = info_film.replace('  ',' ')
			print('\n'+type_lien_s+info_film)
			
			info_film = info_film.replace('\'',' ')
			info_film = info_film.replace('"',' ') 
			#quand on voudra remplacer les dossiers dans chaque profil par un code un peu plus explicite (ex: num_id + nom)
			
			if fbool('Sélectionner ? (O/N) : ','selectionner')==1:
				
				a +=1
				if type_lien==1:
					try:
						py_liste_films = open(profil+'\\liste_films.py','r')
					except:
						py_liste_films = open('liste_films.py','r')
						
					texte_films=py_liste_films.read()
					texte_films=rreplace(texte_films, ']', '', 1)
					py_liste_films.close()
					try:
						py_liste_films = open(profil+'\\liste_films.py','w+')
					except:
						py_liste_films = open('liste_films.py','w+')
					total_films = texte_films+'[\''+id_lien+'\',\''+info_film+'\']]'
					total_films = total_films.replace('][','],[')
					py_liste_films.write(total_films)
					py_liste_films.close()
					
				else:
					try:
						py_liste_personnes = open(profil+'\\liste_personnes.py','r')
					except:
						py_liste_personnes = open('liste_personnes.py','r')
					texte_personnes=py_liste_personnes.read()
					texte_personnes=rreplace(texte_personnes, ']', '', 1)
					py_liste_personnes.close()
					try:
						py_liste_personnes = open(profil+'\\liste_personnes.py','w+')
					except:
						py_liste_personnes = open('liste_personnes.py','w+')
		
					total_personnes = texte_personnes+'[\''+id_lien+'\',\''+info_film+'\']]'
					total_personnes = total_personnes.replace('][','],[')
					py_liste_personnes.write(total_personnes)
					
					py_liste_personnes.close()
					
					prefixe = 'http://www.allocine.fr/personne/fichepersonne-'
					suffixe = '/filmographie/'
					
					url2 = prefixe+id_lien+suffixe
					
					ressource2 = manager.request('GET', url2)
					contenu2 = ressource2.data
					soupe2 = BeautifulSoup(contenu2, 'html.parser')
					
					try:
						py_liste_films_personne = open(profil+'\\'+id_lien+'.py','w+')
						
					except:
						try:
							
							py_liste_films_personne = open(id_lien+'.py','w+')
						except:
							print('ce réalisateur est déjà présent dans la base de donnée.') #vérifier que ça arrive vraiment, ce genre de cas.
					
					py_liste_films_personne.write(s_liste_films_personne)
					py_liste_films_personne.close()
					
					liens = soupe2.find_all('td', {'data-heading' :'Titre'})
					
					for i in range(len(liens)):
						espace_lien = liens[i].find_all('a')
					
						try:
							lien_add_personne = espace_lien[0].get('href')	
							lien_add_personne = re.findall('/film/fichefilm_gen_cfilm=\d+\.html',lien_add_personne)[0] #sinon ça prend les séries
						except:
							continue
							
						id_film_personne = re.findall('\d+',lien_add_personne)[0]
						info_film_personne = espace_lien[0].text
						info_film_personne = info_film_personne.replace('\'',' ')
						
						try:
							py_liste_films_personne = open(profil+'\\'+id_lien+'.py','r')
							
						except:
							py_liste_films_personne = open(id_lien+'.py','r')
							
						
						texte_films_personne = py_liste_films_personne.read()					
						texte_films_personne = rreplace(texte_films_personne, ']', '', 1)
						
						py_liste_films_personne.close()
						
						try:
							py_liste_films_personne = open(profil+'\\'+id_lien+'.py','w')
							
						except:
							py_liste_films_personne = open(id_lien+'.py','w')
						
						total_films_personne = texte_films_personne+'[\''+id_film_personne+'\',\''+info_film_personne+'\']]'
						
						total_films_personne = total_films_personne.replace('][','],[')

						py_liste_films_personne.write(total_films_personne)
						py_liste_films_personne.close()
						
#films peu					
		
					
					if len(liens)==0:
						url3 = 'http://www.allocine.fr/personne/fichepersonne_gen_cpersonne='+id_lien+'.html'
						ressource3 = manager.request('GET', url3)
						contenu3 = ressource3.data
						soupe3 = BeautifulSoup(contenu3, 'html.parser')
						liens_peu = soupe3.find_all('a', {'class' : 'meta-title meta-title-link'})
						
				
						for i in range(len(liens_peu)):
						
							try:	
								lien_add_personne = liens_peu[i].get('href') #pq i n'est pas tjrs bon ?
								lien_add_personne = re.findall('/film/fichefilm_gen_cfilm=\d+\.html',lien_add_personne)[0] #sinon ça prend les séries
							except:
								continue
							
							id_film_personne = re.findall('\d+', lien_add_personne)[0]
							
							info_film_personne = liens_peu[i].get('title')
							info_film_personne = info_film_personne.replace('\'',' ')
							
							try:
								py_liste_films_personne = open(profil+'\\'+id_lien+'.py','r')
							
							except:
								py_liste_films_personne = open(id_lien+'.py','r')
								
								
							texte_films_personne = py_liste_films_personne.read()						
							texte_films_personne = rreplace(texte_films_personne, ']', '', 1)
							
							py_liste_films_personne.close()
							
							try:
								py_liste_films_personne = open(profil+'\\'+id_lien+'.py','w') 
								
							except:
								py_liste_films_personne = open(id_lien+'.py','w')
								
							total_films_personne = texte_films_personne+'[\''+id_film_personne+'\',\''+info_film_personne+'\']]'
							total_films_personne = total_films_personne.replace('][','],[')
							
							py_liste_films_personne.write(total_films_personne)
							
							py_liste_films_personne.close()	
							
				interruption = 0			
				if fbool('Continuer avec la même requête ? (O/N) : ','continuer')==0:
					interruption = 1
					break
		
		
		print('\n')
			
		if c==0:
			print('Aucun résultat.\n')
			
		elif a==0 or interruption==0:
			print('Nous n\'avons plus de résultat à vous proposer.\n')
			
		if fbool('Recommencer avec une autre requête ? (O/N) : ','encore')==0:
			break
		print('\n')
			
	if fbool('Voulez-vous lancer la recherche pour les films et les personnes de votre sélection ? (O/N) : ','lancement')==1:
		print('\n')
		m_recherche = importlib.import_module('recherche_alertes_'+profil)
		m_recherche.recherche()
		
#II-2 configuration films
def conffilms():
	
	manager = urllib3.PoolManager()
	
	try:
		if profil==None:
			profil = input('Nom du profil ? : ')
	except:
		profil = input('Nom du profil ? : ')
	
	while True:
		while True:
			query = usascii(input('Recherche par titre, réalisateur, acteur... : '))
			
			url = 'http://www.allocine.fr/recherche/?q='+query
			ressource = manager.request('GET', url)
			contenu = ressource.data
			soupe = BeautifulSoup(contenu, 'html.parser')
			page = soupe.find_all('div', {'style':'margin-top:-5px;'})
			
			if len(page)!=0:
				break
			else:
				print('Aucun résultat.\n')
				
		a = 0
		c = 0 #un peu inutile en fait... puisque c'est la même condition que else juste au dessus
		
		for unité in page:
		
			c+=1
			str_unité = str(unité)
			lien_film = re.findall('\/film\/.+?\.html',str_unité)
			lien_personne = re.findall('\/personne\/.+?\.html',str_unité)
			if len(lien_film)==0:
				continue
			else:
				type_lien=1
				type_lien_s = 'FILM -'
				lien=lien_film[0]
				
			id_lien = re.findall('\d+',lien)[0]
			
			info_film = unité.text
			info_film = info_film.replace('\n\n\n\n\n',' ') #à améliorer?
			info_film = info_film.replace('\n\n\n\n',' ')
			info_film = info_film.replace('\n\n\n',' ')
			info_film = info_film.replace('\n\n',' ')
			info_film = info_film.replace('\n',' ')
			info_film = info_film.replace('  ',' ')
			print('\n'+type_lien_s+info_film)
			
			info_film = info_film.replace('\'',' ')
			info_film = info_film.replace('"',' ') 
			#quand on voudra remplacer les dossiers dans chaque profil par un code un peu plus explicite (ex: num_id + nom)
			
			if fbool('Sélectionner ? (O/N) : ','selectionner')==1:
				
				a +=1
			
				try:
					py_liste_films = open(profil+'\\liste_films.py','r')
				except:
					py_liste_films = open('liste_films.py','r')
					
				texte_films=py_liste_films.read()
				texte_films=rreplace(texte_films, ']', '', 1)
				py_liste_films.close()
				try:
					py_liste_films = open(profil+'\\liste_films.py','w+')
				except:
					py_liste_films = open('liste_films.py','w+')
				total_films = texte_films+'[\''+id_lien+'\',\''+info_film+'\']]'
				total_films = total_films.replace('][','],[')
				py_liste_films.write(total_films)
				py_liste_films.close()
					
							
				interruption = 0			
				if fbool('Continuer avec la même requête ? (O/N) : ','continuer')==0:
					interruption = 1
					break	
		
		print('\n')
			
		if c==0:
			print('Aucun résultat.\n')
			
		elif a==0 or interruption==0:
			print('Nous n\'avons plus de résultat à vous proposer.\n')
			
		if fbool('Recommencer avec une autre requête ? (O/N) : ','encore')==0:
			break
		print('\n')
		
#II-2(3)
def confartistes():

	manager = urllib3.PoolManager()
	
	try:
		if profil==None:
			profil = input('Nom du profil ? : ')
	except:
		profil = input('Nom du profil ? : ')

	s_liste_films_personne = '''#!/usr/bin/python
# -*- coding: latin-1 -*-
liste=[]'''
	
	while True:
		while True:
			query = usascii(input('ARTISTES - Recherche par nom'))
			url = 'http://www.allocine.fr/recherche/?q='+query
			ressource = manager.request('GET', url)
			contenu = ressource.data
			soupe = BeautifulSoup(contenu, 'html.parser')
			page = soupe.find_all('div', {'style':'margin-top:-5px;'})
			
			if len(page)!=0:
				break
			else:
				print('Aucun résultat.\n')
				
		a = 0
		c = 0 #un peu inutile en fait... puisque c'est la même condition que else juste au dessus
		
		for unité in page:
		
			c+=1
			str_unité = str(unité)
			lien_film = re.findall('\/film\/.+?\.html',str_unité)
			lien_personne = re.findall('\/personne\/.+?\.html',str_unité)
		
			if len(lien_personne)==0:
				continue
			else:
				type_lien=2
				type_lien_s = 'PERSONNE -'
				lien=lien_personne[0]
				
			id_lien = re.findall('\d+',lien)[0]
			
			info_film = unité.text
			info_film = info_film.replace('\n\n\n\n\n',' ') #à améliorer?
			info_film = info_film.replace('\n\n\n\n',' ')
			info_film = info_film.replace('\n\n\n',' ')
			info_film = info_film.replace('\n\n',' ')
			info_film = info_film.replace('\n',' ')
			info_film = info_film.replace('  ',' ')
			print('\n'+type_lien_s+info_film)
			
			info_film = info_film.replace('\'',' ')
			info_film = info_film.replace('"',' ') 
			#quand on voudra remplacer les dossiers dans chaque profil par un code un peu plus explicite (ex: num_id + nom)
			
			if fbool('Sélectionner ? (O/N) : ','selectionner')==1:
				
				a +=1

				try:
					py_liste_personnes = open(profil+'\\liste_personnes.py','r')
				except:
					py_liste_personnes = open('liste_personnes.py','r')
				texte_personnes=py_liste_personnes.read()
				texte_personnes=rreplace(texte_personnes, ']', '', 1)
				py_liste_personnes.close()
				try:
					py_liste_personnes = open(profil+'\\liste_personnes.py','w+')
				except:
					py_liste_personnes = open('liste_personnes.py','w+')
	
				total_personnes = texte_personnes+'[\''+id_lien+'\',\''+info_film+'\']]'
				total_personnes = total_personnes.replace('][','],[')
				py_liste_personnes.write(total_personnes)
				
				py_liste_personnes.close()
				
				prefixe = 'http://www.allocine.fr/personne/fichepersonne-'
				suffixe = '/filmographie/'
				
				url2 = prefixe+id_lien+suffixe
				
				ressource2 = manager.request('GET', url2)
				contenu2 = ressource2.data
				soupe2 = BeautifulSoup(contenu2, 'html.parser')
				
				try:
					py_liste_films_personne = open(profil+'\\'+id_lien+'.py','w+')
					
				except:
					try:
						
						py_liste_films_personne = open(id_lien+'.py','w+')
					except:
						print('ce réalisateur est déjà présent dans la base de donnée.') #vérifier que ça arrive vraiment, ce genre de cas.
				
				py_liste_films_personne.write(s_liste_films_personne)
				py_liste_films_personne.close()
				
				liens = soupe2.find_all('td', {'data-heading' :'Titre'})
				
				for i in range(len(liens)):
					espace_lien = liens[i].find_all('a')
				
					try:
						lien_add_personne = espace_lien[0].get('href')	
						lien_add_personne = re.findall('/film/fichefilm_gen_cfilm=\d+\.html',lien_add_personne)[0] #sinon ça prend les séries
					except:
						continue
						
					id_film_personne = re.findall('\d+',lien_add_personne)[0]
					info_film_personne = espace_lien[0].text
					info_film_personne = info_film_personne.replace('\'',' ')
					
					try:
						py_liste_films_personne = open(profil+'\\'+id_lien+'.py','r')
						
					except:
						py_liste_films_personne = open(id_lien+'.py','r')
						
					
					texte_films_personne = py_liste_films_personne.read()					
					texte_films_personne = rreplace(texte_films_personne, ']', '', 1)
					
					py_liste_films_personne.close()
					
					try:
						py_liste_films_personne = open(profil+'\\'+id_lien+'.py','w')
						
					except:
						py_liste_films_personne = open(id_lien+'.py','w')
					
					total_films_personne = texte_films_personne+'[\''+id_film_personne+'\',\''+info_film_personne+'\']]'
					
					total_films_personne = total_films_personne.replace('][','],[')

					py_liste_films_personne.write(total_films_personne)
					py_liste_films_personne.close()
					
#films peu					
	
				
				if len(liens)==0:
					url3 = 'http://www.allocine.fr/personne/fichepersonne_gen_cpersonne='+id_lien+'.html'
					ressource3 = manager.request('GET', url3)
					contenu3 = ressource3.data
					soupe3 = BeautifulSoup(contenu3, 'html.parser')
					liens_peu = soupe3.find_all('a', {'class' : 'meta-title meta-title-link'})
					
			
					for i in range(len(liens_peu)):
					
						try:	
							lien_add_personne = liens_peu[i].get('href') #pq i n'est pas tjrs bon ?
							lien_add_personne = re.findall('/film/fichefilm_gen_cfilm=\d+\.html',lien_add_personne)[0] #sinon ça prend les séries
						except:
							continue
						
						id_film_personne = re.findall('\d+', lien_add_personne)[0]
						
						info_film_personne = liens_peu[i].get('title')
						info_film_personne = info_film_personne.replace('\'',' ')
						
						try:
							py_liste_films_personne = open(profil+'\\'+id_lien+'.py','r')
						
						except:
							py_liste_films_personne = open(id_lien+'.py','r')
							
							
						texte_films_personne = py_liste_films_personne.read()						
						texte_films_personne = rreplace(texte_films_personne, ']', '', 1)
						
						py_liste_films_personne.close()
						
						try:
							py_liste_films_personne = open(profil+'\\'+id_lien+'.py','w') 
							
						except:
							py_liste_films_personne = open(id_lien+'.py','w')
							
						total_films_personne = texte_films_personne+'[\''+id_film_personne+'\',\''+info_film_personne+'\']]'
						total_films_personne = total_films_personne.replace('][','],[')
						
						py_liste_films_personne.write(total_films_personne)
						
						py_liste_films_personne.close()	
							
				interruption = 0			
				if fbool('Continuer avec la même requête ? (O/N) : ','continuer')==0:
					interruption = 1
					break
		
		
		print('\n')
			
		if c==0:
			print('Aucun résultat.\n')
			
		elif a==0 or interruption==0:
			print('Nous n\'avons plus de résultat à vous proposer.\n')
			
		if fbool('Recommencer avec une autre requête ? (O/N) : ','encore')==0:
			break
		print('\n')

#II-4 recherche
def recherche():
	
	try:
		if profil==None:
			profil = input('Nom du profil ? : ')
	except:
		profil = input('Nom du profil ? : ')
		
	manager = urllib3.PoolManager()
	profil = '03091433'

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


# II - 5 localisation 

def localisation():
	import urllib3
	from bs4 import BeautifulSoup
	import lxml
	import re
	
	manager = urllib3.PoolManager()
	
	s_city = input('Entrez la ville pour laquelle vous voulez configurer vos alertes : ')
	s_city = usascii(s_city)
	s_city = s_city.replace(' ','+')
	
	l_city = 'http://www.allocine.fr/recherche/4/?q='+s_city

	ressource = manager.request('GET', l_city)
	contenu = ressource.data
	soupe = BeautifulSoup(contenu, 'html.parser')
	unite = soupe.find_all('p', {'class' :'purehtml'})
	
	check_city = 0
	
	for i in range(len(unite)):
		ville = unite[i].text
		ville = ville.replace('\n',' ')
		print(ville)
		if fbool('Sélectionner ? (O/N) : ')==1:
			check_city += 1
			
			c_l_city_1 = re.findall('\d+', str(unite[i]))
			c_l_city = c_l_city_1[0]
			
			print('\nLes alertes sont désormais réglées sur les séances à et autour de '+ville+'.')
			print('\nRetour au menu principal.')
			
			
		
			break
			#nécessité de l'écrire dans un fichier. 
	if len(unite)==0:
		print('Votre requête n\'aboutit nulle part.')	
	
	elif check_city == 0:
		print('Nous sommes arrivés au bout des villes que nous avions à vous proposer.')
		print('Si vous êtes sûr de votre requête, essayez d\'ajouter le code postal !')
	
#II-6 supprfilm

def supprfilm():
	
	manager = urllib3.PoolManager()
	
	try:
		if profil==None:
			profil = input('Nom du profil ? : ')
	except:
		profil = input('Nom du profil ? : ')
		
	print('\n\nMenu - Supprimer des Films\n\n')
	
	import liste_films
	liste_1 = liste_films.liste
	
	import liste_personnes
	liste_2 = liste_personnes.liste
	
	liste_total=list()
	
	a=0
	for i in range(len(liste_2)) : #i0->len(liste_2)-1
		personne = liste_2[i][0]
		liste_3 = importlib.import_module(personne).liste
		print('\nFilms de/avec '+liste_2[i][1]+' : \n')
		b=0
		for j in range(len(liste_3)) : #j0->len(liste_3)-1
			a+=1
			b+=1
			liste_3[j].append(personne)
			liste_3[j].append(b)
			liste_total.append(liste_3[j])

			print(str(a)+' - '+liste_3[j][1])
			
	#a0->n1
			
	b=0
	print('\n Films ajoutés à votre liste de manière indépendante : \n')
	for k in range(len(liste_1)) : #k0->len(liste_1)-1
		a+=1
		b+=1
		print('\n'+str(a)+' - '+liste_1[k][1])
		liste_1[k].append('liste_films')
		liste_1[k].append(b)
		liste_total.append(liste_1[k])
		
	#an1->n2
	#liste_total n2 éléments ((i,j)+k, 4arg) liste_total[0]->64
		
	print('\nNous sommes arrivés au bout de vos '+str(a)+' films.')
	
	liste_suppr = list()
	
	while True:
		choix_suppr = input('Quel film souhaitez-vous enlever de votre liste ? (1-'+str(a)+' + 0 : revenir au menu) : ')
		
		if choix_suppr=='0':
			print('\nRetour au menu.\n\n')
			break
		
		try:
			int_choix_suppr = int(choix_suppr)
			entrée_suppr = liste_total[int_choix_suppr-1]
		except:
			print('Votre choix n\'est pas reconnu.')
			continue
			
		if int_choix_suppr in liste_suppr:
			print('Vous avez déjà sélectionné ce film')
			
		
		if fbool('Êtes-vous sûr de vouloir supprimer '+liste_total[int_choix_suppr-1][1]+' ? (O/N) : ')==0:
			print('\nRetour au menu.\n\n')
			break

		#int_choix_suppr 1->65
		while True:
			
			liste_tous_id_multiiple = list()
			liste_suppr.append(int_choix_suppr-1)
		
			test_id_multiple = liste_total[int_choix_suppr-1][0]

			liste_id_multiple = list()
			
			c=0
			
			#liste_suppr élé ds 0->64
			
			for l in liste_total:
				#64 différents l
				
				if l[0]==test_id_multiple:
					liste_id_multiple.append(c)	
					#liste_id_multiple élé ds 0->64
					
				c+=1
					
			if len(liste_id_multiple)>1:
				if fbool('Ce film apparaît plusieurs fois dans votre liste. Voulez-vous supprimer toutes les occurences ? (O/N) : ')==1:
					for m in liste_id_multiple:
						
						if m not in liste_suppr:
							liste_suppr.append(m)
							#m : certains numéros entre 0 et 64
				
			break
			
		if fbool('Voulez-vous supprimer un autre film ? (O/N) : ')==0:
			print('Retour au menu.') #qui n'existe pas encore
			break
	
	liste_suppr.sort(reverse=True)
	for n in liste_suppr:
		
		doc_incriminé = liste_total[n][2]
		num_incriminé = liste_total[n][3]
		
		liste_incriminée = importlib.import_module(doc_incriminé).liste
		
		
		liste_incriminée.pop(num_incriminé-1)
		
		nouvelle_liste = '''#!/usr/bin/python
# -*- coding: latin-1 -*-

liste = '''+str(liste_incriminée)
	
		py_ouvert = open(doc_incriminé+'.py','w+')
		py_ouvert.write(nouvelle_liste)
		py_ouvert.close()
		

#II-7
def supprpers():
	
	manager = urllib3.PoolManager()
	
	try:
		if profil==None:
			profil = input('Nom du profil ? : ')
	except:
		profil = input('Nom du profil ? : ')
	print('\n\nMenu - Supprimer des Personnes\n\n')
	
	import liste_personnes
	liste = liste_personnes.liste
	

	
	a=0
	print('\n Personnes de votre liste : \n')
	for i in range(len(liste_2)) : #i0->len(liste_2)-1
		personne = liste_2[i][0]
		liste[i].append(personne)
		liste[i].append(a)
		a+=1
	
		
	print('\nNous sommes arrivés au bout de vos '+str(a)+' artistes.')
	
	liste_suppr = list()
	
	while True:
		choix_suppr = input('Quel artiste souhaitez-vous enlever de votre liste ? (1-'+str(a)+' + 0 : revenir au menu) : ')
		
		if choix_suppr=='0':
			print('\nRetour au menu.\n\n')
			break
		
		try:
			int_choix_suppr = int(choix_suppr)
			entrée_suppr = liste[int_choix_suppr-1]
		except:
			print('Votre choix n\'est pas reconnu.')
			continue
			
		if int_choix_suppr in liste_suppr:
			print('Vous avez déjà sélectionné cette personne')
			
		
		if fbool('Êtes-vous sûr de vouloir supprimer '+liste[int_choix_suppr-1][1]+' ? (O/N) : ')==0:
			print('\nRetour au menu.\n\n')
			break

		#int_choix_suppr 1->65
		while True:
			
			liste_tous_id_multiiple = list()
			liste_suppr.append(int_choix_suppr-1)
		
			test_id_multiple = liste[int_choix_suppr-1][0]

			liste_id_multiple = list()
			
			c=0
			
			#liste_suppr élé ds 0->64
			
			for l in liste:
				#64 différents l
				
				if l[0]==test_id_multiple:
					liste_id_multiple.append(c)	
					#liste_id_multiple élé ds 0->64
					
				c+=1
					
			if len(liste_id_multiple)>1:
				if fbool('Ce film apparaît plusieurs fois dans votre liste. Voulez-vous supprimer toutes les occurences ? (O/N) : ')==1:
					for m in liste_id_multiple:
						
						if m not in liste_suppr:
							liste_suppr.append(m)
							#m : certains numéros entre 0 et 64
			break
			
		if fbool('Voulez-vous supprimer un autre film ? (O/N) : ')==0:
			print('Retour au menu.') #qui n'existe pas encore
			break
	
	liste_suppr.sort(reverse=True)
	for n in liste_suppr:
		
		doc_incriminé = liste[n][2]
		num_incriminé = liste[n][3]
		
		liste_incriminée = importlib.import_module(doc_incriminé).liste

		liste_incriminée.pop(num_incriminé-1)
		
		nouvelle_liste = '''#!/usr/bin/python
# -*- coding: latin-1 -*-

liste = '''+str(liste_incriminée)
	
		py_ouvert = open(doc_incriminé+'.py','w+')
		py_ouvert.write(nouvelle_liste)
		py_ouvert.close()

#3 - 1 création profil 
def creaprofil():
	profil = input('Entrez le nom du profil que vous voulez créer : ')
	
	try:
		py_configuration_alertes = open(profil+'\\configuration_alertes_'+profil+'.py','r')
		py_configuration_alertes.close()
		try:
			os.mkdir(profil)
			check_profil = 1			
		except:
			print('\nLe profil ne peut pas comporter les caractères suivants " < > | : ? * / \ . Choisissez un autre nom.\n')
	except:
		print('\nCe profil existe déjà.')
		
		
	
		
	
