#!/usr/bin/env python3
#-*- coding : utf8 -*-


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble les functions de
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#	+ split_str_into_list_of_sentences()
#	+ maj_to_min_list_from_list()
#	+ punctuation_sep_word_list_from_list()
#	+ all_punctuation_out_list_from_list()
#	+ all_but_point_and_word_list_from_list()
#       + all_three_points_become_one_string_from_string()
#       +
#       + du_texte_a_sa_liste_exploitable_par_word_distribution()
#       + du_texte_a_sa_liste_exploitable_par_tagging()
########################################################

import re

import modules.others as others
import modules.stats_0_distributions as  stats_0_distributions

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
        #DANS CE CAS "j'y" serais considéré comme 2 entités
        word = re.findall(r"[^\W_]+|[.]{1,3}|[,!?;]" , elt)
        #DANS CE CAS "j'y" serais considéré comme 1 entités
        #word = re.findall(r"[\w']+|[.]{1,3}|[,!?;]" , elt)

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
    >>> b = ["j'ai" , 'joué' , 'au' , 'basket' , '2' , 'fois', '.' ]
    >>> PB si les trois points sont colles '''

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

def all_three_points_become_one_string_from_string(string) :
    ''' a = 'abcd ... efgh ... ijk...'
    >>> e = all_but_one_point_and_word_string_from_string(a)
    >>> e
    'abcd . efgh . ijk.' '''

    str_in = string
    str_out = ''

    for index, char in enumerate(str_in):
        if char == '.' and str_in[index-1] == '.' :
            pass
        else :
            str_out += char

    return str_out

def du_texte_a_sa_liste_exploitable_par_word_distribution(path_file):
        #IMPORTER LE TEXTE EN UNE STR
        file_as_string = others.import_text_as_one_string(path_file)
        # ENLEVER LES 3 POINTS : STR
        string_2 = all_three_points_become_one_string_from_string(file_as_string)
        # CONVERTIR EN LISTE : LIST
        liste_1 = string_2.split()
        # MINUSCULE
        liste_2 = maj_to_min_list_from_list(liste_1)
        # SEPARER LA PONCTUATION DES MOTS LIST : LIST
        liste_3 = punctuation_sep_word_list_from_list(liste_2)

        return liste_3

def du_texte_a_sa_liste_exploitable_par_tagging(path_file):
    #IMPORTER LE TEXTE EN UNE STR
    file_as_string = others.import_text_as_one_string(path_file)
    # ENLEVER LES 3 POINTS : STR
    string_2 = all_three_points_become_one_string_from_string(file_as_string)
    # CONVERTIR EN LISTE : LIST
    liste_1 = re.split("[.!?]", string_2) #use of multidelimiters
    # MINUSCULE
    liste_2 = maj_to_min_list_from_list(liste_1)
    # SEPARER LA PONCTUATION DES MOTS LIST : LIST
    #liste_3 = punctuation_sep_word_list_from_list(liste_2)
    #
    #print(liste_3)

    #Retourne un liste de phrase !
    return liste_2


if __name__ == '__main__':
    pass
