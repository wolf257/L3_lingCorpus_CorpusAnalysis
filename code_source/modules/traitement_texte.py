#!/usr/bin/env python3
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
#TEST written
def list_maj_to_min_from_list(liste_in):
    ''' Reecrit tous les elts de la liste en minuscules '''

    list_out = []

    for elt in liste_in :
        list_out.append(elt.lower())

    return list_out

##############################################################
# Fonction : punctuation_sep
# 	- Separer les signe de ponctuation s'ils sont colles au mot
# Input :
##############################################################
#Test written
def list_punctuation_sep_from_list(list_in):
    ''' separate punctuation from word in list '''

    list_out = []

    for elt in list_in :
        mot = re.findall(r"[\w']+|[.,!?;]" , elt)
        list_out.append(mot)
        #will give a nested list

    #flat list
    list_out = [item for items in list_out for item in items]

    return list_out
##############################################################
# Fonction : punctuation_out
# 	- Transforme tous les caracteres de ponctuation en espace
# Input :
##############################################################
# def list_punctuation_out_from_list(list_in):
#     list_out = []
#
#     for elt in list_in :
#         mot = re.findall(r"[\w']+|[.,!?;]" , elt)
#         list_out.append(mot)
#         #will give a nested list
#
#     #flaten the list
#     list_out = [item for items in list_out for item in items]
#
# 	return list_out
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



if __name__ == '__main__':
    pass
