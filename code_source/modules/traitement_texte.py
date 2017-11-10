#!usr/bin/python3
#-*- coding : utf8 -*-

import re

##############################################################
# Fonction : import text as one list
# 	-
# Input : text
# Return : list
##############################################################
def outside_text_as_one_list(text):
    ''' Import a text as one list '''

    liste_brute = []
    liste_finale = []

    #Importation du texte as one list.
    #Pb : les mots contiennent le '\n'.
    with open(text, 'r') as file :
        liste_brute = file.readlines()

    #Solution : a partir de cette liste, creer une nouvelle en enlever '\n'
    for word in liste_brute :
        liste_finale.append(word.strip())

    return liste_finale

##############################################################
# Fonction : punctuation_out
# 	- Transforme tous les caracteres de ponctuation en espace
# Input :
##############################################################
def punctuation_out(text):
    pass

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
# Fonction : maj_to_min
# 	- Transforme toutes les majuscules en minuscules
# Input :
##############################################################
def maj_to_min():
    pass

# Function qui transfo maj en min


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
