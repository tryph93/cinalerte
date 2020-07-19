#!/usr/bin/python
# -*- coding: latin-1 -*-

import urllib3
import bs4
from bs4 import BeautifulSoup
import lxml
import re
import os
import importlib

def rreplace(s, old, new, occurrence):
	li = s.rsplit(old, occurrence)
	return new.join(li)

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
	
	
def fbool(question, strvar='var'):
	global dictbool
	dictbool=dict()
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

manager = urllib3.PoolManager()
profil='jackson'
	
def configuration():

	s_liste_films_personne = '''#!/usr/bin/python
# -*- coding: latin-1 -*-
liste=[]'''
	
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
			
if __name__=='__main__':
	extension = ''
	configuration()
	fermeture = input('Appuyez sur Entrée pour fermer la fenêtre.')