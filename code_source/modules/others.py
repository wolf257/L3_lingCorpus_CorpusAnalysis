#!/usr/bin/env python3
#-*- coding : utf8 -*-

##############################################################
# Fonction : import_text_as_list
# Input : text
# Return : list
##############################################################
def import_text_as_list(text):
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
