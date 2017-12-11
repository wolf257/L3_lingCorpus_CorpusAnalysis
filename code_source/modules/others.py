#!/usr/bin/env python3
#-*- coding : utf8 -*-


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble les functions de
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
import re
import sys
import io
import codecs
import subprocess

# Lien vers les dossiers de la racine ############################################
#parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#os.sys.path.insert(0, parentdir)
#from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

########################################################
# LIST FUNCTIONS IN MODULES
#       + conversion_pdf_to_text()
#       + creation_folder()
#       +
#       +
#	+ list_text_in_folder_as_list + test
#	+ import_text_as_one_string + test
#	+ import_text_as_list_of_strings + test (obsolete)
#	+ import_text_as_list_of_words + test (obsolete)
#	+ import_real_dictionnary
#	+
#	+ recherche_occurence_mot_in_file_distribution()
#	+
#	+
#	+
#	+
########################################################

##############################################################
# Fonction : conversion_pdf_to_text
##############################################################
def conversion_pdf_to_text(path_to_file, name_script_bash='convert.sh'):
    print('LANCEMENT DU SCRIPT : ' , name_script_bash , ' .' )
    subprocess.call(path_to_file+name_script_bash, shell=True, cwd=path_to_file)
    print('FIN DU SCRIPT')

##############################################################
# Fonction : creation_folder
##############################################################
def creation_folder(path_to_parent, name_folder):
    print('\n+++ Création du dossier : ' , name_folder)
    try :
        if not os.path.exists(path_to_parent + name_folder + '/') :
            os.makedirs(path_to_parent + name_folder + '/')
    except :
        print('\tPROBLEME LORS DE LA CREATION DU DOSSIER.')
    else :
        print('\tCréation du dossier réussi.')


##############################################################
# Fonction : list_text_in_folder_as_list
# Input : text
# Return : list
##############################################################
def list_text_in_folder_as_list(path_to_folder):
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
# Fonction : import_text_as_one_string
# Input : path_to_text
# Return : string
##############################################################
def import_text_as_one_string(path_to_text):
    ''' Import a text as one string '''

    liste_brute = []
    liste_finale = []
    string_from_text = ''

    #list of all lines (not sentences) (from beg to EOL)
    # [l1 , l2 , l3 , ...]
    with codecs.open(path_to_text, mode = 'r', encoding='utf8') as file :
        liste_brute = file.readlines()

    #enlevons les \n \r ...
    for string in liste_brute :
            liste_finale.append(string.strip())


    string_from_text = ' '.join(liste_finale)
    # " l1 ' ' l2 ' ' l3 ' ' ... "

    return string_from_text

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

##############################################################
# Fonction : recherche_occurence_mot_in_file_distribution
# Input :
# Return :
##############################################################
def recherche_occurence_mot_in_file_distribution(path_to_file, mot_a_chercher) :
    #
    try :
        #OPEN FILE
        file = codecs.open(path_to_file, mode='r', encoding='utf8')
    except :
        print('\tPROBLEME LORS DE L\'OUVERTURE DU FICHIER.')
    else :
        print('\tOuverture du fichier réussi.')

        nb = 0
        nb_occurence  = []
        mot = re.compile(mot_a_chercher+' : (\d*)')
        #
        for line in file :
            nb = mot.findall(line)
            #
            nb_occurence += nb
            #

    return int(nb_occurence[0])
