#!/usr/bin/env python3
#-*- coding : utf8 -*-

import os
import re

## Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_TEST_ROOT, MORPHALO_ROOT, RESULT_RAPPORT_ROOT
###################################################################################

########################################################
# LIST FUNCTIONS IN MODULES
#	+ dot_text_files_from_folder_as_list
#	+ import_text_as_list_of_strings
#	+ import_text_as_list_of_words
#	+ import_real_dictionnary
#	+
#	+
#	+
#	+
#	+
#	+
########################################################

##############################################################
# Fonction : dot_text_files_from_folder_as_list
# Input : text
# Return : list
##############################################################
def dot_text_files_from_folder_as_list(path_to_folder):
    ''' Import the content of a folder as one list '''

    liste_finale = []

    for fichier in os.listdir(path_to_folder) :
        if fichier.endswith('.txt') :
            liste_finale.append(fichier)

    return liste_finale

# dossier_corpus = CORPUS_TEST_ROOT
# liste_fichiers_texte = dot_text_files_from_folder_as_list(dossier_corpus)
# print(liste_fichiers_texte)

##############################################################
# Fonction : import_text_as_list_of_words
# Input : text
# Return : list
##############################################################
def import_text_as_list_of_strings(path_to_text):
    ''' Import a text as one list of strings '''

    liste_brute = []
    liste_finale = []

    with open(path_to_text, 'rt', encoding='utf8') as file :
        liste_brute = file.readlines()
        #list of all lines (from beg to EOL)

    for string in liste_brute :
            liste_finale.append(string.strip())

    #PHRASE PAR PHRASE
    # for string in liste_brute :
    #         liste_finale.append(string.strip().split())

    #to make the list flat
    # liste_finale = [item for items in liste_finale for item in items]

    # return liste_brute
    return liste_finale

##############################################################
# Fonction : import_text_as_list_of_words
# Input : text
# Return : list
##############################################################
def import_text_as_list_of_words(path_to_text):
    ''' Import a text as one list of words '''

    liste_brute = []
    liste_finale = []

    with open(path_to_text, 'r', encoding='utf8') as file :
        liste_brute = file.readlines()
        #list of all lines (from beg to EOL)

    #MOT PAR MOT
    for elt in liste_brute :
        word = re.findall(r"[\w']+|[.,!?;]" , elt)

        liste_finale.append(word) #will give a nested list

    #to make the list flat
    liste_finale = [item for items in liste_finale for item in items]

    #LETTRE PAR LETTRE
    # for string in liste_brute :
    #     for word in string :
    #         liste_finale.append(word.strip())

    return liste_finale

# a = import_text_as_list_of_words(CORPUS_TEST_ROOT+"/all_montaigne_essais.txt")
# print("a est de type : " , type(a) , " de taille : " , len(a))
#
# for i in range(5):
#     print("Le mot " , i , " est : " , a[i])

# corpus = CORPUS_TEST_ROOT
# for elt in os.listdir(corpus) :
#     if elt.endswith('.txt') :
#         print(os.path.join(corpus, elt))

##############################################################
# Fonction : import_real_dictionnary
# 	- va transformer le dictionnaire (lang) en liste
# Input : file
# Return : liste
##############################################################
def import_real_dictionnary(file):

    pass

##############################################################
# Fonction : words_in_dict_or_not
# 	- va regarder si chaque mot du fichier existe dans le dictionnaire
#	si dans le dico --> list_in_dict + counter
# 	si non --> list_not_in_dict + counter
# Input : liste, liste
# Return :
##############################################################
def words_in_dict_or_not(file_as_list, dict_as_list):

    list_in_dict = []
    count_in = 0
    list_not_in_dict = []
    count_out = 0

    pass

if __name__ == '__main__':
    pass
