##!usr/bin/env python3
#-*- coding : utf8 -*-

import re

##############################################################
# Fonction : list_from_outside_text_content
# Input : text
# Return : list
##############################################################
def list_from_outside_text_content(text):
    ''' Import a text as one list '''

    liste_brute = []
    liste_finale = []

    with open(text, 'r') as file :
        liste_brute = file.readlines()
        #list of all lines (from beg to EOL)

    for string in liste_brute :
        liste_finale.append(string.strip())

    return liste_finale

##############################################################
# Fonction : list_maj_to_min
# 	- Transforme toutes les majuscules en minuscules
# Input :
##############################################################
def list_maj_to_min(liste_in):

    list_out = []
    list_out = liste_in.lower()

    return list_out


##############################################################
# Fonction : punctuation_out
# 	- Transforme tous les caracteres de ponctuation en espace
# Input :
##############################################################
# def punctuation_out(list_in):
# 	list_out = []
#
# 	for word in list_in :
# 		list_out.append(word.)
#     pass

# If car in liste_car_banni
# Le transfo en espace

# txt = open(f)
# txt = txt.read()
# txt = re.sub(r'[^\w\s]','',txt)
# body = txt.lower().split()


##############################################################
# Fonction : convert_utf8
# 	- Convertit chaque caracteres en utf8
# Input :
##############################################################
def convert_utf8():
    pass

# Caractere par car


##############################################################
# Fonction : space_before_point
# 	- Transforme tous les lettre+'.' en lettre+'espace'+'point'
# Input :
##############################################################
def space_before_point(text):
    pass

##############################################################
# Fonction : tokenizeit
# 	- Nettoie le texte pour ne laisser que des tokens
# Input : texte
# Return : liste de mot
##############################################################
def tokenizeit():
    pass

# avec split
# pb du '- '
