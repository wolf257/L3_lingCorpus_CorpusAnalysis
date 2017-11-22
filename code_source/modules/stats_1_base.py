#!/usr/bin/env python3
#-*- coding : utf8 -*-

from collections import OrderedDict

#from ponctuation_texte import *
#import ponctuation_texte as PT

########################################################
# LIST FUNCTIONS IN MODULES
#	+ count_sentences_nb_from_list_words_with_point
#	+
#	+
########################################################

#########
#TODO : creer moyen d'acces, surtout aux dicos
#########


##############################################################
# Fonction : nb_sentences_from_list_words_with_point
# 	- calcule le nombre de mots et le nombre de point
#	le quotient de leur division donne le nombre de phrase
# Input : list
# Return : number
##############################################################
# prend comme marqueur le '.'
# calcul nombre de mot, nombre de '.' et divise
def count_sentences_nb_from_string_or_list(list_words):

    liste_a_traiter = []
    #liste_a_traiter = all_but_point_and_word_list_from_list(list_words)
    sentences = 0

    for word in list_words :
        if word == '.' :
            sentences += 1

    return sentences

#print(count_sentences_nb_from_string_or_list([2,3,4,5,'.','.']))
##############################################################
# Fonction : nb_average_words_by_sentence
# 	- calcule le nombre de mots et le nombre de point
#	le quotient de leur division donne le nombre de phrase
# Input : list
# Return : number
##############################################################
# prend comme marqueur le '.'
# calcul nombre de mot, nombre de '.' et divise
def average_words_by_sentence_nb_from_(list_words_with_point):

    words, average_words_by_sentence, sentences = 0, 0, 0

    for word in list_words_with_point :
        if word == '.':
            sentences += 1
        #TODO : creer fonction pour separer les points des mots from string
        # PUIS creer la liste
        # NB : pour l'instant 'je.' n'augmentera pas le nb de phrase ET tombe dans le else.

        else :
            words += 1

    try:
        average_words_by_sentence = words / sentences
    except ZeroDivisionError as error :
        average_words_by_sentence = words

    return average_words_by_sentence

#TEST
# a = 'je vais jouer au basket. je reviens'
# b = a.split()
# c = 0
# c = nb_average_words_by_sentence(b)
# print("On a une moyenne de mots/phrase de : " , c)

##############################################################
# Fonction : wordbyValue
# 	-
# Input : dict
# Return : dict
##############################################################
# def wordbyValue(nom_dico) :
    # '''Reverse mot -> occurence pour occurence vers mots
    # Retour : dictionnaire
    # Classement : par frequence '''
    #
    # wordbyValue = {}
    # wordbyValue = dict([[value, key] for key, value in nom_dico.items()])
    #
    # return wordbyValue

    #PB : la key est uniq donc si plusieurs mots ont la même value, seul le dernier sera retenu.

##############################################################
# Fonction : nbres_vs_forme
# 	- calcul le nombre de mots vs le nombre de formes differentes
# Input :
# Return :
##############################################################





if __name__ == '__main__':
    pass
