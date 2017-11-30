#!/usr/bin/env python3
#-*- coding : utf8 -*-

import re

########################################################
# LIST FUNCTIONS IN MODULES
#	+ split_str_into_list_of_sentences
#	+ maj_to_min_list_from_list
#	+ punctuation_sep_word_list_from_list
#	+ all_punctuation_out_list_from_list
#	+ all_but_point_and_word_list_from_list
########################################################

def split_str_into_list_of_sentences(the_string):
    ''' break a paragraph into sentences
        and return a list '''
    # to split by multile characters
    #   regular expressions are easiest (and fastest)

    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(the_string)

    liste_finale = []

    for phrase in sentenceList :
        if phrase != '' :
            liste_finale.append(phrase.strip())

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
    NOTE : les 3 points '...' sont considéré comme bloc
    >>> a = "j'ai joué... au basket.".split()
    >>> b = punctuation_sep_word_list_from_list(b)
    >>> b = ["j'ai" , 'joué' , '...' , 'au' , 'basket' , '.'] '''

    list_out = []
    word = ''

    for elt in list_in :
        word = re.findall(r"[\w']+|[.]{1,3}|[,!?;]" , elt)

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
    #list_in = re.split(r'[\.{3}]| ', list_in)

    for elt in list_in :
        if elt == '...' :
            pass
        else :
            word = re.findall(r"[\w']+|[.]" , elt)
            list_out.append(word) #will give a nested list

    #to make the list flat
    list_out = [item for items in list_out for item in items]

    return list_out

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
