#!/usr/bin/env python3
#-*- coding : utf8 -*-

import re
import string

#TODO : creer une phrase punctuation (avec ou sans point ?) en tant qu'objet re

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
def maj_to_min_list_from_list(liste_in):
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
def punctuation_sep_word_list_from_list(list_in):
    ''' separate punctuation from word in list
    >>> a = "j'ai joué... au basket.".split()
    >>> b = punctuation_sep_word_list_from_list(b)
    >>> b = ["j'ai" , 'joué' , '.' , '.' , '.' , 'au' , 'basket' , '.'] '''

    list_out = []
    word = ''

    for elt in list_in :
        word = re.findall(r"[\w']+|[.,!?;]" , elt)

        list_out.append(word) #will give a nested list

    #to make the list flat
    list_out = [item for items in list_out for item in items]

    return list_out

##############################################################
# Fonction : all_punctuation_out
# 	- Transforme tous les caracteres de ponctuation en espace
# Input :
##############################################################
#Test written
def all_punctuation_out_list_from_list(list_in) :
    ''' erase all punctuation from word in list
    >>> a = "j'ai joué... au basket 2 fois.".split()
    >>> b = punctuation_sep_word_list_from_list(b)
    >>> b = ["j'ai" , 'joué' , 'au' , 'basket' , '2' , 'fois' ] '''

    list_out = []
    word = ''

    for elt in list_in :
        word = re.findall(r"[\w']+" , elt)

        list_out.append(word) #will give a nested list

    #to make the list flat
    list_out = [item for items in list_out for item in items]

    return list_out

##############################################################
# Fonction : punctuation_out
# 	- Transforme tous les caracteres de ponctuation en espace
# Input :
##############################################################
#Test written
def all_but_point_and_word_list_from_list(list_in) :
    ''' erase all punctuation except the points from word in list
    >>> a = "j'ai joué au basket 2 fois.".split()
    >>> b = punctuation_sep_word_list_from_list(b)
    >>> b = ["j'ai" , 'joué' , 'au' , 'basket' , '2' , 'fois', '.' ] '''

    list_out = []
    word = ''

    for elt in list_in :
        word = re.findall(r"[\w']+|[.]" , elt)

        list_out.append(word) #will give a nested list

    #to make the list flat
    list_out = [item for items in list_out for item in items]

    return list_out

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
